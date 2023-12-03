import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\akbar\Documents\DigitalSkola - Data Engineer\Project\Project 3\source\users_w_postal_code.csv", sep=",")

engine = create_engine("postgresql://postgres:akbar8@127.0.0.1:5432/postgres")

df.to_sql("users_w_postal_code", engine)