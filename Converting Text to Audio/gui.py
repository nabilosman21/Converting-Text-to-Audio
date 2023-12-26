from gtts import gTTS
import os
from tkinter import *

# Create the main Tkinter window
root = Tk()

# Create a canvas within the window
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Function to convert text to speech
def textToSpeech():
    text = entry.get()  # Get the text from the Entry widget
    language = 'ar'
    
    # Create a gTTS (Google Text-to-Speech) object
    output = gTTS(text=text, lang=language, slow=False)
    
    # Save the generated speech as an MP3 file named 'output.mp3'
    output.save('output.mp3')
    
    # Play the generated MP3 file
    os.system("start output.mp3")

# Create an Entry widget for user input
entry = Entry(root)

# Place the Entry widget on the canvas
canvas.create_window(200, 180, window=entry)

# Create a Button for triggering text-to-speech conversion
button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 230, window=button)

# Start the Tkinter event loop
root.mainloop()
