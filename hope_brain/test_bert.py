from deeppavlov import build_model, configs
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia
from snips_nlu import SnipsNLUEngine

engine = SnipsNLUEngine.from_path("../snips_nlu/snips_trained_model")
model = build_model(configs.squad.squad, download=False)


def brain():
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

    result = engine.parse(text)

    if result['intent']['intentName']:
        if result['slots']:
            question_text = result['slots'][0].get('rawValue')
            # print(result['slots'][0].get('rawValue'))

            wiki_text = wikipedia.summary(question_text)
            result = model([wiki_text], [text])

            print(result[0][0])
            tts = gTTS(result[0][0])

            tts.save('hello.mp3')
            playsound('hello.mp3')


if __name__ == "__main__":
    for i in range(3):
        brain()