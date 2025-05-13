from langchain_community.document_loaders import CSVLoader

file_path = "data/黑神话/黑神话悟空.csv"
loader = CSVLoader(
    file_path=file_path,
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        # "fieldnames": ["种类", "名称", "说明", "等级"],
    }
)
data = loader.load()


for record in data[:2]:
    print(record.metadata)
    print(record.page_content, end="\n\n")

# from langchain_community.document_loaders import UnstructuredCSVLoader
# loader = UnstructuredCSVLoader(file_path=file_path)
# data = loader.load()
# print("示例 4: 使用 UnstructuredCSVLoader 加载文件")
# print(data)
# print("-" * 80)


