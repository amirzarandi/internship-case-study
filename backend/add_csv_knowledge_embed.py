import openai_util
import pandas as pd
import re
from models.knowledge import Knowledge
from app import db, app

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)  # Keep only word characters and spaces

input_datapath = "../home_depot_data_2021.csv"
df = pd.read_csv(input_datapath)

batch_size = 50

with app.app_context():
    for start in range(0, len(df), batch_size):
        batch_df = df.iloc[start:start + batch_size]
        contents = [
            remove_punctuation(", ".join([f"{col}: {str(row[col])}" for col in df.columns]))
            for _, row in batch_df.iterrows()
        ]
        embeddings = openai_util.get_embedding_batch(contents)
        for content, embedding in zip(contents, embeddings):
            n_token = openai_util.get_text_tokens(content)
            new_entry = Knowledge(
                source="Home Depot Data",
                content=content,
                embedding=embedding,
                n_token=n_token
            )
            db.session.add(new_entry)
        db.session.commit()
        print(f"Successfully inserted batch from row {start + 1} to {min(start + batch_size, len(df))}.")

print("All rows processed and inserted successfully.")
