import os
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
try:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        max_retries=5
    )
    response = client.models.list()
    print("Connected to OpenAI API")
except Exception as e:
    print(f"Error connecting to OpenAI API: {e}")

def get_text_tokens(text):
    encoding = tiktoken.encoding_for_model("gpt-4")
    tokens = encoding.encode(text)
    return len(tokens)

def get_messages_token(messages):
    encoding = tiktoken.encoding_for_model("gpt-4")
    prompt_tokens = 0
    for message in messages:
        prompt_tokens += 4  # Initial tokens per message
        for key, value in message.items():
            prompt_tokens += len(encoding.encode(value))
    prompt_tokens += 2  # End tokens for the overall message
    return prompt_tokens

def get_embedding(text):   
    text = text.replace("\n", " ")
    try:
        response = client.embeddings.create(
            input=[text], 
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_embedding_batch(batch):
    try:
        batch = [text.replace("\n", " ") for text in batch]
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=batch,
            encoding_format="float"  # Ensures float output
        )
        embeddings = [item.embedding for item in response.data]
        return embeddings
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_chat_completion(input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0,
            messages=input
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None