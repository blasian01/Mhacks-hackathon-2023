import tkinter as tk
import speech_recognition
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
    text = "" #empty string to store recognized speech
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
                
            text = recognizer.recognize_google(audio)
            text = text.lower()
                
                #if len(text) > 0 and text[-1] in (".", "?", "!"):
                    #willListen = False
                #print(f"Recognized {text}")
                
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        #continue
    return text

#chatGPT API setup -------------------------------------------------------------------------
openai.api_key = "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"

#creating the GUI of the application
root = tk.Tk()
root.title("GPT Voice Assistant")

# Set the size of the window
root.geometry("500x500")
    
# Create a button
speak_button = tk.Button(root, text="Chat", command=speak, font=("Helvetica", 48), height=5, width=20)
speak_button.pack(pady=100)

#enabling the text to chat speech
text_speech = pyttsx3.init()

while True:
    if True: 
        print("speaking button has been clicked!")
        response = GPT()
        text_speech.say(response)
        text_speech.runAndWait()
    root.mainloop()

root.mainloop()