import pandas as pd
from pymongo import MongoClient
excel_path='Excel/Uni_List.xlsx'
df=pd.read_excel(excel_path)
client=MongoClient('localhost', 27017)
db = client['LI_UK']
collection = db['University_Collection']
data_dict = df.to_dict("records")
collection.insert_many(data_dict)
print("Data has been inserted into MongoDB")