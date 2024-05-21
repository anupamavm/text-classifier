from flask import Flask, render_template, request
import joblib
import os

import sklearn
print(sklearn.__version__)


app = Flask(__name__)

def load_model():
    model_path = 'naive_bayes_model.pkl'
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return joblib.load(model_path)

def map_label_to_category(label):
    target_names = [
        'atheism', 'graphics', 'ms-windows', 'pc.hardware',
        'mac.hardware', 'windows.x', 'forsale', 'autos', 'motorcycles',
        'sport.baseball', 'sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med',
        'sci.space', 'religious.christian', 'talk.politics.guns', 'talk.politics.mideast',
        'talk.politics.misc', 'talk.religion.misc'
    ]
    return target_names[label]

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_category = None
    if request.method == 'POST':
        user_input = request.form['user_text']
        print(f"User Input: {user_input}")  # Debugging line
        try:
            predicted_category = predict_category(user_input)
            print(f"Predicted Category: {predicted_category}")  # Debugging line
        except Exception as e:
            predicted_category = f"An error occurred: {str(e)}"
            print(predicted_category)  # Debugging line
    return render_template('index.html', category=predicted_category)

def predict_category(text):
    model = load_model()
    pred = model.predict([text])
    return map_label_to_category(pred[0])

if __name__ == '__main__':
    app.run(debug=True)
