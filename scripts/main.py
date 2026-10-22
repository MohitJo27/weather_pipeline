from merge import merge_data
from data_cleaning import clean_data
from bigquery_upload import upload_to_bigquery
from fetch_api import load_pop, fetch_weather_data

file = "data/population.xlsx"

def main():
    try:
        # load data
        population = load_pop(file)
        print("Population rows:", len(population))

        # featch api data
        weather = fetch_weather_data(population)
        print("Weather rows:", len(weather))

        # merge data
        merged = merge_data(population, weather)
        print("Merged rows:", len(merged))

        # cleaning
        df = clean_data(merged)

        # uploading data to bigquery
        upload_to_bigquery(df)

        print("Data uploaded to BigQuery")

    except Exception as e:
        print(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()