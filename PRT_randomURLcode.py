from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import secrets
import string

list = ["List_PRT_12",
        "List_PRT_34",
        "List_PRT_56",
        "List_PRT_78"
        ]

# Base for declarative models
Base = declarative_base()

def short_id(length=8):
    characters = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(8), unique=True, nullable=False, default=lambda: short_id(8))
    task_name = Column(String(100), nullable=False)


# Create an in-memory SQLite database engine
engine = create_engine('sqlite:///:memory:')

# Create tables defined in Base
Base.metadata.create_all(engine)

# Create a sessionmaker to produce Session objects
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Example usage: Iterate through the list and create tasks
for name in list:
    task = Task(task_name=name)
    print(f"Before INSERT: task.public_id = {task.public_id}") # Will be None as public_id is assigned on commit

    session.add(task)
    session.commit()
    
    print(f"After INSERT: task.public_id = {task.public_id}")  # 8 uppercase letters and digits, e.g., XKQBMJTR
    print(f"After INSERT: task.id = {task.id}")

# You can also query all tasks after the loop to see them
print("\nAll tasks in the database:")
for task in session.query(Task).all():
    print(f"ID: {task.id}, Public ID: {task.public_id}, Name: {task.task_name}")
