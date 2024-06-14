# scrapy_parser_pep

Этот проект представляет собой веб-скрапер, написанный с использованием Scrapy, для парсинга страниц PEP (Python Enhancement Proposals) с сайта peps.python.org. Парсер собирает информацию о всех PEP: номер, название и статус. Данные сохраняются в двух CSV файлах: один со списком всех PEP и другой с суммарной информацией по статусам PEP.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Riadnov-dev/scrapy_parser_pep
    cd scrapy_parser_pep
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

Для запуска паука выполните следующую команду:
```bash
scrapy crawl pep
Результаты
После выполнения парсинга будут созданы два CSV файла в директории results:

pep_<ДатаВремя>.csv: Содержит список всех PEP с номерами, названиями и статусами.
status_summary_<ДатаВремя>.csv: Содержит сводку по статусам PEP, включая общее количество документов.

Структура проекта

scrapy_parser_pep/
 ├── pep_parse/
 │   ├── spiders/
 │   │   ├── __init__.py
 │   │   └── pep.py
 │   ├── __init__.py
 │   ├── items.py
 │   ├── middlewares.py
 │   ├── pipelines.py
 │   └── settings.py
 ├── tests/
 │   └── <содержимое tests>
 ├── results/
 │   ├── pep_<ДатаВремя>.csv
 │   └── status_summary_<ДатаВремя>.csv
 ├── .flake8
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── scrapy.cfg
