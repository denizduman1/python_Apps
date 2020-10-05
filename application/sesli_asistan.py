#pip install PyAudio
#pip install SpeechRecognition
#pip install gTTS
#pip install playsound
#pip install selenium

import speech_recognition as sr
import webbrowser 

r =  sr.Recognizer()
mic = sr.Microphone()

def sesliKomut(): # ses algılama fonksiyonu
    with mic as m:
        audio = r.listen(m)
        text  = r.recognize_google(audio,language='tr-TR')
        return text

'''
def sesliYanit(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,100000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

sayHello = 0
'''

while True:
    text = sesliKomut()
    print(text)
    if(text=="kapat"or text=="Kapat"):
        print("sistem kapatılıyor.")
        break
    if("merhaba" in text) : print("merhaba")
    if("ne haber" in text): print("iyidir senden ne haber?")
    if("Google aç" in text) : webbrowser.open("https://google.com")
