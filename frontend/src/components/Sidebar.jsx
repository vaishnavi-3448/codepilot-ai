import { useEffect, useState } from "react";

import {
    Folder,
    FolderOpen,
    FileCode2,
    RefreshCw,
    Trash2,
    ChevronRight,
    ChevronDown
} from "lucide-react";

import {
    getRepositoryTree
} from "../services/api";


function TreeItem({ item,level = 0,onFileClick }) {

    const [expanded, setExpanded] = useState(
        level < 1
    );


    if (item.type === "file") {

    return (
        <div
            className="tree-item file-item"
            style={{
                paddingLeft:
                    `${14 + level * 16}px`
            }}
            onClick={() =>
                onFileClick(item.path)
            }
        >

            <FileCode2 size={15} />

            <span>
                {item.name}
            </span>

        </div>
    );
}


    return (
        <div>

            <div
                className="tree-item folder-item"
                style={{
                    paddingLeft:
                        `${8 + level * 16}px`
                }}
                onClick={() =>
                    setExpanded(!expanded)
                }
            >

                {expanded ? (
                    <ChevronDown size={14} />
                ) : (
                    <ChevronRight size={14} />
                )}


                {expanded ? (
                    <FolderOpen size={15} />
                ) : (
                    <Folder size={15} />
                )}


                <span>
                    {item.name}
                </span>

            </div>


            {expanded &&
                item.children?.map(
                    (child, index) => (

                    <TreeItem
                key={`${child.name}-${index}`}
    item={child}
    level={level + 1}
    onFileClick={onFileClick}
/>

                ))}

        </div>
    );
}


function Sidebar({
    onIndex,
    onClearMemory,
    indexing,
    onFileClick
}) {

    const [tree, setTree] = useState([]);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState(null);


    async function loadTree() {

        setLoading(true);
        setError(null);

        try {

            const result =
                await getRepositoryTree();

            setTree(result.tree || []);

        } catch (err) {

            setError(err.message);

        } finally {

            setLoading(false);

        }
    }


    useEffect(() => {

        loadTree();

    }, []);


    async function handleIndex() {

        await onIndex();

        await loadTree();
    }


    return (

        <aside className="sidebar">

            <div className="sidebar-section">

                <div className="sidebar-title">

                    <Folder size={17} />

                    <span>
                        Repository
                    </span>

                </div>


                <div className="repository-tree">

                    {loading && (

                        <div className="tree-status">
                            Loading repository...
                        </div>

                    )}


                    {error && (

                        <div className="tree-error">
                            {error}
                        </div>

                    )}


                    {!loading &&
                        !error &&
                        tree.length === 0 && (

                        <div className="tree-status">
                            No files found.
                        </div>

                    )}


                    {!loading &&
                        !error &&
                        tree.map(
                            (item, index) => (

                            <TreeItem
                                key={`${item.name}-${index}`}
                                item={item}
                                onFileClick={onFileClick}
                            />

                        ))}

                </div>

            </div>


            <div className="sidebar-actions">

                <button
                    onClick={handleIndex}
                    disabled={indexing}
                >

                    <RefreshCw size={16} />

                    {indexing
                        ? "Indexing..."
                        : "Index Repository"}

                </button>


                <button
                    className="secondary"
                    onClick={onClearMemory}
                >

                    <Trash2 size={16} />

                    Clear Chat

                </button>

            </div>

        </aside>
    );
}


export default Sidebar;