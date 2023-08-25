import os
import openai

# Playground examples found here: https://platform.openai.com/playground
# API docs found here: https://platform.openai.com/docs/api-reference

openai.api_key = os.getenv("OPENAI_API_KEY")

def basic_question(question: str, system: str, model: str):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    result = response.choices[0].message.content
    return result


def list_models():
    """ Returns a list of model IDs """
    response = openai.Model.list()
    response['data'].sort(key=lambda x: x['id'])
    id_list = [model['id'] for model in response['data']]
    return id_list