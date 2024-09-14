import githubMark from '../assets/github-mark.png';
import { Modal, Button, Input } from 'react-daisyui';
import { useState, useEffect, useRef, useCallback } from 'react';

const Settings = () => {
    const ref = useRef(null);

    const [apiBase, setApiBase] = useState('');
    const [apiKey, setApiKey] = useState('');

    useEffect(() => {
        const storedApiBase = localStorage.getItem('apiBase');
        const storedApiKey = localStorage.getItem('apiKey');
        if (storedApiBase) setApiBase(storedApiBase);
        if (storedApiKey) setApiKey(storedApiKey);
    }, []);

    const handleShow = useCallback(() => {
        ref.current?.showModal();
    }, [ref]);

    const handleSubmit = (e) => {
        e.preventDefault();
        localStorage.setItem('apiBase', apiBase);
        localStorage.setItem('apiKey', apiKey);
        console.log(apiBase, apiKey);
        ref.current?.close();
    };

    return (
        <>
            <div className="fixed top-5 left-5 w-400 text-center">
                <div>
                    <button className="btn btn-circle btn-lg btn-ghost" onClick={handleShow}>⚙️</button>
                </div>
                <div>
                    <button className='btn btn-circle btn-lg btn-ghost'
                        onClick={() => window.open('https://github.com/ChenZiHong-Gavin/Polish-Your-Prompt')}>
                        <img src={githubMark} alt="Github" className="w-5 h-5" />
                    </button>
                </div>
            </div>
            <Modal ref={ref}>
                <Modal.Header className="font-bold">Fill in your API base and API key.</Modal.Header>
                <Modal.Body>
                    <div className='p-2'>
                        <form method="dialog">
                            <Input label="API base" placeholder="API base" className='w-full'
                                value={apiBase}
                                onChange={(e) => setApiBase(e.target.value)}
                            />
                        </form>

                    </div>
                    <div className='p-2'>
                        <Input label="API key" placeholder="API key" className='w-full' type='password'
                            value={apiKey}
                            onChange={(e) => setApiKey(e.target.value)}
                        />
                    </div>
                </Modal.Body>
                <Modal.Actions>
                    <form method="dialog">
                        <Button type="primary" className='mr-2' onClick={handleSubmit}>Save</Button>
                        <Button onClick={handleShow}>Close</Button>
                    </form>
                </Modal.Actions>
            </Modal>
        </>
    );
}


export default Settings;
