import spacy
import unidecode
import csv
import os
import logging
import copy
import warnings
warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)

#large-english-web====================
nlp = spacy.load("en_core_web_lg")
#=====================================

def nlpTreatment(strInput):
    strInput = unidecode.unidecode(strInput) #Acentos
    #Model applied to strInput
    doc = nlp(strInput)
    lemmaInput = []
    posTag = []
    for token in doc:
        lemmaInput.append(token.lemma_)
        posTag.append(spacy.explain(token.pos_))
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    print(f"\nPosTag: \n{posTag}\n")
    print(f"\nEntities: \n{entities}\n")    

    availableClasses = getAvailableClasses()
    
    bestAlternative = {'score': 0, 'word': ""}

    alternative = ["",""]
    outList = []

    for i,tag in enumerate(posTag):
        if "noun" in tag:
            inputWordNoun = lemmaInput[i]
            if tag not in availableClasses:
                #print(f"\n\nBuscando alternativa para {inputWordNoun}.")
                #print(f"La palabra {inputWordNoun} is a {tag}")
                word = nlp(inputWordNoun)
                for wordC in availableClasses:
                    wordCompareVector = nlp(wordC)
                    similarity = word.similarity(wordCompareVector)
                    actual = similarity
                    if wordCompareVector and len(wordCompareVector.vector) > 0:
                        if actual > bestAlternative['score']:
                            bestAlternative['score'] = actual
                            bestAlternative['word'] = wordC
                    #print(f"Similarity: {word} - {wordC} =  {similarity}") 
            else:
                print(f"La clase si existe: {inputWordNoun} => {inputWordNoun}")
                            
            if bestAlternative['word'] != '' and bestAlternative['score'] != 0.0:
                print(f"\n Alternativa para {inputWordNoun} => {bestAlternative}\n")
                alternative[0] = inputWordNoun
                alternative[1] = bestAlternative['word']
                outList.append(copy.deepcopy(alternative))

            else:
                print(f"No se encontró nada relacionado a {inputWordNoun}")

    return outList
 
def getAvailableClasses():
    path = "./classes.csv"
    availableClasses = []
    try:
        with open(path,"r",encoding="utf8") as file:
            for line in file:
                if line not in availableClasses:
                    availableClasses.append(line.strip())
    except:
        print(f"Error en el documento {path}")
    return availableClasses

def start():
    print("Bienvendo a QUEARE")
    entrada = input("¿Qué deseas buscar?    : ")

    print("="*60)
    print("Procesando entrada")
    print("="*60)
    outList = nlpTreatment(entrada)
    return outList
