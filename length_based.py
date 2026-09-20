from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

# Create recursive text splitter
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

# Split documents into chunks
result = splitter.split_documents(docs)

# Print second chunk
print(result[1].page_content)