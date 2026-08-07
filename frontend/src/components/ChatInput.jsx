import { useState } from "react";
import { Send } from "lucide-react";


function ChatInput({ onSend, disabled }) {

    const [question, setQuestion] = useState("");


    function handleSubmit(event) {

        event.preventDefault();


        const trimmed = question.trim();


        if (!trimmed || disabled) {
            return;
        }


        onSend(trimmed);

        setQuestion("");
    }


    return (
        <form
            className="chat-input"
            onSubmit={handleSubmit}
        >

            <input
                type="text"
                placeholder="Ask CodePilot about your repository..."
                value={question}
                onChange={(event) =>
                    setQuestion(event.target.value)
                }
                disabled={disabled}
            />


            <button
                type="submit"
                disabled={
                    disabled ||
                    !question.trim()
                }
            >

                <Send size={18} />

            </button>

        </form>
    );
}


export default ChatInput;