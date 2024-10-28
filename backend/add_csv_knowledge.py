import openai_util
import pandas as pd
import re
from models.knowledge import Knowledge
from app import db, app

def remove_punctuation(text):
    """Remove all punctuation from the text."""
    return re.sub(r'[^\w\s]', '', text)  # Keep only word characters and spaces

input_datapath = "../home_depot_data_2021.csv"
df = pd.read_csv(input_datapath)

# Set batch size
batch_size = 50

with app.app_context():
    # Iterate through the dataframe in batches of 50
    for start in range(0, len(df), batch_size):
        # Prepare batch data
        batch_df = df.iloc[start:start + batch_size]
        # Remove punctuation from content and join the columns
        contents = [
            remove_punctuation(", ".join([f"{col}: {str(row[col])}" for col in df.columns]))
            for _, row in batch_df.iterrows()
        ]

        # Get embeddings for the batch
        embeddings = openai_util.get_embedding_batch(contents)

        # Prepare and add Knowledge entries to the session
        for content, embedding in zip(contents, embeddings):
            n_token = openai_util.get_text_tokens(content)
            new_entry = Knowledge(
                source="Home Depot Data",
                content=content,
                embedding=embedding,
                n_token=n_token
            )
            db.session.add(new_entry)

        # Commit the batch to the database
        db.session.commit()

        # Print success message after processing each batch
        print(f"Successfully inserted batch from row {start + 1} to {min(start + batch_size, len(df))}.")

print("All rows processed and inserted successfully.")
