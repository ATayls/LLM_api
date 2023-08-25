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
    default_model = 'gpt-3.5-turbo'

    system_prompt = """You are a highly intelligent question 
                    answering bot. If you are asked a question that is
                    rooted in truth, you will give the answer. If you are asked a
                    question that is nonsense, trickery, or has no clear answer, 
                    you will respond with \"Unknown\"."""

    if request.method == 'POST':
        question = request.form['question']
        selected_model = request.form['dropdown']
        response = basic_question(question, system_prompt, selected_model)
        return render_template('index.html', question=question, response=response,
                               model_list=model_list, default_model=default_model)

    return render_template('index.html', model_list=model_list, default_model=default_model)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)