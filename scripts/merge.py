import pandas as pd


def merge_data(population: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    return population.merge(weather, on="City", how="inner")