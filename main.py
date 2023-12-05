import spacy

# Load the 'en_core_web_sm' model
nlp = spacy.load('en_core_web_sm')

# Input text
#text = "Photo of my white notebook with the title Math"
text = "Video of me and my husband in our party and a text that says BIENVENIDO A CASA"
# Process the text with spaCy
doc = nlp(text)

# Initialize a list to store the extracted phrases
phrases = []

# Iterate through the tokens in the document
for token in doc:
    # Check if the token is a noun and not a stop word
    if token.pos_ == "NOUN" and not token.is_stop:
        phrase = token.text
        # Follow the dependency tree to find possible noun phrases
        for child in token.children:
            if child.dep_ in ("amod", "compound"):
                phrase = f"{child.text} {phrase}"
        phrases.append(phrase)

# Print the extracted phrases
print("Extracted Phrases:")
for phrase in phrases:
    print(phrase)


''''
The key difference between the previous code and the code that successfully extracts the desired phrases "white notebook" and "Math" is how we approach the text analysis. In the earlier code examples, we were focused on entity recognition, which is primarily designed to identify named entities like organizations, locations, dates, etc. However, in your example, the target phrases are not conventional named entities, which is why those approaches didn't yield the desired results.

In the code that works, we've shifted our approach to focus on the structure of the text and the relationships between words, using part-of-speech tagging and dependency parsing. This allows us to identify and extract noun phrases (in this case, "white notebook") and simple nouns ("Math") based on their grammatical and syntactic properties.'''