# settings.py
"""This file calls the 'config.py' file."""
import pyodbc
import pandas as pd
import time
import math
import warnings
from pkg.config import DB_CONFIG

# Global variables ----------------------------------------
table1 = "table1"
table2 = "table2"
log_file = "process_log.txt"
path_results = "results"
# -------------------------------------------------------
receptorRFC_list = ["valor1", "valor2", "valor3"]
table_list = [table1, table2]

# File to write some text
f = open(log_file, "w", encoding="utf-8")

conn_str = (
    f"DRIVER={DB_CONFIG['driver']};"
    f"SERVER={DB_CONFIG['server']};"
    f"DATABASE={DB_CONFIG['database']};"
    f"UID={DB_CONFIG['username']};"
    f"PWD={DB_CONFIG['password']};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

# To ignore all warnings
warnings.filterwarnings("ignore")
