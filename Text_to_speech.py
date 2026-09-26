from gtts import gTTS

text = "Hello!!, this is einstein and i Love JESUS!!!!!!!!!!!!!!!!!!!!!!!!!!!"
tts = gTTS(text=text,lang="en")
tts.save("speech.mp3")
print("Speech success")