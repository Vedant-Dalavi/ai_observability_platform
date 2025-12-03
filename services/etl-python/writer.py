import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRONZE_DIR = os.path.join(BASE_DIR, "storage", "bronze")


def write_to_parquet(records):
    if not records:
        return

    os.makedirs(BRONZE_DIR, exist_ok=True)

    file_path = os.path.join(BRONZE_DIR, "logs.parquet")
    print("file_path:", file_path)
    df = pd.DataFrame(records)

     # If file exists -> append, else write fresh
    if os.path.exists(file_path):
        # append to existing parquet
        df.to_parquet(file_path, engine="fastparquet", append=True)
    else:
        # create new parquet file
        df.to_parquet(file_path, engine="fastparquet")

    print(f"Wrote {len(records)} logs to {file_path}")
