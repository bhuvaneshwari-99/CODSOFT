import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise import dump

# Sample movie ratings data
data_dict = {
    'user_id': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D'],
    'movie_id': ['M1', 'M2', 'M3', 'M1', 'M2', 'M4', 'M2', 'M3', 'M4', 'M1'],
    'rating': [5, 4, 3, 4, 5, 2, 3, 4, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data_dict)

# Use Surprise's Reader to parse the ratings data
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)

# Split the dataset into a training set and a test set
trainset, testset = train_test_split(data, test_size=0.2)

# Use Singular Value Decomposition (SVD) for collaborative filtering
model = SVD()
model.fit(trainset)

# Predict ratings for the test set
predictions = model.test(testset)

# Compute and print RMSE
rmse = accuracy.rmse(predictions)


# Function to get movie recommendations for a user
def get_movie_recommendations(user_id, model, df, n_recommendations=3):
    # Get a list of all movie IDs
    all_movie_ids = df['movie_id'].unique()

    # Predict ratings for all movies not rated by the user
    user_movies = df[df['user_id'] == user_id]['movie_id'].unique()
    not_rated_movies = [movie for movie in all_movie_ids if movie not in user_movies]

    predictions = []
    for movie in not_rated_movies:
        pred = model.predict(user_id, movie)
        predictions.append((movie, pred.est))

    # Sort predictions by estimated rating and return the top n recommendations
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:n_recommendations]


# Get recommendations for user 'A'
user_recommendations = get_movie_recommendations('A', model, df)
print("Recommended Movies for User A:")
for movie, rating in user_recommendations:
    print(f"Movie ID: {movie}, Predicted Rating: {rating:.2f}")
