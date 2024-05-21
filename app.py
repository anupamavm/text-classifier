# app.py

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

def load_model():
    # Load the trained Naïve Bayes model
    return joblib.load('naive_bayes_model.pkl')  # Replace with your actual model filename

def map_label_to_category(label):
    target_names = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','windows.x','misc.forsale','rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey','sci.crypt','sci.electronics','sci.med','sci.space','soc.religious.christian','talk.politics.guns','talk.politics.mideast','talk.politics.misc','talk.religion.misc']  # Replace with your actual target names
    return target_names[label]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_text']
        predicted_category = predict_category(user_input)
        return render_template('result.html', category=predicted_category)
    return render_template('index.html')

def predict_category(s):
    model = load_model()
    pred = model.predict([s])
    return map_label_to_category(pred[0])  # Map numeric label to category name

#__main_
if __name__ == '__main__':
    app.run(debug=True)
