{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc8a292e-421f-4ae3-87fb-b589fa5645b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "from flask import request\n",
    "from flask import render_template\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "986261ad-62db-4478-bfc8-599dfb7515e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__,static_folder='static')\n",
    "model=joblib.load('boston_prediction')\n",
    "@app.route('/')\n",
    "def home(name=None):\n",
    "    return render_template('index.html',name=name)\n",
    "@app.route('/index',methods=['GET','POST'])\n",
    "def get_values():\n",
    "    if(request.method=='POST'):\n",
    "        rm=float(request.form.get('rm'))\n",
    "        pt=float(request.form.get('pt'))\n",
    "        lstat=float(request.form.get('lstat'))\n",
    "        predict_value=model.predict([[rm,pt,lstat]])\n",
    "        #render result.html instead of index.html\n",
    "        return render_template('result.html',prediction=predict_value[0],rm=rm,pt=pt,lstat=lstat)\n",
    "        #if Get request, redirect to home\n",
    "        return render_template('index.html')\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "402fe05a-bc19-4370-83db-1bda53a98341",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
      " * Running on http://127.0.0.1:5000\n",
      "\u001b[33mPress CTRL+C to quit\u001b[0m\n",
      "127.0.0.1 - - [18/Aug/2026 10:08:02] \"GET / HTTP/1.1\" 200 -\n",
      "/opt/anaconda3/lib/python3.14/site-packages/sklearn/utils/validation.py:2827: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [18/Aug/2026 10:08:36] \"POST /index HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:08:52] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon-precomposed.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon-precomposed.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon-precomposed.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon-precomposed.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /apple-touch-icon.png HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [18/Aug/2026 10:09:09] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d6e1d4b-4f02-47ee-9ee0-a5a52d1e5777",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e30eb735-2804-416c-afe7-325b6e0473f4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
