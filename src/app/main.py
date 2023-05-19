from flask import Flask, render_template
from dotenv import load_dotenv
import config

# Load environment variables from .env file
load_dotenv("../.env")

app = Flask(__name__)

# Load configurations from config.py
app.config.from_object(config.Config)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)