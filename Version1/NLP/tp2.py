import speech_recognition as sr

transcription = ""
# Initialize recognizer class (for recognizing the speech)
def voice_recognition():
    global transcription
    recognizer = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Start Talking")
        audio_text = recognizer.listen(source, phrase_time_limit=5)
        print("Time over, thank you")

        try:
            # using google speech recognition
            transcription = recognizer.recognize_google(audio_text)
            print(transcription)
        except:
            print("Sorry, I did not get that")

    return transcription