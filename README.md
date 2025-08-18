# 🕷️ Scrapy PEP Parser

A **Python web scraper** built with **Scrapy** to extract data from the [Python Enhancement Proposals (PEP)](https://peps.python.org/) website.  
It collects structured information on all PEPs and saves it into **two CSV files**:  

- 📄 **PEP List** — number, title, and status for each proposal  
- 📊 **Status Summary** — aggregated statistics by status type  

---

## 🧰 Tech Stack

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Scrapy-0A8C5F?style=for-the-badge&logo=scrapy&logoColor=white"/> <img src="https://img.shields.io/badge/ItemLoaders-FF9800?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/CSV%20Export-000000?style=for-the-badge&logo=csv&logoColor=white"/> <img src="https://img.shields.io/badge/Logging-808080?style=for-the-badge&logo=python&logoColor=white"/>

---

## ✨ Features

- 🕸️ **Full PEP parsing** from the official Python website  
- 📂 **CSV export** — structured results for further analysis  
- 📊 **Status aggregation** with counts by type  
- ⚙️ **ItemLoaders** for structured and normalized data  
- 🛠️ **Configurable settings** in `settings.py`  
- 📑 **Detailed logging** for debugging and transparency  

---




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
