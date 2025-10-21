import os
import requests
from dotenv import load_dotenv
from datetime import datetime


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = "https://calendarific.com/api/v2/holidays"
    payload = {
      "api_key": api_key,
      "country": "RU",
      "year": "2025"
    }

    response = requests.get(url, params=payload)
    holidays = response.json()["response"]["holidays"]

    months_ru = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]

    for holiday in holidays:
        day = holiday["date"]["datetime"]["day"]
        month = holiday["date"]["datetime"]["month"]
        month = months_ru[month-1]

        name = holiday["name"]
        description = holiday["description"]

        print(f"Дата: {day} {month}, ")
        print(f"Назавание праздника: {name}, ")
        print(f"Описание: {description} \n")


if __name__ == '__main__':
    main()
