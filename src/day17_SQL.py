import pandas as pd
import sqlite3
conn = sqlite3.connect("C:/Users/91807/Desktop/database/internship.db")
df=pd.read_sql_query("SELECT name, track FROM interns", conn)
print(df)