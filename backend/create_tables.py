from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, BigInteger, String, Index
from pgvector.sqlalchemy import Vector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4528@localhost/instalily'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Knowledge(db.Model):
    __tablename__ = 'knowledge'
    
    id = db.Column(Integer, primary_key=True)
    source = db.Column(String(128), nullable=False)
    content = db.Column(String(16384), nullable=False)
    n_token = db.Column(BigInteger, nullable=False)
    embedding = db.Column(Vector(1536), nullable=False)

    __table_args__ = (
        Index('ix_embedding_l2', embedding, postgresql_using='ivfflat', postgresql_with={'lists': 100},
              postgresql_ops={'embedding': 'vector_l2_ops'}),
    )

    def __repr__(self):
        return f"Knowledge: {self.content}"

from sqlalchemy import text

with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    db.create_all()
    print("Tables created successfully.")
