from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
try:
    driver.get('https://www.news29.ru/novosti/ekonomika/')
    time.sleep(3)  # Подождать загрузку (можно увеличить при медленном интернете)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Поиск  ссылок
    links = soup.select('a[href*="/novosti/"]')

    if not links:
        print("Ссылки на новости не найдены.")
    else:
        for i, tag in enumerate(links, 1):
            text = tag.get_text(strip=True)
            href = tag.get('href', 'нет ссылки')
            # Приводим href к абсолютной ссылке, если нужно
            if href.startswith('/'):
                href = 'https://www.news29.ru' + href
            print(f"{i}. {text} | Ссылка: {href}")

finally:
    driver.quit()