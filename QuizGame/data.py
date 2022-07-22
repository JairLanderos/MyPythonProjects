import requests

QUESTIONS_AMOUNT = 5
TYPE = "boolean"

response = requests.get(url=f"https://opentdb.com/api.php?amount={QUESTIONS_AMOUNT}&type={TYPE}")
response.raise_for_status()
question_data = response.json()["results"]
