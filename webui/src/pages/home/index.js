import { useEffect, useState } from "react";
import SimpleRefiner from "./simple-refiner";
import SchemaRefiner from "./schema-refiner";
import AnnotatedRefiner from "./annotated-refiner";
import Settings from "../../components/settings";


const Head = () => {
    return (
        <div className="flex flex-col items-center">
            <img src="/logo.png" alt="logo" className="w-20 h-20" />
            <h1 className="text-5xl font-bold text-blue-600">Polish Your Prompt</h1>
            <h2 className="text-2xl font-semibold text-gray-500">Make anyone master of prompt engineering!
            </h2>
        </div>
    )
}

const Home = () => {
    const [theme] = useState('emerald');

    useEffect(() => {
        document.getElementsByTagName('html')[0].setAttribute('data-theme', theme);
        window.localStorage.setItem('sb-react-daisyui-preview-theme', theme);
    }, [theme])

    return (
        <>
            <div className="pt-10 h-screen">
                <Head />
                <div className="flex justify-between mt-20 h-auto">
                    <SimpleRefiner />
                    <SchemaRefiner />
                    <AnnotatedRefiner />
                </div>
                <Settings />
            </div>
        </>
    )
}

export default Home