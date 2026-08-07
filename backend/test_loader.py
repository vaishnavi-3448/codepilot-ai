from services.document_loader import DocumentLoader

loader = DocumentLoader()

text = loader.load("uploads/sample.txt")

print(text)