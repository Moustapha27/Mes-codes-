import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors



#import du data
data = pd.read_csv('question_faq.csv')
print(data.head())


#1-traitement du langage naturel 

# Pour la tokenisation
nltk.download('punkt_tab')  
# Pour enlever les stopwords
nltk.download('stopwords') 
# Pour la lemmatisation
nltk.download('wordnet')  


#2-Tokénisation et suppression des stopwords

stop_words = set(stopwords.words('french'))

def clean_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

data['cleaned_questions'] = data['Question'].apply(clean_text)
#print(data['cleaned_questions'].head())



#3-Lematization


lemmatizer = WordNetLemmatizer()

def lemmatize_text(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

data['lemmatized_questions'] = data['cleaned_questions'].apply(lemmatize_text)
#print(data['lemmatized_questions'].head())


#4- Création d’un modèle de classification

#Utilisation de TF-IDF pour la représentation des textes
vectorizer = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x, lowercase=False)
X = vectorizer.fit_transform(data['lemmatized_questions'])


# Utiliser un modèle KNN pour la classification
model_knn = NearestNeighbors(n_neighbors=1, metric='cosine')
model_knn.fit(X)



# Prévoir une fonction pour répondre aux questions

def get_response(user_question):
    user_question_clean = clean_text(user_question)
    user_question_lemmatized = lemmatize_text(user_question_clean)
    user_question_vec = vectorizer.transform([user_question_lemmatized])
    
    # Trouver la question la plus proche
    _, idx = model_knn.kneighbors(user_question_vec, n_neighbors=1)
    return data['Réponse'].iloc[idx[0][0]]



#interaction utilisateur

while True:
    user_input = input("Vous: ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")



