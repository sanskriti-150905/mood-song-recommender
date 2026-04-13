# Mood-Based Song Recommendation System

## Project Overview
- Machine learning system to classify songs into mood categories.
- Recommends songs based on selected mood.
- Deployed using Streamlit for user interaction.

## Objectives
- Analyze audio features of songs.
- Classify songs into moods: Happy, Sad, Calm, Energetic.
- Compare multiple models and select the best.
- Provide a simple GUI for recommendations.

## Methodology
- Dataset loading and exploration
- Data preprocessing
- Feature selection and engineering
- Model training:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Voting Classifier
- Model evaluation and comparison
- Best model selection (Random Forest)
- GUI implementation using Streamlit

## Features Used
- valence
- energy
- danceability
- tempo
- loudness
- acousticness

## Results
- Random Forest achieved ~89% accuracy.
- System successfully classifies and recommends songs based on mood.

## Project Structure
- mood.py – Streamlit application
- model.pkl – trained model
- scaler.pkl – feature scaler
- label_encoder.pkl – label encoder
- SPL_PROJECT.ipynb – project notebook

## Dataset
- Dataset not included due to size constraints.
- Source: https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db

## How to Run
- Install dependencies:
  pip install streamlit pandas scikit-learn
- Run application:
  streamlit run mood.py

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Conclusion
- Demonstrates classification of songs based on mood using audio features.
- Provides an interactive interface for song recommendations.

## GitHub Link
- https://github.com/sanskriti-150905/mood-song-recommender
