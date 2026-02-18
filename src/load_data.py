import os
import requests

DATA_URL = "https://data.gov.ua/dataset/sports-rules/resource/1208ea90-47e7-46a0-a5ad-b91c15bd3cd6/download/sports-rules.csv"

OUTPUT_DIR = "data/raw"
OUTPUT_FILE = "sports_rules.csv"


def download_data():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Починаю завантаження...")

    response = requests.get(DATA_URL)

    if response.status_code == 200:
        path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

        with open(path, "wb") as f:
            f.write(response.content)

        print("Файл успішно збережено:", path)
    else:
        print("Помилка завантаження:", response.status_code)


if __name__ == "__main__":
    download_data()
