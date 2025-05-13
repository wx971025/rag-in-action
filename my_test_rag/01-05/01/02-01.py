from llama_index.readers.database import DatabaseReader

reader = DatabaseReader(
    scheme="mysql",
    host="localhost",
    port=3306, 
    user="wangxu",
    password="wangxu1025",
    dbname="example_db",
)
query = "SELECT * FROM game_scenes"
documents = reader.load_data(query=query)

print(f"从数据库加载的文档数量: {len(documents)}")
for doc in documents[0]:
    print(doc)
 