from flask import Flask, render_template, request
from dotenv import load_dotenv

from gptapi.openai_api import basic_question, list_models
import config

# Load environment variables from .env file
load_dotenv("../.env")

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object(config.Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    model_list = list_models()
    default_model = 'text-davinci-003'

    if request.method == 'POST':
        question = request.form['question']
        selected_model = request.form['dropdown']
        response = basic_question(question, selected_model)
        return render_template('index.html', response=response, model_list=model_list, default_model=default_model)

    return render_template('index.html', model_list=model_list, default_model=default_model)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)