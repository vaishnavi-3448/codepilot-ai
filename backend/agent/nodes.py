from agent.state import AgentState
from services.repository_indexer import RepositoryIndexer
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY
from services.retriever import CodeRetriever


# Initialize repository RAG
repository_indexer = RepositoryIndexer("../")

retriever = CodeRetriever(
    repository_indexer
)


# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=GEMINI_API_KEY
)


def code_search_agent(
    state: AgentState
):

    question = state["question"]
    
    results = retriever.search(
            question,
            k=5
        )
    

    if not results:

        return {
            "answer": "I could not find relevant code.",
            "sources": []
        }

    context_parts = []

    sources = []

    for result in results:

        file_path = result.metadata.get(
            "file_path",
            "unknown"
        )

        language = result.metadata.get(
            "language",
            "unknown"
        )

        content = result.page_content

        context_parts.append(
            f"""
FILE: {file_path}
LANGUAGE: {language}

CODE:
{content}
"""
        )

        sources.append({
            "file_path": file_path,
            "language": language,
            "content": content
        })

    context = "\n\n".join(
        context_parts
    )

    prompt = f"""
You are CodePilot AI's code search agent.

Answer the user's question using ONLY the
repository code provided below.

Explain where the relevant code is located.

Always mention the relevant file path.

Do not invent files, functions, or code.

REPOSITORY CODE:

{context}

USER QUESTION:

{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):

        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
            and item.get("text")
        )

    return {
        "answer": answer,
        "sources": sources
    }


def code_explanation_agent(
    state: AgentState
):

    question = state["question"]

    # Make sure repository has been indexed
   

    # Retrieve relevant code
    results = retriever.search(
     question,
    k=5
)
    

    if not results:

        return {
            "answer": "I could not find relevant code to explain.",
            "sources": []
        }

    context_parts = []

    sources = []

    for result in results:

        file_path = result.metadata.get(
            "file_path",
            "unknown"
        )

        language = result.metadata.get(
            "language",
            "unknown"
        )

        content = result.page_content

        context_parts.append(
            f"""
FILE: {file_path}
LANGUAGE: {language}

CODE:
{content}
"""
        )

        sources.append({
            "file_path": file_path,
            "language": language,
            "content": content
        })

    context = "\n\n".join(
        context_parts
    )

    prompt = f"""
You are CodePilot AI's code explanation agent.

Your job is to explain code from the user's
repository clearly and accurately.

Use ONLY the repository code provided below.

For the user's question:

1. Identify the relevant file.
2. Explain what the code does.
3. Explain important classes, functions, or
   components involved.
4. Explain how the relevant pieces interact.
5. Mention important dependencies when visible.
6. Mention the file path.
7. Do not invent functionality that isn't present.

Keep the explanation technically accurate and
easy for a developer to understand.

REPOSITORY CODE:

{context}

USER QUESTION:

{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):

        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
            and item.get("text")
        )

    return {
        "answer": answer,
        "sources": sources
    }


def bug_detection_agent(
    state: AgentState
):

    question = state["question"]

    # Make sure repository has been indexed
    repository_rag.index()

    # Retrieve code relevant to the user's question
    results = (
        repository_rag.vector_store.similarity_search(
            question,
            k=7
        )
    )

    if not results:

        return {
            "answer": "I could not find relevant code to analyze.",
            "sources": []
        }

    context_parts = []
    sources = []

    for result in results:

        file_path = result.metadata.get(
            "file_path",
            "unknown"
        )

        language = result.metadata.get(
            "language",
            "unknown"
        )

        content = result.page_content

        context_parts.append(
            f"""
FILE: {file_path}
LANGUAGE: {language}

CODE:
{content}
"""
        )

        sources.append({
            "file_path": file_path,
            "language": language,
            "content": content
        })

    context = "\n\n".join(
        context_parts
    )

    prompt = f"""
You are CodePilot AI's bug detection agent.

Analyze the provided repository code for genuine
bugs, logical errors, security problems, incorrect
assumptions, and potentially dangerous behavior.

IMPORTANT:

- Use ONLY the provided repository code.
- Do not invent files or functionality.
- Do not report something as a bug merely because
  it is a stylistic preference.
- If there are no obvious bugs, say so.
- Distinguish confirmed issues from potential issues.

For every issue you identify, provide:

1. File
2. Severity
3. Problem
4. Why it is a problem
5. Evidence from the code
6. Suggested fix

Use these severity levels:

CRITICAL
HIGH
MEDIUM
LOW

At the end, provide a short summary of the
most important findings.

REPOSITORY CODE:

{context}

USER REQUEST:

{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):

        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
            and item.get("text")
        )

    return {
        "answer": answer,
        "sources": sources
    }


def general_agent(
    state: AgentState
):

    return {
        "answer": "General agent selected."
    }