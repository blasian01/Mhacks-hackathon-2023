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
    text = ""

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

    except speech_recognition.UnknownValueError:
        print("Speech recognition could not understand audio")
    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return text

def shutdown():
    text_speech.stop()
    text_speech.shutdown()

def speakGPT():
    response = GPT()
    text_speech.say(response)
    text_speech.runAndWait()
        
    shutdown()
        
text_speech = pyttsx3.init()


# Call the shutdown function before exiting the program
shutdown()

        
openai.api_key = "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"

root = tk.Tk()
root.geometry("200x150")

button1 = tk.Button(root, text="Click me", command=speak)
button1.pack(pady=10)

button2 = tk.Button(root, text="GPT", command=speakGPT)
button2.pack()

root.mainloop()
