
import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# Load API key from the existing .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "groq/openai/gpt-oss-20b"

# Page settings
st.set_page_config(
    page_title="MAST AI by Divya | Your Smart Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chatbot personalities
PERSONAS = {
    "Friendly": (
        "You are MAST AI by Divya, a friendly and helpful assistant. "
        "Be conversational, engaging, and clear."
    ),
    "Teacher": (
        "You are an excellent teacher. Explain concepts "
        "step by step with simple examples."
    ),
    "Coder": (
        "You are an expert programming assistant. Provide "
        "correct code and explain the important logic."
    ),
    "Creative": (
        "You are a creative assistant who suggests original "
        "ideas and interesting solutions."
    ),
    "Professional": (
        "You are a professional assistant. Give clear, "
        "structured, practical answers."
    )
}

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "persona" not in st.session_state:
    st.session_state.persona = "Friendly"

if "chats" not in st.session_state:
    st.session_state.chats = []

# Custom styling - ORIGINAL DESIGN PRESERVED
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #111c32);
    color: #edf2ff;
}

[data-testid="stSidebar"] {
    background-color: #0b1324;
    border-right: 1px solid #263653;
}

.hero {
    padding: 26px;
    border-radius: 18px;
    background: linear-gradient(120deg, #243f80, #4938a8);
    margin-bottom: 22px;
}

.hero h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 6px;
}

.hero p {
    color: #e1e7ff;
    font-size: 16px;
}

.status {
    color: #6ee7b7;
    font-size: 14px;
}

.stButton button {
    border-radius: 10px;
    border: 1px solid #43558b;
    transition: 0.2s;
}

.stButton button:hover {
    border-color: #8b9cff;
    color: #c7d2fe;
}

[data-testid="stChatMessage"] {
    background: rgba(36, 53, 82, 0.72);
    border: 1px solid #304464;
    border-radius: 15px;
    padding: 12px;
}

[data-testid="stChatInput"] {
    border-color: #5869ba;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("# 🤖 MAST AI by Divya")
    st.caption("Your Smart AI Assistant")
    st.markdown("---")

    st.markdown("### 🎭 Personality")

    selected_persona = st.selectbox(
        "Choose your assistant style",
        list(PERSONAS.keys()),
        index=list(PERSONAS.keys()).index(
            st.session_state.persona
        )
    )

    if selected_persona != st.session_state.persona:
        st.session_state.persona = selected_persona
        st.rerun()

    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")

    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("👋 New Conversation", use_container_width=True):
        if st.session_state.messages:
            st.session_state.chats.append({
                "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                "messages": list(st.session_state.messages)
            })
        st.session_state.messages = []
        st.rerun()

    if st.session_state.messages:
        chat_text = "\n\n".join(
            f"{'You' if m['role'] == 'user' else 'MAST AI by Divya'}:\n"
            f"{m['content']}"
            for m in st.session_state.messages
        )

        st.download_button(
            "⬇️ Download Chat",
            data=chat_text,
            file_name="mast_ai_by_divya_chat.txt",
            mime="text/plain",
            use_container_width=True
        )

    with st.expander("📜 Previous Conversations"):
        if st.session_state.chats:
            for i, chat in enumerate(
                reversed(st.session_state.chats), start=1
            ):
                st.caption(f"Conversation {i} · {chat['time']}")
                if st.button(
                    f"Open conversation {i}",
                    key=f"old_chat_{i}",
                    use_container_width=True
                ):
                    st.session_state.messages = list(chat["messages"])
                    st.rerun()
        else:
            st.caption("Your saved session history will appear here.")

    st.markdown("---")
    st.markdown("### 🔌 Connection")
    st.markdown(
        '<p class="status">● Groq + LiteLLM</p>',
        unsafe_allow_html=True
    )
    st.caption(f"Model: {MODEL}")

# Main page header - NAME UPDATED
st.markdown("""
<div class="hero">
    <h1>✨ Welcome to MAST AI by Divya</h1>
    <p>Ask anything, explore ideas, solve problems,
    or just have a chat!</p>
</div>
""", unsafe_allow_html=True)

if not API_KEY:
    st.error(
        "GROQ_API_KEY was not found. Check your .env file "
        "and restart the application."
    )
    st.stop()

# Welcome screen
if not st.session_state.messages:
    st.markdown("### What can I help you with today?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💡 **Learn something**\n\nUnderstand a new concept.")

    with col2:
        st.info("💻 **Write code**\n\nBuild or debug a program.")

    with col3:
        st.info("🎨 **Explore ideas**\n\nBrainstorm something creative.")

# Render existing messages
for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Message MAST AI by Divya...")

if user_input:
    # Display and store the user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Construct API messages with the current personality
    api_messages = [
        {
            "role": "system",
            "content": PERSONAS[st.session_state.persona]
        }
    ] + st.session_state.messages[-20:]

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("MAST AI by Divya is thinking..."):
            try:
                response = completion(
                    model=MODEL,
                    api_key=API_KEY,
                    messages=api_messages,
                    temperature=0.7,
                    max_tokens=1200
                )

                answer = (
                    response.choices[0].message.content or ""
                )

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                # Remove the unanswered user message
                st.session_state.messages.pop()

                st.error(
                    "Sorry, I couldn't get a response. "
                    "Check your internet connection, API key, "
                    "model access, and API quota."
                )
                st.caption(str(error))
