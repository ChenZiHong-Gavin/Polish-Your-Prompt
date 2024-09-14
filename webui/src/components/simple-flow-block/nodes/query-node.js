import React, { useEffect, useState } from 'react';
import { Badge, Input } from 'react-daisyui'
import { usePrefixAndQueryStore } from '../../../store/simple-refiner-store'

function QueryNode() {
    const { setQuery } = usePrefixAndQueryStore()
    const [inputValue, setInputValue] = useState('Write a blog about Python for me.');

    useEffect(() => {
        setQuery(inputValue)
    }, [inputValue, setQuery])

    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="accent" size='lg'>👤 Query</Badge>
                </div>
                <Input
                    className='mb-2'
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    autoFocus
                    style={{ resize: 'none', width: '80%' }}
                />
            </div>
        </>
    );
}

export default QueryNode;