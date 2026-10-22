import pandas as pd
import pandas_gbq
from pathlib import Path
from google.oauth2 import service_account


PROJECT_ID="lithe-vent-512412-j1"
DATASET_ID="global_weather_data"
TABLE_ID="current_weather_stats"

KEY_PATH = Path(__file__).parent / "gcp-key.json"
credentials= service_account.Credentials.from_service_account_file(KEY_PATH)

def upload_to_bigquery(df: pd.DataFrame):
    if df.empty:
        raise ValueError("cannot upload an empty DataFrame.")
    
    destination_table = f"{DATASET_ID}.{TABLE_ID}"

    pandas_gbq.to_gbq(
        dataframe=df,
        destination_table=destination_table,
        project_id=PROJECT_ID,
        credentials=credentials,
        if_exists="replace",
        progress_bar=True
    )

    print(f"Successfully uploaded {len(df)} rows to {PROJECT_ID}.{destination_table}")