import google.genai as genai
from PIL import Image
import cv2
import os
from dotenv import load_dotenv
import pyttsx3
import threading
import time

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("=" * 60)
    print(" [!] GOOGLE_API_KEY not found in local environment or .env file.")
    api_key = input(" Please paste your Gemini API Key here and press Enter: ").strip()
    print("=" * 60)

if not api_key:
    print("Error: No API key provided. Exiting application...")
    time.sleep(3)
    exit(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

client = genai.Client(api_key=api_key)

def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run, daemon=True).start()


def analyze(frame):
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    prompt = """Analyze this person briefly and bluntly:
    - If messy: "Why are you looking so messy?"
    - If tired: "Why are you looking so tired?"
    - If sad: "You look sad today bro!"
    - If happy: "You look happy today!!!"
    - If well-dressed: "Lookin' good! Keep it up!" 
    Add one quick comment about their appearance. Keep it short and blunt. Do not use any emojis."""

    response = client.models.generate_content(

        model='gemini-3.8-flash',
        contents=[prompt, img]
    )
    return response.text


cam = cv2.VideoCapture(1)
if not cam.isOpened():
    print("Error: Could not open camera")
    exit(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

last_time = 0
result = ""

print("press q to quit\n")

while True:
    success, frame = cam.read()
    if not success:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0 and (time.time() - last_time) >= 60:
        last_time = time.time()


        def process():
            global result
            result = analyze(frame)
            print(result)
            speak(result)


        threading.Thread(target=process, daemon=True).start()

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if result:
        y = 30
        for line in result.split('. '):
            if line:
                cv2.putText(frame, line[:60], (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                y += 25

    cv2.imshow('vision', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nGoodbye!")
        speak("Goodbye!")
        break

cam.release()
cv2.destroyAllWindows()
