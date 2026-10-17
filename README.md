<div align="center">

# 👁️ Vision Analyzer

</div>

A fun python app that uses your webcam to spot your face, sends the frame to Google's Gemini API, and roasts your appearance loud. 

## See It In Action
![Demo](demo/Demo.gif)

### Terminal Output

<img width="819" height="334" alt="terminal output" src="https://github.com/user-attachments/assets/05070cd3-ba17-40ce-aacd-515ad5dc239c" />

### Demo video

https://github.com/user-attachments/assets/09994e55-8186-4fdb-94ee-f6ed0f8073b2

## Quick Start

1.  [Latest Release](https://github.com/Adnanosman9/Appearance_Speak/releases) is here. Download it. 
2. Install the required libraries:
   ```bash
   pip install google-generativeai opencv-python python-dotenv Pillow pyttsx3
   ```
3. Create a `.env` file in the root folder and add your API key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
4. Run the script:
   ```bash
   python Emotion_Analyzer.py
   ```
   *(Press **Q** inside the camera window to exit).*

5. ### **Star the repo guys (I like it😭).**

## How It Works
* **Face Detection:** Uses OpenCV's Haar Cascade classifier to scan frames and see if a user is sitting in front of the camera.
* **Rate Limiting:** A simple time check ensures it only triggers an API request once every 10 seconds so it doesn’t spam the server. Change it if it causes any problems. 
* **AI Analysis:** Converts the active video frame into a PIL image and sends it over to Gemini to generate a funny critique.
* **Voice Output:** Passes the AI response to `pyttsx3` to read the roast out loud.

----------------

### Additional note

Some part of the debugging was done with **Claude Sonnet 4.5** helping me figure out why things weren't working. 

**Debugged with:**

<img src="https://img.shields.io/badge/Claude-Sonnet_4.5-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Sonnet 4.5">

----------

## Troubleshooting
* **Blank Camera Feed:** Make sure no other apps (like Zoom or Discord) are using your webcam. 
* **API Issues:** Double-check that your `.env` variable matches your Google AI Studio key exactly.

## License
MIT

