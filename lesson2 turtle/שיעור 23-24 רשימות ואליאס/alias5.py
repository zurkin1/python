from google import genai
from google.genai import types
import random
import turtle


client = genai.Client(api_key="*************************")
sc = turtle.Screen()
sc.setup(600,600)
sc.bgcolor("cyan")
player = turtle.Turtle()
player.pu()
player.goto(-200,200)
player.write('welcome to alias game! ',font=("Arial",28,"bold"))

MODEL = "gemini-3.5-flash"
continue_playing = True
score = 0
def ask_gemini(request: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            temperature=0.1)
        )
    return response.text

def end_game(score):
    player.clear()
    message = "YOUR SCORE: "+ str(score)
    player.write(message,font=("Arial",28,"bold"))

prompt_template = f"""
הצע רשימה של 20 מילים שמיועדות לניחוש עבור משחק אליאס
הפרד בין המילים עם פסיק
תכתוב רק את המילים, ללא מלל נוסף
"""


WORDS = ask_gemini(prompt_template)
#print("First ", WORDS)
LIST_OF_WORDS = [word.strip() for word in WORDS.split(",")]
#print("Second ", LIST_OF_WORDS)

while continue_playing:
   chosen_word = random.choice(LIST_OF_WORDS)
   #print("chosen word: "+chosen_word)
   PROMPT = f"""
אתה מששתף במשחק אליאס שבו עליי לנחש מילת יעד  שאתה מתאר במשפט או שניים. אסור לך להזכיר את מילת היעד או כל מילה הדומה לה.   
 מילת היעד  :    
   {chosen_word }
   """
   description = ask_gemini(PROMPT)
   guesed_word = turtle.textinput(description,'נחש את המילה')
   if guesed_word != chosen_word:
       continue_playing = False
       end_game(score)
   else:
       score = score + 1
       LIST_OF_WORDS.remove(guesed_word)


#print(PROMPT)
turtle.mainloop()
