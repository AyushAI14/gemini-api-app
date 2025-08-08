from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from a .env file
load_dotenv()

# Get the API key from environment variables
# It's a good practice to use a more specific name like GEMINI_API_KEY
GEMINI_API_KEY = os.getenv('GEMINI_API')

# Configure the API key for the genai library
genai.configure(api_key=GEMINI_API_KEY)

# Create a generative model instance with a valid model name
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content with a text prompt
response = model.generate_content('Explain about AI')

# Print the generated text from the response
print(response.text)