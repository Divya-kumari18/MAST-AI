
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatArea = document.getElementById("chat-messages");
const welcome = document.getElementById("welcome");
const personaSelect = document.getElementById("persona");
const historyList = document.getElementById("history-list");

let messages = [];
let conversations = [];
let isSending = false;

function renderMessage(role, content) {
    const row = document.createElement("div");
    row.className = `message ${role}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = role === "user" ? "🧑" : "🤖";

    const body = document.createElement("div");
    body.className = "message-body";

    // Use textContent so model output is displayed as text,
    // not interpreted as HTML.
    body.textContent = content;
    body.style.whiteSpace = "pre-wrap";

    row.append(avatar, body);
    chatArea.appendChild(row);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function renderAllMessages() {
    chatArea.replaceChildren();

    messages.forEach(message => {
        renderMessage(message.role, message.content);
    });

    const hasMessages = messages.length > 0;
    welcome.hidden = hasMessages;
    chatArea.hidden = !hasMessages;
}

function renderHistory() {
    historyList.replaceChildren();

    if (conversations.length === 0) {
        const empty = document.createElement("p");
        empty.className = "muted";
        empty.textContent = "Your recent chats will appear here.";
        historyList.appendChild(empty);
        return;
    }

    conversations.forEach((chat, index) => {
        const button = document.createElement("button");
        button.className = "history-item";

        const firstUserMessage = chat.messages.find(
            message => message.role === "user"
        );

        button.textContent = firstUserMessage
            ? firstUserMessage.content.slice(0, 45)
            : "Conversation";

        button.title = chat.time;

        button.addEventListener("click", () => {
            saveCurrentConversation();
            messages = chat.messages.map(message => ({ ...message }));
            conversations.splice(index, 1);
            renderAllMessages();
            renderHistory();
        });

        historyList.appendChild(button);
    });
}

function saveCurrentConversation() {
    if (messages.length === 0) return;

    conversations.unshift({
        time: new Date().toLocaleString(),
        messages: messages.map(message => ({ ...message }))
    });

    // Keep a manageable number of conversations in this browser.
    conversations = conversations.slice(0, 20);
}

async function sendMessage(text) {
    if (isSending || !text.trim()) return;

    isSending = true;
    sendButton.disabled = true;
    input.disabled = true;

    const userMessage = {
        role: "user",
        content: text.trim()
    };

    messages.push(userMessage);
    renderAllMessages();

    const thinkingRow = document.createElement("div");
    thinkingRow.className = "message assistant";

    const thinkingAvatar = document.createElement("div");
    thinkingAvatar.className = "avatar";
    thinkingAvatar.textContent = "🤖";

    const thinkingText = document.createElement("div");
    thinkingText.className = "message-body";
    thinkingText.textContent = "MAST AI by Divya is thinking...";

    thinkingRow.append(thinkingAvatar, thinkingText);
    chatArea.appendChild(thinkingRow);
    chatArea.scrollTop = chatArea.scrollHeight;

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messages: messages.slice(-20),
                persona: personaSelect.value
            })
        });

        const data = await response.json();
        thinkingRow.remove();

        if (!response.ok) {
            throw new Error(data.error || "Unable to get a response.");
        }

        messages.push({
            role: "assistant",
            content: data.reply
        });

        renderAllMessages();

    } catch (error) {
        thinkingRow.remove();

        // Remove the unanswered user message so it can be retried.
        messages.pop();
        renderAllMessages();

        alert(error.message || "Could not connect to MAST AI.");
    } finally {
        isSending = false;
        sendButton.disabled = false;
        input.disabled = false;
        input.focus();
    }
}

form.addEventListener("submit", event => {
    event.preventDefault();

    const text = input.value;
    if (!text.trim() || isSending) return;

    input.value = "";
    sendMessage(text);
});

input.addEventListener("keydown", event => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        form.requestSubmit();
    }
});

document.querySelectorAll(".suggestion").forEach(button => {
    button.addEventListener("click", () => {
        input.value = button.dataset.prompt;
        input.focus();
        form.requestSubmit();
    });
});

document.getElementById("clear-chat").addEventListener("click", () => {
    if (isSending) return;

    messages = [];
    renderAllMessages();
});

document.getElementById("new-chat").addEventListener("click", () => {
    if (isSending) return;

    saveCurrentConversation();
    messages = [];

    renderAllMessages();
    renderHistory();
});

document.getElementById("download-chat").addEventListener("click", () => {
    if (messages.length === 0) {
        alert("There are no messages to download yet.");
        return;
    }

    const text = messages.map(message => {
        const speaker = message.role === "user"
            ? "You"
            : "MAST AI by Divya";

        return `${speaker}:\n${message.content}`;
    }).join("\n\n");

    const blob = new Blob([text], {
        type: "text/plain;charset=utf-8"
    });

    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");

    link.href = url;
    link.download = "mast_ai_by_divya_chat.txt";
    link.click();

    URL.revokeObjectURL(url);
});

renderAllMessages();
renderHistory();
