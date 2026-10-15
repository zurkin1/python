from google import genai

client = genai.Client(api_key="")

# The client may also get the API key from the environment variable `GEMINI_API_KEY`.

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="suggest an easy word for alias game"
)
print(response.text)