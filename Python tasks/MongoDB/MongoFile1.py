import pymongo
client = pymongo.MongoClient('mongodb+srv://DevanDuraiPragash:Devan1401@cluster0.weyhdl2.mongodb.net/?retryWrites=true&w=majority')
DB1=client['Demo1']
col1=DB1['democol']
doc1={
    'Name':'Dave',
    'Age ':'16',
    'Grade':'XI'
    }
col1.insert_one(doc1)
print(client.list_database_names())
