import tkinter as tk
import speech_recognition as sr
import pyttsx3
import os
import openai
import gradio as gr

#checking if the button is pressed. if pressed the speech will toggle on and off
def button_pressed():
    global button_is_pressed
    button_is_pressed = True
    
def check_button():
    global button_is_pressed
    if button_is_pressed:
        #print("Button pressed")
        button_is_pressed = False
    root.after(100, check_button)
    
#functionality for the API to retrieve GPT response
def GPT(prompt):
    print("User said: " + prompt)
    
    model = "text-davinci-003" # or any other model you want to use
    
    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1000,
    n = 1,
    )
    
    print("getting GPT reply")
    GPTreply = response.choices[0].text
    print(GPTreply)
    return GPTreply

#creating a function that will activate the microphone of the device and start using googles voice recognition to get a quiry
def speak():
    print("starting...")
    text = "" #empty string to store recognized speech
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Speak now: ")
        # listen for audio input, limit to 5 seconds
        audio = r.listen(source, phrase_time_limit=3)

        # recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            text = "give me a second"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            text = "give me a second"

    return text

#chatGPT API setup -------------------------------------------------------------------------
openai.api_key = "API_KEY"

#creating the GUI of the application
root = tk.Tk()
root.title("GPT Voice Assistant")

# Set the size of the window
root.geometry("500x500")

# Create a button
def on_chat_button_click():
    while True:
        recognized_text = speak()
        print("got it")
        GPTresponse = GPT(recognized_text)
        print("going to speak")
        text_speech.say(GPTresponse)
        text_speech.runAndWait()

speak_button = tk.Button(root, text="Chat", command=on_chat_button_click, font=("Helvetica", 48), height=5, width=20)
speak_button.pack(pady=100)

#enabling the text to chat speech
text_speech = pyttsx3.init()

root.mainloop()
