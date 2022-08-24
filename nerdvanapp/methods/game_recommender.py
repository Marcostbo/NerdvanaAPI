from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class GameRecommender:
    def __init__(self, game_data, ids, summaries):
        self.game_data = game_data
        self.ids = ids
        self.summaries = summaries
        self.tfidf_matrix = None
        self.cosine_similarities = {}

    def create_tfidf_matrix(self):
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(self.summaries)
        self.tfidf_matrix = tfidf_matrix
