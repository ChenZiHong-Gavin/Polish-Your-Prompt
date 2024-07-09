import SideBar from "../../components/side-bar"
import Flow from "../../components/flow";
import ChatArea from "../../components/chat-area";
import { useEffect, useState } from "react";


const Home = () => {
    const [theme, setTheme] = useState('emerald');

    useEffect(() => {
        document.getElementsByTagName('html')[0].setAttribute('data-theme', theme);
        window.localStorage.setItem('sb-react-daisyui-preview-theme', theme);
    }, [theme])

    return (
        <div className="flex flex-row">
            <SideBar />
            <Flow />
            <ChatArea />
        </div>
    )
}

export default Home