from sqlalchemy import select, func, literal_column
from sqlalchemy.orm import aliased

def get_embeddings_by_distance(input_embedding, budget):
    from models.knowledge import Knowledge
    from app import db

    total_tokens = 0
    context_entries = []
    batch_size=50
    batch = db.session.scalars(select(Knowledge)
                                   .order_by(Knowledge.embedding.l2_distance(input_embedding))
                                   .limit(batch_size))
    for entry in batch:
            n_tokens = entry.n_token
            if total_tokens + n_tokens > budget:
                break
            context_entries.append(entry.content)
            total_tokens += n_tokens

    context_string = "\n".join(context_entries)
    return context_string