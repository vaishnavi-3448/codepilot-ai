import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";


function ChatWindow({
    messages,
    onSend,
    loading
}) {

    return (
        <main className="chat-window">

            <div className="chat-header">

                <div>

                    <h2>
                        CodePilot Assistant
                    </h2>

                    <p>
                        Ask questions about your codebase
                    </p>

                </div>

            </div>


            <div className="messages">

                {messages.length === 0 && (

                    <div className="empty-state">

                        <div className="empty-icon">
                            ⚡
                        </div>

                        <h2>
                            How can I help?
                        </h2>

                        <p>
                            Ask me to explain code,
                            find files, or understand
                            your repository.
                        </p>


                        <div className="suggestions">

                            <button
                                onClick={() =>
                                    onSend(
                                        "Where is the FastAPI application created?"
                                    )
                                }
                            >
                                Where is the FastAPI app?
                            </button>


                            <button
                                onClick={() =>
                                    onSend(
                                        "Explain the repository architecture"
                                    )
                                }
                            >
                                Explain the architecture
                            </button>


                            <button
                                onClick={() =>
                                    onSend(
                                        "What does ChromaDB do?"
                                    )
                                }
                            >
                                What does ChromaDB do?
                            </button>

                        </div>

                    </div>
                )}


                {messages.map(
                    (message, index) => (

                    <ChatMessage
                        key={index}
                        message={message}
                    />

                ))}


                {loading && (

                    <div className="typing">
                        CodePilot is thinking...
                    </div>

                )}

            </div>


            <ChatInput
                onSend={onSend}
                disabled={loading}
            />

        </main>
    );
}


export default ChatWindow;