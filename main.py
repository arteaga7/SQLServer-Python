#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:           main.py
Author:         Antonio Arteaga
Last Updated:   2025-11-28
Version:        1.0
Description:
Connection to a SQLServer DB for 2 tables and multiple values in column 'Column1'.
The query result for every table is saved in an excel file (or multiple excel files).
Dependencies:   pyodbc==5.3.0, pandas==2.3.3, openpyxl==3.1.5, python-dotenv==1.2.1,
Driver 'ODBC Driver 18 for SQL Server' installed (file "msodbcsql.msi").
Usage:          Every sql query has the form:
----
SELECT TOP 10 *
FROM dbo.[tabla1]
WHERE Column1 IN ('valor1','valor2','valor3')
----
Portability:    To make this project executable, run:
pyinstaller --onefile --add-data "pkg/.env;." main.py
"""

from pkg.modules import *
from pkg.settings import conn_str
import pyodbc


def sql_process() -> None:
    """
    DB connection and sql queries are performed, DataFrames are saved as Excel files.
    """
    try:
        conn = pyodbc.connect(conn_str)
        drivers = [driver for driver in pyodbc.drivers() if "SQL" in driver]
        print("Drivers encontrados:", drivers)
        print(f"Conexión exitosa con la DB '{DB_CONFIG['database']}'.")
        queries = construct_queries(table_list, receptorRFC_list)
        execute_queries(conn, table_list, queries)
        conn.close()

    except Exception as e:
        print("Error al conectar o ejecutar consulta:", e)


def main():
    sql_process()
    f.close()


if __name__ == "__main__":
    main()
