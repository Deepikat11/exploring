from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyDhGoNL_zZyBU2PLHfMVztk-FUZPIwjznU")  # Replace with your API key

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use an available model

# Initialize Flask app
app = Flask(__name__)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    
    # Get response from Gemini API
    response = model.generate_content(user_message)
    
    return jsonify({"response": response.text})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
