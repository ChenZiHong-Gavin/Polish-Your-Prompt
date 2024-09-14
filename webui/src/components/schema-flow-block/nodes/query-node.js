import React, { useEffect, useState } from 'react';
import { Badge, Input } from 'react-daisyui'
import { useQueryAndSchemaAndModeStore } from '../../../store/schema-refiner-store'
import LoadingLine from '../../loading-line';

function QueryNode() {
    const { setQuery } = useQueryAndSchemaAndModeStore()
    const [inputValue, setInputValue] = useState('Help me do my homework.');

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
            <LoadingLine />
        </>
    );
}

export default QueryNode;