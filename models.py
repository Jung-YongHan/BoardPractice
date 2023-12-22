from sqlalchemy import Column, Integer, TEXT, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base

class Question(Base):
    # 데이터베이스에서 사용할 테이블의 이름을 SQLAlchemy에 알려주기
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # author = Column(VARCHAR(10), nullable=False)
    title = Column(VARCHAR(20), nullable=False)
    content = Column(TEXT,nullable=False)
    create_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # author = Column(VARCHAR(10), nullable=False)
    content = Column(TEXT, nullable=False)
    create_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")