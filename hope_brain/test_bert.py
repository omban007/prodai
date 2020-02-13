from deeppavlov import build_model, configs
from gtts import gTTS
from playsound import playsound
import wikipedia
# import spacy

model = build_model(configs.squad.squad, download=True)

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("This is a sentence.")

for i in range(2):
    result = model(['Datta ban is working in neosoft technologies'], ['Where datta work'])
    print(result[0][0])

#tts = gTTS(result[0][0])

#tts.save('hello.mp3')
#playsound('hello.mp3')
