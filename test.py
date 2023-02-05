# starter code by OpenAI tutorial (https://platform.openai.com/docs/guides/completion)

import os
import openai
from dotenv import load_dotenv
import tts

# load .env file for environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ask user for response
p = input("Enter your question: ")

response = openai.Completion.create(
  model="text-davinci-003",
  # prompt provides examples about how to handle questions it knows and doesn't know. "p" is added in at the end.
  prompt=f"Q: Who is Batman?\nA: Batman is a fictional comic book character.\n\nQ: What is torsalplexity?\nA: ?\n\nQ: What is Devz9?\nA: ?\n\nQ: Who is George Lucas?\nA: George Lucas is American film director and producer famous for creating Star Wars.\n\nQ: What is the capital of California?\nA: Sacramento.\n\nQ: What orbits the Earth?\nA: The Moon.\n\nQ: Who is Fred Rickerson?\nA: ?\n\nQ: What is an atom?\nA: An atom is a tiny particle that makes up everything.\n\nQ: Who is Alvan Muntz?\nA: ?\n\nQ: What is Kozar-09?\nA: ?\n\nQ: How many moons does Mars have?\nA: Two, Phobos and Deimos.\n\nQ: What is the capital of France?\nA: Paris.\n\nQ:{p}",
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n\n"]
)

# cleaning up answer and sending it to TTS
answer = response["choices"][0]["text"].strip("\nA: ")
tts.synthesize_text(answer)

# response is cleaned up and printed out
print(answer)