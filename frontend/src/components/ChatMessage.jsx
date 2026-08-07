import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { Copy, Check } from "lucide-react";


function CodeBlock({ language, children }) {

    const [copied, setCopied] = useState(false);

    const code = String(children).replace(/\n$/, "");


    async function copyCode() {

        await navigator.clipboard.writeText(code);

        setCopied(true);

        setTimeout(() => {
            setCopied(false);
        }, 1500);
    }


    return (
        <div className="code-block">

            <div className="code-header">

                <span>
                    {language || "code"}
                </span>

                <button onClick={copyCode}>

                    {copied
                        ? <Check size={14} />
                        : <Copy size={14} />
                    }

                    {copied
                        ? "Copied"
                        : "Copy"
                    }

                </button>

            </div>


            <SyntaxHighlighter
                language={language || "text"}
                PreTag="div"
                customStyle={{
                    margin: 0,
                    padding: "16px",
                    background: "#0b0d10",
                    fontSize: "13px",
                    lineHeight: "1.6"
                }}
            >
                {code}
            </SyntaxHighlighter>

        </div>
    );
}


function ChatMessage({ message }) {

    const isUser =
        message.role === "user";


    return (

        <div
            className={`message-row ${
                isUser
                    ? "user-message"
                    : "assistant-message"
            }`}
        >

            <div className="message-avatar">

                {isUser ? "You" : "AI"}

            </div>


            <div className="message-content">

                <div className="message-role">

                    {isUser
                        ? "You"
                        : "CodePilot"}

                </div>


                <div className="message-text">

                    {isUser ? (

                        <div>
                            {message.content}
                        </div>

                    ) : (

                        <ReactMarkdown
                            components={{
                                code({
                                    inline,
                                    className,
                                    children,
                                    ...props
                                }) {

                                    const match =
                                        /language-(\w+)/.exec(
                                            className || ""
                                        );


                                    if (!inline) {

                                        return (
                                            <CodeBlock
                                                language={
                                                    match
                                                        ? match[1]
                                                        : "text"
                                                }
                                            >
                                                {children}
                                            </CodeBlock>
                                        );

                                    }


                                    return (
                                        <code
                                            className="inline-code"
                                            {...props}
                                        >
                                            {children}
                                        </code>
                                    );
                                }
                            }}
                        >
                            {message.content}
                        </ReactMarkdown>

                    )}

                </div>


                {message.sources &&
                    message.sources.length > 0 && (

                    <div className="sources">

                        <div className="sources-title">
                            Retrieved Sources
                        </div>


                        {message.sources.map(
                            (source, index) => (

                            <div
                                className="source"
                                key={index}
                            >

                                <div>
                                    📄{" "}

                                    {source.metadata?.file_path ||
                                        `Source ${index + 1}`}

                                </div>

                            </div>

                        ))}

                    </div>

                )}

            </div>

        </div>
    );
}


export default ChatMessage;