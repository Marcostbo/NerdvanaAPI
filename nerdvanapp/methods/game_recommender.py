from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class GameRecommender:
    def __init__(self, game_data):
        self.game_data = game_data
        self.tfidf_matrix = None
        self.cosine_similarities = {}
