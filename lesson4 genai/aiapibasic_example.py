from google import genai

client = genai.Client(api_key="")

# The client may also get the API key from the environment variable `GEMINI_API_KEY`.

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="ספר לי בדיחה"
)
print(response.text)

#for model in client.models.list():
#    print(model.name)