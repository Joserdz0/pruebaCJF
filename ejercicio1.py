import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

# la url que utilizamos fue la de comunicaos de la scjn
base_url = "https://www.scjn.gob.mx/multimedia/comunicados"
current_url = base_url
page_number = 0
all_content = ""
# Note: 1 recopilacion de datos
while True:
    response = requests.get(current_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Imprimir la página actual
        print(f"Obteniendo la página {page_number}...")
        
        # Realizar el análisis del contenido HTML para extraer la información deseada
        # ...
        
        # Concatenar el contenido HTML actual a la variable all_content
        all_content += response.text
        
        # Encontrar el enlace "Siguiente"
        next_link = soup.find('a', title='Ir a la página siguiente')
        
        # Verificar si hay más páginas disponibles
        if next_link is None:
            break
        
        # Obtener la URL de la siguiente página
        current_url = base_url + next_link['href']
        page_number += 1
        # Imprimir la página actual
    else:
        print(f"No se pudo obtener la página {page_number}")
        break

# Imprimir el contenido HTML de todas las páginas
# print(all_content)
# Note: 2 extraccion de datos

# Ya unido el contenido de las paginas le damos formato
soup = BeautifulSoup(all_content, 'html.parser')

# Obtenemos los textos de los elementos que tienen tittle="Comunicado"
comunicados = soup.find_all('a', attrs={'title': 'Este comunicado se abrirá en una nueva página.'})
#Los imprimimos
for comunicado in comunicados:
    print(comunicado.text)
# Extrae el texto de los comunicados
comunicados_text = [comunicado.get_text() for comunicado in comunicados]
# Note: 3 limpieza de datos

# Descarga los recursos necesarios de NLTK
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
# Define una lista de stopwords en español
stop_words = set(stopwords.words("spanish"))

# Inicializa el lematizador de palabras
lemmatizer = WordNetLemmatizer()

preprocessed_comunicados = []


for comunicado in comunicados_text:
    # Elimina caracteres no alfanuméricos excepto letras acentuadas
    comunicado = re.sub(r"[^\w\sáéíóúüñ]", "", comunicado)

    # Tokenización
    tokens = word_tokenize(comunicado)

    # Eliminación de stopwords y palabras cortas
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and len(token) > 2]

    # Lematización
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Une los tokens preprocesados en un solo texto
    preprocessed_comunicado = " ".join(lemmatized_tokens)

    preprocessed_comunicados.append(preprocessed_comunicado)

# print(preprocessed_comunicados)



# Note: 4 limpieza de datos
nlp = spacy.load("es_core_news_sm")
# nlp sirve para procesar el texto y obtener las entidades nombradas (NER) y sus categorías (PERSON, ORG, etc.) 
# en este caso, se usa para obtener las entidades nombradas de los comunicados
doc = []
for comunicado in preprocessed_comunicados:
    doc.append(nlp(comunicado))
# creamos un array con todas las entidades nombradas
entities = []
for doc in doc:
    for ent in doc.ents:
        entities.append([ent.text,ent.label_])
# imprimimos las entidades nombradas
print(entities)
