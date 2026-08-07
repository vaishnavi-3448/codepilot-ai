import { useEffect, useState } from "react";
import { FileCode2, X } from "lucide-react";

import { getRepositoryFile } from "../services/api";


function FileViewer({
    filePath,
    onClose
}) {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);


    useEffect(() => {

        if (!filePath) {
            return;
        }

        async function loadFile() {

            setLoading(true);
            setError(null);

            try {

                const result =
                    await getRepositoryFile(filePath);

                setFile(result);

            } catch (err) {

                setError(err.message);

            } finally {

                setLoading(false);

            }
        }

        loadFile();

    }, [filePath]);


    if (!filePath) {
        return (
            <div className="file-viewer empty-viewer">

                <FileCode2 size={38} />

                <h2>
                    Select a file
                </h2>

                <p>
                    Click a file from the repository
                    explorer to view its contents.
                </p>

            </div>
        );
    }


    return (
        <div className="file-viewer">

            <div className="file-viewer-header">

                <div className="file-title">

                    <FileCode2 size={17} />

                    <span>
                        {filePath}
                    </span>

                </div>


                <button
                    onClick={onClose}
                    className="close-file"
                >

                    <X size={17} />

                </button>

            </div>


            <div className="file-content">

                {loading && (
                    <div className="viewer-status">
                        Loading file...
                    </div>
                )}


                {error && (
                    <div className="viewer-error">
                        {error}
                    </div>
                )}


                {file && !loading && (

                    <pre>
                        <code>
                            {file.content}
                        </code>
                    </pre>

                )}

            </div>

        </div>
    );
}


export default FileViewer;