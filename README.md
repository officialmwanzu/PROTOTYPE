# 🤖 Aura: Your Day-to-Day Personal AI Assistant

Aura is a proof-of-concept for a modern, conversational AI assistant designed to streamline your daily routine, schedule management, and information retrieval. This project demonstrates a decoupled Frontend and a Python/Flask Backend built for easy integration with advanced Large Language Models (LLMs) and external APIs via a Tool Calling pattern.

## ✨ Features

  * **Conversational Interface:** Processes natural language queries like "What's the weather?" or "Reschedule my meeting."
  * **Decoupled Architecture:** Clean separation between the client-side interface and the API backend.
  * **Python/Flask Backend:** Lightweight and scalable API server for processing requests.
  * **Tool Calling Simulation:** Uses conditional logic in Python to simulate calling external services (e.g., Calendar, Weather) before responding to the user.
  * **Simple Frontend:** Minimalist HTML/Tailwind CSS chat interface for immediate interaction.

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | Python 3, Flask, Flask-CORS | Core logic, API routing, and AI integration handler. |
| **Frontend** | HTML, Tailwind CSS, JavaScript | User interface and AJAX communication with the backend. |
| **Core Intelligence** | Simulated LLM Response | Designed to be easily replaced by the **Gemini API** for real-world functionality. |

## 🚀 Getting Started

Follow these steps to set up and run the Aura Assistant locally.

### 1\. Backend Setup (Python/Flask)

1.  **Clone the Repository:**

    ```bash
    git clone [Your-Repo-Link-Here]
    cd aura-assistant/backend
    ```

2.  **Create a Virtual Environment and Install Dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install Flask Flask-CORS
    ```

3.  **Run the Flask Server:**

    ```bash
    python app.py
    ```

    The backend will start running on **`http://127.0.0.1:5000`**. Keep this terminal window open.

### 2\. Frontend Setup (HTML/JavaScript)

1.  **Navigate to the Frontend Directory:**

    ```bash
    cd ../frontend # Assuming your HTML file is here
    ```

2.  **Open the Interface:**
    Open the `index.html` file in your web browser.

      * *Tip:* Use a local development server like VS Code's "Live Server" extension to handle the CORS request smoothly.

## 💡 Usage

With both the backend running (Terminal 1) and the frontend open (Browser), you can test the simulated intelligence:

| Query | Expected Simulated Action |
| :--- | :--- |
| **"What's the weather like tomorrow?"** | Triggers the simulated weather check function. |
| **"I need to schedule a meeting with John."** | Triggers the simulated calendar/scheduling tool. |
| **"Can you remind me to buy milk in the morning?"** | Triggers the simulated reminder tool. |
| **"What is the capital of France?"** | Triggers the generic response/knowledge retrieval. |

## 🧩 Modularity and Expansion

The current `app.py` uses a simple `mock_ai_response()` function. To transform Aura into a fully functional assistant, the next steps would be:

1.  **Integrate Gemini API:** Replace the `mock_ai_response` function with a call to the **Gemini API** using the Python SDK.
2.  **Define Tool Schemas:** Define the Python functions (`create_event`, `get_weather`) with docstrings and type hinting, which the Gemini model will use for **Function Calling** (Tool Use).
3.  **Database Integration:** Connect the backend to a database (e.g., PostgreSQL) to persist reminders, user preferences, and conversation history.

-----

## 📄 License

This project is open-source and available under the MIT License.

## 🙋‍♀️ Contribution

Contributions are welcome\! Feel free to open issues or submit pull requests.
