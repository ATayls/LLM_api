from flask import Flask, render_template, request
from dotenv import load_dotenv

from gptapi.openai_api import basic_question
import config

# Load environment variables from .env file
load_dotenv("../.env")

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object(config.Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        response = basic_question(question)  # Replace get_response with your function that generates the response
        return render_template('index.html', response=response)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)