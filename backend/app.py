from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Index, text
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4528@localhost/instalily'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Knowledge(db.Model):
    __tablename__ = 'knowledge'
    
    item_id = db.Column(Integer, primary_key=True)
    source = db.Column(String(128), nullable=False)
    source_id = db.Column(UUID(as_uuid=True), nullable=False)  # assuming UUID type for uniqueness
    chat_id = db.Column(UUID(as_uuid=True), nullable=False)
    content = db.Column(String(16384), nullable=False)
    embedding = db.Column(Vector(1536), nullable=False)

    # Index for fast retrieval on embeddings
    __table_args__ = (
        Index('ix_embedding_l2', embedding, postgresql_using='ivfflat', postgresql_with={'lists': 100},
              postgresql_ops={'embedding': 'vector_l2_ops'}),
    )
    
    def __repr__(self):
        return f"Knowledge: {self.content}"

# @app.route('/')
# def hello():
#     return 'Hey!'

# if __name__ == '__main__':
#     app.run()