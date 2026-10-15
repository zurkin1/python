from google import genai
from google.genai import types

client = genai.Client(api_key="*************************")

MODEL = "gemini-2.5-flash"
WORD = "בית ספר"

def ask_gemini(request: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            temperature=0.1)
        )
    return response.text


PROMPT = f"""
אתה משתתף במשחק אליאס שבו עליי לנחש מילת יעד  שאתה מתאר במשפט או שניים. אסור לך להזכיר את מילת היעד או כל מילה הדומה לה.
 מילת היעד  : 
{WORD }
 """

#print(PROMPT)
print(ask_gemini(PROMPT))