from Tkinter import *
from gtts import gTTS

import os

language = "en"

# ==================PLAY FUNCTION=======


def play():
    maneno = myText.get("1.0", "end-1c")
    output = gTTS(text=maneno, lang=language, slow=False)
    output.save("words.mp3")
    os.system("vlc words.mp3")


# ======================================


root = Tk()
root.bg = "green"
# flaticon.com has very nice icons
root.title("Phero Text to Speech")

inputValue = StringVar()
myText = Text(root, width=70, height=15, bg="white",
              fg="green", font=("verdana", 16))
myText.grid(row=0, column=0)

playButton = Button(text="play", bg="green", width=8,
                    height=2, command=play).grid(row=1)


root.mainloop()
