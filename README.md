# Text Classifier App using Flask and Naive Bayes

This repository contains a simple text classifier web application built with Flask and a Naive Bayes machine learning model. The app allows users to input text and receive predictions about its category (e.g., spam vs. not spam, sentiment analysis, topic classification).

## Features

- **Text Classification**: The app uses a pre-trained Naive Bayes model to classify input text into predefined categories.
- **Web Interface**: Users can interact with the app through a straightforward web interface.
- **Bootstrap CSS**: The frontend is designed using Bootstrap for a clean and responsive layout.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- Scikit-learn (for the Naive Bayes model)
- Pandas (for data handling)
- HTML and Bootstrap (for frontend)

## Installation

Clone this repository:

```
git clone https://github.com/anupamavm/text-classifier.git
cd text-classifier
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

Install the required packages:
```bash
pip install flask scikit-learn pandas
```
## Usage

Run the Flask app:

```bash
python app.py
```
Open your web browser and navigate to http://localhost:5000.

Enter some text in the input field and click the “Classify” button to see the predicted category.

## Dataset

The dataset used for training the Naive Bayes model was acquired from Kaggle. It contains labeled examples of text data along with their corresponding categories.

## Model Training

The Naive Bayes model was trained using the following steps:

1. **Data Preprocessing**:
   - Cleaned and tokenized the text data.
   - Removed any noise, special characters, or irrelevant information.
   - Ensured consistent formatting.

2. **Feature Extraction**:
   - Used techniques like **TF-IDF (Term Frequency-Inverse Document Frequency)** or **bag-of-words** to convert text into numerical features.
   - TF-IDF assigns weights to words based on their importance in a document relative to the entire corpus.
   - Bag-of-words represents each document as a vector of word frequencies.

3. **Model Training**:
   - Trained the Naive Bayes classifier on the processed data.
   - Naive Bayes is a probabilistic algorithm based on Bayes' theorem.
   - It assumes that features are conditionally independent given the class label.

4. **Model Evaluation**:
   - Assessed the model's performance using techniques such as **cross-validation** or a **holdout test set**.
   - Metrics like accuracy, precision, recall, and F1-score were used to evaluate the model.

Here is the  [Colab Notebook](https://colab.research.google.com/drive/1PMYX8Cldw3t051ecJ6m1CprGkkFFVpIn?usp=sharing)


## Acknowledgments

- Kaggle for providing the dataset.
- The Flask and Bootstrap communities for their excellent documentation.

