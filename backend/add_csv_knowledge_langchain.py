import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

input_datapath = "../home_depot_data_2021.csv"
df = pd.read_csv(input_datapath)
print(df.shape)
print(df.columns.tolist())


engine = create_engine("sqlite:///instalily.db")
df.to_sql("instalily", engine, index=False)


db = SQLDatabase(engine=engine)
print(db.dialect)
print(db.get_usable_table_names())