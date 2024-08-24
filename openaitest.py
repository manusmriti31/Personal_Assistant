import os
import openai
from config import api_key
openai.api_key = api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= "How are you",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)