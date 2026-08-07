import { useState } from "react";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import FileViewer from "./components/FileViewer";
import {
    sendMessage,
    indexRepository,
    clearMemory
} from "./services/api";


function App() {

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const [indexing, setIndexing] = useState(false);
    const [selectedFile, setSelectedFile] =
    useState(null);

    async function handleSend(question) {

        setMessages((previous) => [

            ...previous,

            {
                role: "user",
                content: question
            }

        ]);


        setLoading(true);


        try {

            const result =
                await sendMessage(question);


            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content:
                        result.answer ||
                        "No answer returned.",
                    sources:
                        result.sources || []
                }

            ]);

        } catch (error) {

            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content:
                        "⚠️ " + error.message
                }

            ]);

        } finally {

            setLoading(false);

        }
    }


    async function handleIndex() {

        setIndexing(true);


        try {

            const result =
                await indexRepository();


            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content:
                        `Repository indexed successfully. ` +
                        `${result.files} files and ` +
                        `${result.chunks} chunks processed.`
                }

            ]);

        } catch (error) {

            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content:
                        "⚠️ Indexing failed: " +
                        error.message
                }

            ]);

        } finally {

            setIndexing(false);

        }
    }


    async function handleClearMemory() {

        try {

            await clearMemory();

            setMessages([]);

        } catch (error) {

            console.error(error);

        }
    }


    return (

        <div className="app">

            <Header />


            <div className="workspace">

                <Sidebar
                    onIndex={handleIndex}
                    onClearMemory={handleClearMemory}
                    indexing={indexing}
                    onFileClick={setSelectedFile}
                />


                {selectedFile ? (

    <FileViewer
        filePath={selectedFile}
        onClose={() =>
            setSelectedFile(null)
        }
    />

) : (

    <ChatWindow
        messages={messages}
        onSend={handleSend}
        loading={loading}
    />

)}

            </div>

        </div>

    );
}


export default App;