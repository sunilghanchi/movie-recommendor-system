# Movie Recommendation System 
website - https://mrs-sunil.onrender.com/

 
## Overview

This project aims to build a movie recommendation system for Bollywood movies from 1950 to 2019 using content-based filtering. The recommendation system suggests movies to users based on the similarity between their preferences and the movies in the dataset.

## Dataset

The dataset used in this project contains approximately 3500 Bollywood movies released between 1950 and 2019. The dataset includes information such as movie titles, genres, actors, etc.

## Process Overview

The project involves the following steps:

1. **Data Acquisition**: Obtain the dataset containing information about Bollywood movies.
2. **Data Preprocessing**: Clean and preprocess the dataset, handling missing values, removing duplicates, and standardizing text data.
3. **Feature Engineering**: Convert text data (movie titles, genres, etc.) into numerical feature vectors using techniques like CountVectorizer or TF-IDF.
4. **Similarity Calculation**: Calculate the similarity between movies based on their feature vectors using cosine similarity.
5. **Model Building**: Build a recommendation model using the similarity scores obtained.
6. **Model Serialization**: Serialize the trained model using pickle for later use.
7. **Interface Development with Streamlit**: Create a user-friendly interface using Streamlit for users to input their preferences and receive personalized movie recommendations.
8. **Deployment on Free Cloud with Onrender Cloud**: Deploy the Streamlit app on a free cloud platform like Heroku or Streamlit's sharing platform.

## HTML Processing

The Streamlit interface will include the following components:

- **Input Form**: Users can input their preferences such as favorite movie, genre, etc.
- **Recommendation Display**: Display personalized movie recommendations based on user input.
- **User Interaction**: Allow users to interact with the interface and explore different movie recommendations.

## Usage

To run the project locally:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/bollywood-movie-recommendation.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

## Contributions

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

