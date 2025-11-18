# app.py (Flask Backend)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for the frontend running on a different port/host
CORS(app, resources={r"/api/*": {"origins": "*"}}) 

# ⚠️ IMPORTANT: In a real application, you would initialize and use the Gemini API here.
# For this blueprint, we'll use a mocked function for demonstration.

def mock_ai_response(user_prompt):
    """
    Simulates the AI's complex reasoning and response generation.
    In production, this would be a call to the Gemini API with tools enabled.
    """
    prompt_lower = user_prompt.lower()
    
    if "weather" in prompt_lower:
        # Example of a tool call result integrated into the response
        return "I checked the forecast: It's expected to be sunny in Nairobi tomorrow, perfect for an early start. Any schedule updates needed?"
    elif "meeting" in prompt_lower or "schedule" in prompt_lower:
        return "I see your calendar is open tomorrow afternoon. What time and duration should I book your meeting for?"
    elif "remind" in prompt_lower:
        return "Reminder noted! I'll remind you about that task tomorrow morning. Anything else I can help you organize?"
    else:
        return f"Hello! That's interesting. As your assistant, I've received your request: '{user_prompt}'. How can I further assist with your day-to-day tasks or schedule?"


@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint to handle user queries and return AI responses."""
    
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({"response": "Please provide a message for Aura."}), 400
    
    # Process the message through the mock AI
    ai_response = mock_ai_response(user_message)
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    # Runs on port 5000 by default, which the frontend will call.
    print("Aura Backend is starting...")
    app.run(debug=True)
