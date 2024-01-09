import spacy
import unidecode


def normalizeInput(strInput):
    strInput = unidecode.unidecode(strInput)
    #nlp = spacy.load("es_core_news_sm")
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(strInput)

    lemmaInput = []
    posTag = []
    entity = []
    for token in doc:
        lemmaInput.append(token.lemma_)
        posTag.append(spacy.explain(token.pos_))

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    print(entities)
    print(lemmaInput)
    print(posTag)

    print("\n\n\n")
    word = nlp("office")
    availableClasses = ["alpaca", "whiteboard"]

    for wordC in availableClasses:
        wordCompareVector = nlp(wordC)
        similarity = word.similarity(wordCompareVector)
        print(f"Similarity: {word} - {wordC} =  {similarity}") 
 
    

def main():
    print("Bienvendo a QUEARE")
    entrada = input("¿Qué deseas buscar?    : ")
    normalizeInput(entrada)



if __name__ == main():
    main()