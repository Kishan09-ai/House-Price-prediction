from flask import Flask, request, render_template
import joblib

app = Flask(__name__, static_folder='static')

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


if __name__ == "__main__":
    app.run()
