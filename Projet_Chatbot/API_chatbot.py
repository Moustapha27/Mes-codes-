from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from fastapi.responses import HTMLResponse

app = FastAPI()

# Chargement du fichier CSV
data = pd.read_csv('question_faq.csv')

# Téléchargement des ressources nécessaires pour NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Préparation des outils de traitement de texte
stop_words = set(stopwords.words('french'))
lemmatizer = WordNetLemmatizer()

# Fonction de nettoyage et de lemmatisation
def clean_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return [lemmatizer.lemmatize(word) for word in tokens]

# Prétraitement des questions dans le fichier CSV
data['cleaned_questions'] = data['Question'].apply(clean_text)

# Utilisation de TF-IDF pour transformer les questions en vecteurs
vectorizer = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x, lowercase=False)
X = vectorizer.fit_transform(data['cleaned_questions'])

# Modèle KNN pour trouver les réponses les plus proches
model_knn = NearestNeighbors(n_neighbors=1, metric='cosine')
model_knn.fit(X)

# Modèle de requête pour FastAPI
class QuestionRequest(BaseModel):
    user_question: str

# Fonction pour obtenir la réponse la plus pertinente
def get_response(user_question):
    user_question_clean = clean_text(user_question)
    user_question_vec = vectorizer.transform([user_question_clean])
    
    # Trouver l'indice de la question la plus proche
    _, idx = model_knn.kneighbors(user_question_vec, n_neighbors=1)
    return data['Réponse'].iloc[idx[0][0]]

# Route API pour interagir avec le chatbot
@app.post("/chatbot")
async def chatbot(request: QuestionRequest):
    user_question = request.user_question
    if not user_question:
        raise HTTPException(status_code=400, detail="Une question doit être fournie")
    
    response = get_response(user_question)
    return {"response": response}

# Route pour servir la page HTML
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot FAQ</title>
    </head>
    <body>
        <h1>Chatbot FAQ</h1>
        <div>
            <label for="user_question">Posez une question :</label>
            <input type="text" id="user_question" placeholder="Votre question...">
            <button onclick="askQuestion()">Envoyer</button>
        </div>
        
        <div>
            <h2>Réponse :</h2>
            <p id="response_text">La réponse apparaîtra ici...</p>
        </div>

        <script>
            async function askQuestion() {
                const question = document.getElementById('user_question').value;

                // Envoyer une requête POST à l'API FastAPI
                const response = await fetch('/chatbot', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_question: question }),
                });

                const data = await response.json();
                document.getElementById('response_text').textContent = data.response;
            }
        </script>
    </body>
    </html>
    """

# Lancer l'application FastAPI avec Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
