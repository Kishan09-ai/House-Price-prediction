from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__, static_folder='static')

CORS(app)

model = joblib.load('boston_prediction')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def get_values():

    if request.method == 'POST':

        rm = float(request.form.get('rm'))
        pt = float(request.form.get('pt'))
        lstat = float(request.form.get('lstat'))

        predict_value = model.predict([[rm, pt, lstat]])

        return render_template(
            'result.html',
            prediction=predict_value[0],
            rm=rm,
            pt=pt,
            lstat=lstat
        )

    return render_template('index.html')


# API for GitHub Pages
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    rm = float(data['rm'])
    pt = float(data['pt'])
    lstat = float(data['lstat'])

    prediction = model.predict([[rm, pt, lstat]])

    return jsonify({
        'prediction': float(prediction[0]),
        'rm': rm,
        'pt': pt,
        'lstat': lstat
    })


if __name__ == '__main__':
    app.run()
