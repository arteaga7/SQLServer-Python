# SQLServer-Python
This project shows how to connect Python to a SQL Server database by using the library Pyodbc.

## Repository Structure
```
SQLServer-Python/
│
├── .gitignore
├── main.py
├── env/                # Virtual enviroment
└── requirements.txt
└── pkg                 # Contains all needded files
    └── __init__.py     # Specifies that folder 'pkg' is a Python package
    └── config.py       # Contains all configuration params
    └── modules.py      # Contains all functions
    └── settings.py     # Contains all global variables
    └── .env            # Contains all secret parameters (not provided)
```


## Details
**main.py:** Connects to a SQLServer Data Base for 2 tables and multiple values in column 'Column1'.
The query result for every table is saved in an Excel file (or multiple Excel files if there are more that 600,000 rows).

**Dependencies:**
pyodbc==5.3.0, pandas==2.3.3, openpyxl==3.1.5, python-dotenv==1.2.1, pyinstaller==6.17.0, Driver 'ODBC Driver 18 for SQL Server' installed (file 'msodbcsql.msi').

**Usage:**
Every sql query has the form:

----
SELECT TOP 10 *

FROM dbo.[tabla1]

WHERE Column1 IN ('valor1','valor2','valor3')

----

**Portability:**
To make this project executable, run:
```
pyinstaller --onefile --add-data "pkg/.env;." main.py
```

## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/arteaga7/SQLServer-Python.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
python3 -m venv env
env/Scripts/activate
pip3 install -r requirements.txt
```
For Linux:
```
python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt
```
3. Create '.env' file with your secret data.
4. Run "main.py".
