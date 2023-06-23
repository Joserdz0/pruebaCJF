import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Preprocesamiento
data = pd.read_csv('ejercicio2.csv') # Asegúrate de tener un archivo CSV con preguntas y respuestas

X = data['Pregunta']
y = data['Respuesta']

# Creación de conjuntos de datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorización de las preguntas
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Entrenamiento
model = LogisticRegression()
model.fit(X_train, y_train)

# Validación
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

# Pruebas
def ask_question(question):
    question = vectorizer.transform([question])
    answer = model.predict(question)
    return answer[0]

print(ask_question("Hola, ¿cómo estás?"))