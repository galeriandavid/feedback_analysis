import flair
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import KNeighborsClassifier
import pickle


import os

file_path = os.getcwd()
print(file_path)

class FeedbackAnalisys:
    def __init__(self, 
                 sentiment_model_name='en-sentiment',
                 embedding_model_name='sentence-transformers/paraphrase-mpnet-base-v2',
                 cluster_model_path = 'feedback_analisys/knn_model.pkl'):
        self.sentiment_model = flair.models.TextClassifier.load(sentiment_model_name)
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.cluster_model = self.load_cluster_model(cluster_model_path)

    def predict(self, text):
        sentiment, probability = self.predict_sentiment(text)
        cluster = self.predict_cluster(text)
        return (sentiment, probability, cluster)

    def predict_sentiment(self, text):
        doc = flair.data.Sentence(text)
        self.sentiment_model.predict(doc)
        return [doc.labels[0].value, doc.labels[0].score]

    def predict_cluster(self, text):
        embeddings = self.embedding_model.encode([text])
        cluster = self.cluster_model.predict(embeddings)
        return cluster[0]

    @staticmethod
    def load_cluster_model(cluster_model_path):
        with open(cluster_model_path, 'rb') as f:
            return pickle.load(f)
