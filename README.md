
This project is a content-based movie recommendation system built using Python and Jupyter Notebook. It suggests movies similar to the one selected by the user, based on several key features like genres, cast, director, keywords, and more.
Features
Recommend top 5 similar movies based on a selected title

Utilizes Natural Language Processing (NLP) for text similarity

Built using popular libraries like Pandas, Scikit-learn, and Numpy

Clean and interactive design in Jupyter Notebook for better understanding

Data sourced from TMDB 5000 Movie Dataset

 Technologies Used
Python

Jupyter Notebook

Pandas

Scikit-learn (TF-IDF Vectorizer and Cosine Similarity)

Numpy

 How It Works
Data Cleaning & Preprocessing: Merge relevant columns like genres, cast, and director.

Feature Engineering: Create a "tags" column combining textual data.

Vectorization: Convert text to vectors using TF-IDF.

Similarity Calculation: Use Cosine Similarity to find the most similar movies.

Recommendation: Display top 5 recommendations based on similarity scores.

 Dataset
TMDB 5000 Movie Dataset
