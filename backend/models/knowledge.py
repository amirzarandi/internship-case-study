from sqlalchemy import Column, Integer, BigInteger, String, Index
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'knowledge'

    id = Column(Integer, primary_key=True)
    source = Column(String(128), nullable=False)
    content = Column(String(16384), nullable=False)
    n_token = Column(BigInteger, nullable=False)
    embedding = Column(Vector(1536), nullable=False)

    __table_args__ = (
        Index('ix_embedding_l2', embedding, postgresql_using='ivfflat',
              postgresql_with={'lists': 100}, postgresql_ops={'embedding': 'vector_l2_ops'}),
    )

    def __repr__(self):
        return f"Knowledge: {self.content}"