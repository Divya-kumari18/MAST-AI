# 🤖 MAST AI — Your Personalized AI Assistant

### *One AI. Multiple Personalities. Endless Possibilities.*

MAST AI is a web-based AI chatbot designed to provide interactive, personalized, and context-aware conversations through multiple AI personas. Built with **Flask, Python, HTML, CSS, JavaScript, and Groq-powered LLM inference**, the application combines a clean web interface with an AI-powered backend.

The project also explores **Prompt Engineering** to customize the behavior, tone, and response style of an AI assistant for different use cases, including learning, programming, professional assistance, and creative thinking.

---

## ✨ Key Features

- 💬 **AI-Powered Conversations:** Generate responses using a large language model through the Groq API and LiteLLM.
- 🎭 **Multiple AI Personas:** Switch between five personalities based on your needs.
- 🧠 **Context-Aware Chat:** Send recent conversation history to help the model respond with relevant context.
- 🎨 **Interactive Web Interface:** Chat through a custom HTML, CSS, and JavaScript frontend.
- ⚡ **Fast Inference:** Use Groq's inference service to generate AI responses.
- 🔐 **Environment-Based API Configuration:** Keep API credentials outside the application source code.
- 🌐 **Web Deployment:** Deploy the Flask application as a web service using Render.
- 🛠️ **Prompt Engineering:** Use carefully designed system prompts to guide the assistant's behavior.

---

## 🎭 AI Personas

MAST AI supports five personas, each with its own system prompt.

| Persona | Purpose |
|---|---|
| 😊 Friendly | Provides conversational, helpful, and engaging responses. |
| 📚 Teacher | Explains concepts step by step with simple examples. |
| 💻 Coder | Helps with programming, code generation, and logic explanations. |
| 🎨 Creative | Suggests original ideas and creative solutions. |
| 💼 Professional | Provides clear, structured, and practical answers. |

The selected persona changes the system instruction sent to the language model, allowing the same underlying model to respond in different styles.

---

## 🧰 Technologies Used

### 1. Python
**Role: Backend programming language**

Python handles the application's backend logic, processes incoming chat requests, manages conversation data, and coordinates calls to the AI model.

### 2. Flask
**Role: Web framework**

Flask connects the frontend to the backend and exposes HTTP routes.

- `/` — Serves the main chatbot interface.
- `/api/chat` — Accepts chat requests through POST and returns AI-generated responses in JSON format.

Flask also handles request validation and error responses.

### 3. LiteLLM
**Role: Language model integration**

LiteLLM provides a unified interface for calling supported language models. In this project, it is used to send messages to the configured model and retrieve its response.

### 4. Groq API
**Role: AI inference service**

Groq provides the inference infrastructure used to generate responses from the configured large language model.

**Configured model:** `groq/openai/gpt-oss-20b`

The application sends the system prompt and recent conversation messages to the model through LiteLLM.

### 5. HTML5
**Role: Frontend structure**

HTML defines the structure of the chatbot interface, including the main page elements and the areas used to display conversations and controls.

### 6. CSS3
**Role: Styling and visual presentation**

CSS controls the appearance of the interface, including layout, spacing, colors, typography, and visual styling.

### 7. JavaScript
**Role: Frontend interaction**

JavaScript makes the interface interactive and communicates with the Flask backend. It can send chat requests to `/api/chat` and handle the JSON responses returned by the server.

### 8. python-dotenv
**Role: Environment variable management**

The `python-dotenv` package loads variables from a local `.env` file during development. The application reads the Groq API key through `os.getenv("GROQ_API_KEY")`.

On Render, the API key is configured through the service's Environment Variables settings.

### 9. Gunicorn
**Role: Production application server**

Gunicorn runs the Flask application in a deployment environment. It is used as the production start command on Render.

### 10. Render
**Role: Application hosting and deployment**

Render hosts the Flask web application and provides a public URL for accessing the deployed chatbot.

---

## 🧠 Prompt Engineering in MAST AI

Prompt Engineering is an important part of this project. It involves designing instructions that guide a language model to respond in a desired manner.

MAST AI uses **system prompts** to define the behavior of each persona.

For example, the Teacher persona is guided to explain concepts step by step using simple examples, while the Coder persona is instructed to provide correct code and explain important logic.

### How Prompt Engineering Is Used

1. **Role Definition:** Each persona is assigned a specific role and purpose.
2. **Response Style Customization:** Instructions guide the tone and structure of responses.
3. **Task-Oriented Behavior:** The prompts emphasize the needs of different users, such as learners and programmers.
4. **Dynamic Prompt Selection:** The application selects the system prompt based on the persona chosen by the user.
5. **Conversation Context:** Recent user and assistant messages are included with the system prompt to help the model maintain conversational relevance.

This approach demonstrates how prompt design can customize an AI application's behavior without training a separate model for every persona.

---

## ⚙️ How the Application Works

1. **User Input:** The user enters a message through the chatbot interface.
2. **Frontend Request:** JavaScript sends the conversation messages and selected persona to the Flask `/api/chat` endpoint.
3. **Request Validation:** Flask checks the submitted data, validates the persona, and filters messages to accepted roles.
4. **Prompt Construction:** The backend combines the selected persona's system prompt with recent conversation history.
5. **AI Inference:** LiteLLM sends the request to the configured Groq-hosted model.
6. **Response Processing:** Flask extracts the model's response and returns it as JSON.
7. **Frontend Display:** JavaScript receives the response and displays it in the chatbot interface.

### Architecture Overview

```text
             USER
               |
               v
       HTML + CSS Interface
               |
               v
       JavaScript (Frontend)
               |
          POST /api/chat
               |
               v
         Flask Backend
               |
       Persona System Prompt
               +
      Recent Conversation History
               |
               v
             LiteLLM
               |
               v
          Groq API
               |
               v
     Configured Language Model
               |
       AI-Generated Response
               |
               v
       Flask JSON Response
               |
               v
       Chatbot Interface
```

---

## 📁 Project Structure

```text
MAST-AI/
│
├── app.py                  # Flask backend and chat API
├── requirements.txt        # Python dependencies
├── .gitignore              # Excludes sensitive and temporary files
├── .env                    # Local environment variables (not committed)
│
├── templates/
│   └── index.html          # Main chatbot webpage
│
└── static/
    ├── style.css           # Frontend styling
    └── script.js           # Frontend interaction and API requests
```

> The `.env` file is for local development and should not be committed to GitHub. Render environment variables are configured separately.

---

## 🚀 Run the Project Locally

### Prerequisites

- Python 3 installed
- Git installed
- A Groq API key
- Internet access for AI inference

### Step 1: Clone the repository

```bash
git clone https://github.com/Divya-kumari18/MAST-AI.git
cd MAST-AI
```

### Step 2: Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If Python 3.13 is not installed, create the environment using an available compatible Python version.

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key. Never publish the real key.

### Step 5: Start the application

```bash
python app.py
```

Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment on Render

MAST AI can be deployed as a **Render Web Service** because it uses Flask for backend request handling.

Configure the service as follows:

| Setting | Value |
|---|---|
| Repository | `Divya-kumari18/MAST-AI` |
| Branch | `main` |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

### Environment Variable

Add the following in the Render service's Environment settings:

| Key | Value |
|---|---|
| `GROQ_API_KEY` | Your actual Groq API key |

After configuration, create or deploy the Web Service. Render will provide a public URL when the service is available.

**Security note:** Never expose your API key in frontend JavaScript, HTML, public commits, or screenshots.

---

## 🔒 Error Handling and Basic Security

The backend includes several useful safeguards:

- Checks whether the Groq API key is configured.
- Validates incoming chat messages.
- Accepts only `user` and `assistant` message roles.
- Limits the number of recent messages and the length of individual message content.
- Uses a default persona if an unsupported persona is submitted.
- Returns JSON error messages when a request fails.
- Keeps the API key in an environment variable rather than hardcoding it in the source code.

These measures improve basic input handling and configuration security. They do not replace a full production security review.

---

## 🎯 Learning Outcomes

Through this project, I explored:

- Building a web application with Python and Flask.
- Connecting a frontend to a backend using HTTP requests and JSON.
- Integrating a large language model through LiteLLM and the Groq API.
- Designing system prompts for persona-based AI interactions.
- Applying Prompt Engineering to customize model behavior.
- Managing API credentials through environment variables.
- Handling request validation and AI API errors.
- Preparing and deploying a Python web application on Render.
- Organizing a project into frontend, backend, and configuration files.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Persistent chat history across sessions.
- User authentication and personalized settings.
- Streaming AI responses for a more responsive experience.
- Additional personas and configurable response styles.
- Improved error messages and API usage monitoring.
- Automated tests for backend routes and request validation.
- Rate limiting and additional production security controls.

These are potential enhancements, not claims about features already implemented.

---

## 👩‍💻 Project Credits

**Developed by Divya Kumari**

MAST AI was developed as a practical exploration of AI-powered application development, API integration, and **Prompt Engineering**.

The project brings together web development and large language model integration to demonstrate how a carefully designed interface, backend API, and system prompts can work together to create a personalized AI assistant.

### Technologies at a Glance

`Python` · `Flask` · `LiteLLM` · `Groq API` · `HTML5` · `CSS3` · `JavaScript` · `Prompt Engineering` · `python-dotenv` · `Gunicorn` · `Render`

---

⭐ If you find this project interesting, consider giving the repository a star!
