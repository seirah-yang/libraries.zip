from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import secrets
import string
import pandas as pd # Required for the batch processing part
import os # To check for file existence

# Base for declarative models
Base = declarative_base()

def short_id():
    """대문자 3 개 + 숫자 3 개 조합 (예: XKQ394)"""
    letters = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(3))
    digits = ''.join(secrets.choice(string.digits) for _ in range(3))
    return letters + digits

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(6), unique=True, nullable=False, default=lambda: short_id())
    task_name = Column(String(100), nullable=False)


# --- Section 1: Single Task Creation Example ---
print("--- Single Task Creation Example ---")

# Create an in-memory SQLite database engine for this example
single_task_engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(single_task_engine)
SingleTaskSession = sessionmaker(bind=single_task_engine)
single_task_session = SingleTaskSession()

task_single = Task(task_name="과제명_기입_단일")
print(f"Before INSERT: task.public_id = {task_single.public_id}") # Will be None

single_task_session.add(task_single)
single_task_session.commit() # Commit to generate public_id

print(f"After INSERT: task.public_id = {task_single.public_id}") # e.g., XKQ394
print(f"After INSERT: task.id = {task_single.id}")
print("-" * 30)


# --- Section 2: Batch Task Creation from CSV Example ---
print("\n--- Batch Task Creation from CSV Example ---")

# Create a fresh in-memory SQLite database engine for this example
batch_task_engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(batch_task_engine)
BatchTaskSession = sessionmaker(bind=batch_task_engine)
batch_task_session = BatchTaskSession()

# Mock creation of '/content/address.csv' if it doesn't exist
file_path = "/content/address.csv"
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write("protocol_num\n")
        f.write("DM001-BATCH-A\n")
        f.write("DM001-BATCH-B\n")
        f.write("DM001-BATCH-C\n")
    print(f"Created a mock CSV file at {file_path} for demonstration.")


try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: CSV file not found at {file_path}. Please create it or update the path.")
    df = pd.DataFrame(columns=["protocol_num"]) # Create an empty DataFrame to prevent errors

results = []

for _, row in df.iterrows():
    if "protocol_num" in row.index: # Check if column exists
        task_name = str(row["protocol_num"])
        task_batch = Task(task_name=task_name)
        batch_task_session.add(task_batch)
        batch_task_session.commit() # Commit each task for its public_id to be generated

        results.append({
            "과제번호": task_name,
            "변환된값": task_batch.public_id
        })
    else:
        print(f"Warning: 'protocol_num' column not found in row: {row.to_dict()}. Skipping this row.")

if results:
    result_df = pd.DataFrame(results)
    output_excel_path = "tasks_converted.xlsx"
    result_df.to_excel(output_excel_path, index=False)
    print(f"변환 완료: {output_excel_path}")
    print(result_df)
else:
    print("No tasks were processed from the CSV (possibly file not found or empty/missing column).")

print("-" * 30)
