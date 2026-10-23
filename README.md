## Summary
End-to-end pipeline that fetches live weather from Open-Meteo, merges it with
population data, loads it into BigQuery, aggregates it with SQL, and
visualizes it in a Looker Studio dashboard.

## What changed
- `fetch_api.py`: loads the population file and calls Open-Meteo per city
- `merge.py`: joins population and weather on `City`
- `data_cleaning.py`: handles nulls, enforces dtypes (`int64`, `float64`),
  adds `Temperature_Category` (Cold/Mild/Hot)
- `bigquery_upload.py`: loads the DataFrame into `current_weather_stats`
- `main.py`: runs the whole pipeline
- Project setup: `.gitignore` (data, venv, cache, `.env`, GCP key), uv environment

## Deliverables
- Looker Studio dashboard: <https://datastudio.google.com/u/0/reporting/3d95b646-e601-4a9b-ad77-cc4265372b05/page/SrwBG>
  - Page 1: Top 5 hottest large countries (uses `vw_hottest_large_countries_top5`)
  - Page 2: all countries (uses `vw_hottest_large_countries`)
  - Drop-down filter on Temperature Category
