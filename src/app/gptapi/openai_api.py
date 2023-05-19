import os
import openai

# Playground examples found here: https://platform.openai.com/playground
# API docs found here: https://platform.openai.com/docs/api-reference

openai.api_key = os.getenv("OPENAI_API_KEY")


def basic_question(question: str):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"""
          I am a highly intelligent question answering bot. If you ask me a question that is
          rooted in truth, I will give you the answer. If you ask me a question that is nonsense
          trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: {question}? \nA:"
      """,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["\n"]
    )
    result = response.choices[0].text
    return result
