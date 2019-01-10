from gtts import gTTS
import os
import time

end = False
# setup
while end == False:
    text = input("Enter what you want to say: ")
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("test.mp3")

    # play
    os.popen("test.mp3")
    time.sleep(2)

