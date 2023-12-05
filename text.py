import spacy

# Carga el modelo de idioma en español
nlp = spacy.load("es_core_news_sm")

# Texto de la oración
texto = "la libreta con título matemáticas"

# Procesa el texto con SpaCy
doc = nlp(texto)

# Define un patrón de coincidencia para buscar "con título [TÍTULO]"
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
patron = [{"LOWER": "con"}, {"LOWER": "título"}, {"IS_TITLE": True}]
matcher.add("TITULO_PATTERN", [patron])

# Encuentra coincidencias en el documento
matches = matcher(doc)

# Extrae el texto del título si se encuentra una coincidencia
if len(matches) > 0:
    match_id, start, end = matches[0]
    titulo = doc[start+2:end].text  # Extrae el texto del título (start+2 para omitir "con título")
    print("Título extraído:", titulo)
else:
    print("No se encontró un título en la oración.")
