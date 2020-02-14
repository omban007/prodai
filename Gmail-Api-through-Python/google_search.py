import wikipedia
import spacy

print("Loading spacy model.....")
nlp = spacy.load("en_core_web_md")
print("Spacy model loded")
while True:
    doc = nlp(input("enter ner txt:-"))
    for ent in doc.ents:
            # if ent.label_ == "PERSON":
            print(ent.text)
    # print(wikipedia.summary("iron man"))

# tell me about
# let me know about
# do you know about
# what about
# can you ask about
# explain me about docker
