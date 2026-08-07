from services.code_rag import CodeRAG


repository_path = "../"

code_rag = CodeRAG(
    repository_path
)


print("\nIndexing repository...\n")

result = code_rag.index_repository()

print(
    f"Files indexed: {result['files']}"
)

print(
    f"Chunks created: {result['chunks']}"
)


question = "Where is the FastAPI application created?"


result = code_rag.ask(
    question
)


print("\n" + "=" * 70)

print("QUESTION")

print("=" * 70)

print(question)


print("\n" + "=" * 70)

print("ANSWER")

print("=" * 70)

print(result["answer"])


print("\n" + "=" * 70)

print("SOURCES")

print("=" * 70)


for source in result["sources"]:

    print("\nFILE:")
    print(source["file_path"])

    print("\nLANGUAGE:")
    print(source["language"])

    print("\nCODE:")
    print(source["content"])

    print("-" * 60)