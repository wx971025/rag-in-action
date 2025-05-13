from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    path="/Users/wangxu/github_project/rag-in-action/my_test_rag/data",
    glob="**/*.csv",
    loader_cls=CSVLoader
)

docs = loader.load()
print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])

loader = DirectoryLoader(
    path="/Users/wangxu/github_project/rag-in-action/my_test_rag/data",
)

docs = loader.load()
print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])
