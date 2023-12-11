import pandas as pd
import spacy
import random as random 


nlpDescriptionsPath = "datasetImages\captions.txt"

data = pd.read_csv(nlpDescriptionsPath)

nlp = spacy.load("en_core_web_sm")


text = (data.iloc[random.randint(0, 1000),1])
print(f" >TEXT: {text}")
nlpText = nlp(text)    
    
print(f"_______Entidades_________")
for ent in nlpText.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
print(f"_______Partes de un Texto_________")
for token in nlpText:
    print(token.lemma_, token.pos_)
print(f"_______Oraciones_________")

sentences = list(nlpText.sents)

for sentence in sentences:
    print(f"{sentence}")