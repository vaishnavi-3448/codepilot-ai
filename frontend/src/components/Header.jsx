import { useEffect, useState } from "react";
import { Activity, Zap } from "lucide-react";
import { checkHealth } from "../services/api";


function Header() {

    const [connected, setConnected] = useState(false);


    useEffect(() => {

        checkHealth()
            .then(() => setConnected(true))
            .catch(() => setConnected(false));

    }, []);


    return (
        <header className="header">

            <div className="brand">

                <div className="logo">
                    <Zap size={20} />
                </div>

                <div>
                    <h1>CodePilot AI</h1>

                    <span>
                        Multi-Agent Engineering Copilot
                    </span>
                </div>

            </div>


            <div className="connection">

                <Activity size={16} />

                <span>
                    {connected
                        ? "Backend Connected"
                        : "Backend Offline"}
                </span>

            </div>

        </header>
    );
}


export default Header;