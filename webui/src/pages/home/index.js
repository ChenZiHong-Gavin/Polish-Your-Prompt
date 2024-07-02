import SideBar from "../../components/side-bar"
import { useEffect, useState } from "react";


const Home = () => {
    const [theme, setTheme] = useState('emerald');

    useEffect(() => {
        document.getElementsByTagName('html')[0].setAttribute('data-theme', theme);
        window.localStorage.setItem('sb-react-daisyui-preview-theme', theme);
    }, [theme])

    return (
        <>
            <SideBar />
        </>
    )
}

export default Home