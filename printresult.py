import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_collection("pdf_vectors")

results = collection.get()
print(results)