from google import genai
from google.genai import types
import random

client = genai.Client(api_key="*************************")

MODEL = "gemini-2.5-flash"


def ask_gemini(request: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            temperature=0.1)
        )
    return response.text

prompt_template = f"""
הצע רשימה של 20 מילים שמיועדות לניחוש עבור משחק אליאס
הפרד בין המילים עם פסיק
תכתוב רק את המילים, ללא מלל נוסף
"""


WORDS = ask_gemini(prompt_template)
print("First ", WORDS)
LIST_OF_WORDS = [word.strip() for word in WORDS.split(",")]
print("Second ", LIST_OF_WORDS)

chosen_word = random.choice(LIST_OF_WORDS)
print("chosen word: "+chosen_word)
PROMPT = f"""
אתה מששתף במשחק אליאס שבו עליי לנחש מילת יעד  שאתה מתאר במשפט או שניים. אסור לך להזכיר את מילת היעד או כל מילה הדומה לה.
 מילת היעד  : 
{chosen_word }
 """

print(PROMPT)
print(ask_gemini(PROMPT))