# 🕷️ Scrapy PEP Parser

**Scrapy PEP Parser** is a Python-based web scraper built with [Scrapy](https://scrapy.org/) to extract information from the [Python Enhancement Proposals (PEP)](https://peps.python.org/) website.  
It collects data on all PEPs — including their number, title, and status — and saves it into **two CSV files**:  
- 📄 **PEP List**: number, title, status for each proposal  
- 📊 **Status Summary**: aggregated statistics by status type


## 🧰 Tech Stack

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-Web%20Crawler-0A8C5F?logo=scrapy)](https://scrapy.org/)
[![ItemLoaders](https://img.shields.io/badge/ItemLoaders-Data%20Parsing%20Helpers-FF9800?logo=python)](https://docs.scrapy.org/en/latest/topics/loaders.html)
[![Logging](https://img.shields.io/badge/Logging-built--in-lightgrey?logo=python)](https://docs.python.org/3/library/logging.html)
[![CSV Export](https://img.shields.io/badge/CSV%20Export-built--in-blue?logo=python)](https://docs.python.org/3/library/csv.html)



## ✨ Features
- Full PEP parsing from the official Python website
- Data stored in clean CSV format
- Status aggregation with document counts
- `ItemLoaders` for structured and normalized data
- Configurable settings in `settings.py`
- Detailed logging for debugging



### 📦 Installation

1. **Clone the repository**  
```
git clone https://github.com/Riadnov-dev/scrapy_parser_pep.git

cd scrapy_parser_pep
```

2. **Create and activate a virtual environment**
```
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**

```
pip install -r requirements.txt
```

### 🚀 Usage
Run the pep spider:

```
scrapy crawl pep
```

After execution, two CSV files will be created inside the results/ directory:

pep_<datetime>.csv — full list of PEPs with number, title, and status

status_summary_<datetime>.csv — aggregated count of PEPs by status

### 📂 Project Structure

```
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
 ├── results/
 │   ├── pep_<datetime>.csv
 │   └── status_summary_<datetime>.csv
 ├── tests/
 ├── .flake8
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── scrapy.cfg
```

### 👤 Author
Nikita Riadnov

GitHub: https://github.com/Riadnov-dev
