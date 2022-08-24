from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class GameRecommender:
    def __init__(self, game_data):
        self.game_data = game_data
        self.tfidf_matrix = None
        self.cosine_similarities = {}

    def create_tfidf_matrix(self):
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        summaries = [game[1] for game in self.game_data]
        tfidf_matrix = tf.fit_transform(summaries)
        self.tfidf_matrix = tfidf_matrix

    def create_cosine_similarities(self, game_id):
        cosine_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        for idx, row in enumerate(self.game_data):
            current_game = row[0]
            if current_game == game_id:
                similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
                similar_items = [(cosine_similarities[idx][i], self.game_data[i][0]) for i in similar_indices]
                self.cosine_similarities[row[0]] = similar_items[1:]

    def recommend(self, game_id, number_of_recommendations):
        recommendations = self.cosine_similarities[game_id][:number_of_recommendations]
        return recommendations
