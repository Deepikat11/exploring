
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDhGoNL_zZyBU2PLHfMVztk-FUZPIwjznU")  # Replace with your key

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use the latest model

# Function to chat with Gemini
def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# Interactive Chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chat_with_gemini(user_input)
    print("Gemini:", response)

