import speech_recognition as sr

# create a Recognizer object
r = sr.Recognizer()

# use a microphone as the audio source
with sr.Microphone() as source:
    print("Speak now!")
    # listen for audio input, limit to 5 seconds
    audio = r.listen(source, phrase_time_limit=5)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
