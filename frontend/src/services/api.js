const API_BASE_URL = "http://127.0.0.1:8000";


export async function checkHealth() {

    const response = await fetch(
        `${API_BASE_URL}/health`
    );

    if (!response.ok) {
        throw new Error("Backend unavailable");
    }

    return response.json();
}


export async function sendMessage(question) {

    const response = await fetch(
        `${API_BASE_URL}/chat`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        }
    );

    if (!response.ok) {

        const error = await response.text();

        throw new Error(error);
    }

    return response.json();
}


export async function indexRepository() {

    const response = await fetch(
        `${API_BASE_URL}/index`,
        {
            method: "POST"
        }
    );

    if (!response.ok) {
        throw new Error("Repository indexing failed");
    }

    return response.json();
}


export async function clearMemory() {

    const response = await fetch(
        `${API_BASE_URL}/chat/memory`,
        {
            method: "DELETE"
        }
    );

    if (!response.ok) {
        throw new Error("Could not clear memory");
    }

    return response.json();
}
export async function getRepositoryTree() {

    const response = await fetch(
        `${API_BASE_URL}/repository/tree`
    );

    if (!response.ok) {
        throw new Error(
            "Could not load repository tree"
        );
    }

    return response.json();
}
export async function getRepositoryFile(path) {

    const response = await fetch(
        `${API_BASE_URL}/repository/file?path=${encodeURIComponent(path)}`
    );

    if (!response.ok) {

        const error = await response.text();

        throw new Error(error);
    }

    return response.json();
}