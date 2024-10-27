import os
import uuid
from typing import List
import pandas as pd
from openai import OpenAI
from app import db, app, Knowledge
from sqlalchemy import text

# Set up OpenAI client with API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    max_retries=5
)

def get_embedding(text: str, model="text-embedding-3-small", **kwargs) -> List[float]:
    # Replace newlines, which can negatively affect performance.
    text = text.replace("\n", " ")
    # Get the response object
    response = client.embeddings.create(input=[text], model=model, **kwargs)
    # Extract the embedding vector from the response object
    embedding = response.data[0].embedding  # Adjusting to handle CreateEmbeddingResponse
    return embedding

# Parameters for embedding model
embedding_model = "text-embedding-3-small"
input_datapath = "../home_depot_data_2021.csv"
chat_id = str(uuid.uuid4())
source_id = str(uuid.uuid4())  # Unique identifier for this CSV file as source_id

# Load the dataset
df = pd.read_csv(input_datapath, index_col=0)

# Wrap database operations in the app context
with app.app_context():
    # Limit to first 5 rows for demo purposes
    for _, row in df.head(5).iterrows():
        # Concatenate all columns in the row with spaces in between to form content
        content = " ".join(row.astype(str))

        # Generate the embedding for the content
        embedding = get_embedding(content, model=embedding_model)

        # Insert into database
        new_entry = Knowledge(
            source="Home Depot Data",
            source_id=source_id,
            chat_id=chat_id,
            content=content,
            embedding=embedding
        )
        db.session.add(new_entry)

    # Commit the transaction
    db.session.commit()

print("Inserted first 5 rows with embeddings into the database successfully.")