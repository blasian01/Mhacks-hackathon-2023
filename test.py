import tkinter as tk
import speech_recognition as sr
import pyttsx3
import os
import openai
import gradio as gr
import threading
    
# functionality for the API to retrieve GPT response
def GPTapi():
    # storing the words spoken in a variable to use
    recognized_text = speak()
    print("User said: " + recognized_text)
    
    prompt = recognized_text
    model = "text-davinci-003" # or any other model you want to use
    
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
        n=1,
    )
    
    GPTreply = response.choices[0].text
    print(GPTreply)
    return GPTreply

# creating a function that will activate the microphone of the device and start using Google's voice recognition to get a query
def speak():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        while True:
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language="en-US", show_all=False)
            text = text.lower()
            print(f"Recognized {text}")
            
            if text and text[-1] in ".?!":
                return text

# speak GPT response
def speakGPT():
    while True:
        response = GPTapi()
        text_speech.say(response)
        text_speech.runAndWait()
        
def start_speakGPT_thread():
    speak_thread = threading.Thread(target=speakGPT)
    speak_thread.start()
        
#------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # chatGPT API setup
    openai.api_key = "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"

    # creating the GUI of the application
    root = tk.Tk()
    root.title("GPT Voice Assistant")
    root.geometry("500x500")
    
    # Create a button
    speak_button = tk.Button(root, text="Chat", command=start_speakGPT_thread, bg="green", width=10, height=5)
    speak_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # enabling the text to chat speech
    text_speech = pyttsx3.init()

    root.mainloop()
