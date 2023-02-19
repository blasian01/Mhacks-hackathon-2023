import tkinter as tk
import speech_recognition
import pyttsx3
import os
import openai
import gradio as gr
    
#functionality for the API to retrieve GPT response
def GPT():
    #storing the words spoken in a variable to use
    recognized_text = speak()
    print("moving to GPT function")
    print("User said: " + recognized_text)
    
    prompt = recognized_text
    model = "text-davinci-003" # or any other model you want to use
    
    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1000,
    n = 1,
    )
    
    GPTreply = response.choices[0].text
    print(GPTreply)
    return GPTreply

#creating a function that will activate the microphone of the device and start using googles voice recognition to get a quiry
def speak():
    print("grabing speech")
    recognizer = speech_recognition.Recognizer()
    willListen = True
    text = "" #empty string to store recognized speech
    
    while willListen:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                if len(text) > 0 and text[-1] in (".", "?", "!"):
                    willListen = False
                    break
                #print(f"Recognized {text}")
                
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue
    print("putting string in text")
    return text
    
def speakGPT():
    while True:
        print("starting function")
        response = GPT()
        print("about to speak")
        text_speech.say(response)
        text_speech.runAndWait()
        if response.lower() == "stop":
            break

print("starting program")

text_speech = pyttsx3.init()
openai.api_key = "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"

print("running function")
speakGPT()
