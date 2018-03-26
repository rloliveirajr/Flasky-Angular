# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.exam import Exam

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = sessions.query(Exam).all()

if len(exams) == 0:
    #create and persis dummy data
    python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy")
    session.add(python_exam)
    session.commit()
    session.close()

    exams = session.query(Exam).all()

# show existing exams
print("### Exams")

for exam in exams:
    print(f'({exam.id}). {exam.title} - {exam.description}')


