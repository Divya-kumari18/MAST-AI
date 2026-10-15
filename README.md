# 🤖 MAST AI by Divya

### Your Smart AI Assistant | Prompt Engineering Project

MAST AI by Divya is an interactive AI-powered chatbot developed as part of my **Prompt Engineering learning journey**. The project explores how Large Language Models (LLMs) can be integrated into a user-friendly application and guided through carefully designed prompts to generate helpful, context-aware responses.

Built using Python and Streamlit, MAST AI provides a conversational interface where users can ask questions, explore ideas, learn new concepts, and get programming assistance. It integrates Groq's API through LiteLLM, allowing the application to communicate with an AI model without exposing API credentials in the source code.

The project combines **Prompt Engineering, LLM integration, Python development, and interactive UI design** to create a practical AI assistant.

---

## ✨ Features

- **💬 Interactive AI Chat:** Ask questions and receive AI-generated responses through a conversational interface.
- **🎭 Multiple Assistant Personalities:** Choose from five different personalities:
  - **Friendly:** Conversational, engaging, and helpful responses.
  - **Teacher:** Step-by-step explanations with simple examples.
  - **Coder:** Programming assistance, code generation, and explanations.
  - **Creative:** Brainstorming, original ideas, and creative suggestions.
  - **Professional:** Clear, structured, and practical responses.
- **🧠 Prompt-Based Behaviour:** Uses system prompts to guide the assistant's tone, role, and response style.
- **📜 Conversation History:** Maintains messages during the current Streamlit session.
- **🆕 New Conversation:** Starts a fresh chat while retaining the previous conversation in the session.
- **🧹 Clear Chat:** Clears the current conversation.
- **⬇️ Download Chat:** Exports the current conversation as a text file.
- **🎨 Custom User Interface:** Features a dark blue background, purple gradient header, styled chat messages, and a sidebar for settings and quick actions.
- **🔐 API Key Management:** Loads the Groq API key from environment variables instead of hardcoding it in the application.
- **☁️ Deployment Ready:** Can be deployed using Streamlit Community Cloud with the API key configured through its Secrets settings.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language used to build the application. |
| Streamlit | Creates the interactive web interface, chat layout, sidebar, buttons, and session state. |
| Groq API | Provides access to the hosted language model used to generate responses. |
| LiteLLM | Connects the Python application to the language model through a unified completion interface. |
| `openai/gpt-oss-20b` via Groq | The configured language model used to generate chatbot responses. |
| Prompt Engineering | Defines system instructions and assistant personalities to guide response behaviour. |
| `python-dotenv` | Loads environment variables from the local `.env` file during development. |
| Python `os` module | Reads the API key from environment variables. |
| Python `datetime` module | Adds timestamps to previous conversations. |
| Git and GitHub | Version control and source code hosting. |
| Streamlit Community Cloud | Hosting option for publishing and sharing the chatbot online. |

---

## 🧠 Prompt Engineering Concepts

Prompt Engineering is a key part of this project. Instead of using the same instructions for every interaction, MAST AI uses system prompts to define the assistant's role and expected behaviour.

### 1. Role-Based Prompting

Each personality is assigned a specific role and response style. For example, the Teacher personality is instructed to explain concepts step by step, while the Coder personality focuses on correct code and important programming logic.

### 2. System Instructions

The application passes a system message to the model before the conversation. This provides the overall instructions that guide how the assistant should respond.

### 3. Contextual Conversations

Previous messages are included in the model request, allowing the assistant to consider recent conversation context when generating a response.

### 4. Controlling Response Generation

The application configures parameters such as temperature and maximum output tokens to influence response generation.

- **Temperature:** Set to `0.7` to configure the model's response generation behaviour.
- **Maximum output tokens:** Set to `1200` to limit the length of an individual response.

### 5. Prompt Customization

Users can switch between Friendly, Teacher, Coder, Creative, and Professional modes. This demonstrates how changing the instructions supplied to an LLM can influence its response style for different tasks.

---

## ⚙️ How It Works

1. The user enters a message through the Streamlit chat interface.
2. The application retrieves the selected assistant personality.
3. A system prompt and recent conversation messages are prepared.
4. LiteLLM sends the request to the configured language model through Groq.
5. The model generates a response.
6. Streamlit displays the response and stores it in the current session's conversation history.

**Simplified workflow:**

`User Input → Streamlit → System Prompt + Chat Context → LiteLLM → Groq API → AI Response → Chat Interface`

---

## 📁 Project Structure

```text
MAST-AI/
│
├── app.py             # Main Streamlit chatbot application
├── chatbot.ipynb      # Notebook used for experimentation
├── requirements.txt   # Python dependencies
├── .gitignore         # Excludes secrets and local environment files
└── README.md          # Project documentation
```

The `.env` file and `.venv` directory are used locally and should not be committed to the public repository.

---

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer.
- A Groq API key.
- Git, if you want to clone the repository.

### 1. Clone the repository

```bash
git clone https://github.com/Divya-kumari18/MAST-AI.git
cd MAST-AI
```

### 2. Create and activate a virtual environment

Create the environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project directory and add:

```text
GROQ_API_KEY=your_actual_groq_api_key
```

Replace the placeholder with your own Groq API key.

**Security note:** Never upload your `.env` file or publish your API key on GitHub.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser to use MAST AI.

---

## ☁️ Deployment

MAST AI can be deployed using **Streamlit Community Cloud**.

1. Push the project files to GitHub.
2. Sign in to Streamlit Community Cloud using GitHub.
3. Create a new app and select the `MAST-AI` repository.
4. Set `app.py` as the main application file.
5. Add `GROQ_API_KEY` through the app's Secrets settings.
6. Deploy the application and share the generated URL.

The API key should be stored in the hosting platform's secret settings rather than committed to the repository.

---

## 🔒 Security and Limitations

- API credentials are loaded through environment variables.
- Public repositories must not contain API keys or other secrets.
- API requests consume the configured Groq account's available usage and are subject to its applicable limits and terms.
- Conversation history and previous chats are stored in Streamlit session state; they are not a permanent database and may not persist across sessions.
- The application depends on API availability, model access, network connectivity, and service limits.
- The current version does not implement user authentication or a permanent, multi-user conversation database.

---

## 🎯 Learning Outcomes

Through this project, I explored:

- Applying Prompt Engineering concepts in a working application.
- Integrating a hosted Large Language Model into a Python project.
- Designing system prompts for different assistant roles.
- Managing conversation context and application state.
- Building interactive web applications using Streamlit.
- Using environment variables for API key management.
- Organizing dependencies and preparing an application for cloud deployment.
- Combining backend API integration with user interface design.

---

## 🔮 Future Enhancements

- Add user authentication and access control.
- Store conversation history persistently in a database.
- Add streaming responses for a more responsive chat experience.
- Introduce additional assistant personalities and customizable prompts.
- Support document uploads and question answering over user-provided files.
- Add usage monitoring and safeguards against excessive API consumption.

---

## 👩‍💻 Author

**Divya Kumari**

Created as part of my learning journey in **Prompt Engineering and AI application development**.

- **GitHub:** [Divya-kumari18](https://github.com/Divya-kumari18)

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.

*MAST AI by Divya — Exploring the possibilities of Prompt Engineering and Generative AI.*
