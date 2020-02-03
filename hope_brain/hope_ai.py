from deeppavlov import build_model, configs
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr  

r = sr.Recognizer()

print ("say something2")
with sr.Microphone() as source:               
    r.adjust_for_ambient_noise(source)  # here
    print ("say something3")
    audio = r.listen(source,timeout=3)

text = r.recognize_google(audio)
try:
    print("You said " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

model = build_model(configs.squad.squad, download=True)
result = model([
                   'Some time later, a ruthless rival, Obadiah Stane, manipulates Stark emotionally into a serious '
                   'relapse. As a result, Stark loses control of Stark International to Stane, becomes a homeless '
                   'alcoholic vagrant and gives up his armored identity to Rhodes, who becomes the new Iron Man.'
                   ' Eventually, Stark recovers and joins a new startup, Circuits Maximus. Stark concentrates on '
                   'new technological designs, including building a new set of armor as part of his recuperative '
                   'therapy. Rhodes continues to act as Iron Man but steadily grows more aggressive and paranoid, '
                   'due to the armor not having been calibrated properly for his use. Eventually Rhodes goes on a '
                   'rampage, and Stark has to don a replica of his original armor to stop him. Fully recovered,'
                   ' Stark confronts Stane who has himself designed armor based on designs seized along with Stark '
                   'International, dubbing himself the Iron Monger. Defeated in battle, Stane, rather than give Stark '
                   'the satisfaction of taking him to trial, commits suicide.[49] Shortly thereafter, Stark regains'
                   ' his personal fortune, but decides against repurchasing Stark International until much later; he '
                   'instead creates Stark Enterprises, headquartered in Los Angeles..'],
               [text])


print(result[0][0])
tts = gTTS(result[0][0])

tts.save('hello.mp3')
playsound('hello.mp3')
