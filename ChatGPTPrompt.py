from openai import OpenAI
from dotenv import dotenv_values


#Load Env. settings
enviromentParameters = dotenv_values(".env")

#Set up OpenAI API key
client = OpenAI(api_key=enviromentParameters["OPENAI_API_KEY"])

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)