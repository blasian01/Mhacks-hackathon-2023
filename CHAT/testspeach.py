import tkinter as tk
import speech_recognition
import pyttsx3
import os
import openai
import gradio as gr
    
#functionality for the API to retreive GPT response
def GPT():
    #storing the words spoken in a variable to use
    recognized_text = speak()
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
        return text

def turn_on():
    speak_button.config(state='active')
    root.after(1000, turn_off)
    listen = True
    print("button is on")
    return listen

def turn_off():
    speak_button.config(state='normal')
    print("button is off")

#------------------------------------------------------------------------------------------

if __name__ == "__main__":
    #chatGPT API setup
    openai.api_key = "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"

    #creating the GUI of the application
    root = tk.Tk()
    root.title("GPT Voice Assistant")
    root.title("GPT Voice Assistant")

    # Set the size of the window
    root.geometry("1920x1080")
        
    # Create a button
    speak_button = tk.Button(root, text="Chat", command=turn_on, font=("Helvetica", 48), height=5, width=20)
    speak_button.pack(pady=100)

    #enabling the text to chat speech
    text_speech = pyttsx3.init()

    while True:
        if turn_on() == True: #if the button if pressed then get the response from GPT and speak
            response = GPT()
            text_speech.say(response)
            text_speech.runAndWait()
        root.mainloop()
        