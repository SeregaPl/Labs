import requests
import json
import time


def crawl_quotes_scroll(output_file='quotes.json'):
    all_quotes = []
    page = 1
    base_url = "https://quotes.toscrape.com/api/quotes?page={}"

    while True:
        url = base_url.format(page)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка при загрузке страницы {page}: {response.status_code}")
            break

        data = response.json()
        quotes = data.get('quotes', [])
        if not quotes:
            break

        for quote in quotes:
            all_quotes.append({
                'text': quote['text'],
                'author': quote['author']['name'],
                'tags': quote['tags']
            })

        print(f"Загружено {len(quotes)} цитат со страницы {page}")

        if not data.get('has_next', False):
            break
        page += 1
        # Опционально: небольшая задержка, чтобы не нагружать сервер
        time.sleep(0.5)

    # Сохраняем в JSON-файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_quotes, f, ensure_ascii=False, indent=2)

    print(f"Сбор завершён. Всего собрано цитат: {len(all_quotes)}. Результат сохранён в '{output_file}'")


# Запуск паука
crawl_quotes_scroll('quotes.json')
