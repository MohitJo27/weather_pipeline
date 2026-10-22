import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleaing and Normalizes the data"""

    # Handle missing values
    df.dropna(subset=["Temperature", "Population"], inplace = True)

    # Changin data type
    df["Population"] = df["Population"].astype("int64")
    df["Temperature"] = df["Temperature"].astype("float64")

    # Creating new column: Cold / Mild / Hot
    def categorize_temperature(temp):
            if temp < 15:
                return "Cold"
            elif temp < 28:
                return "Mild"
            else:
                return "Hot"

    df["Temperature_category"] = df["Temperature"].apply(categorize_temperature)

    return df