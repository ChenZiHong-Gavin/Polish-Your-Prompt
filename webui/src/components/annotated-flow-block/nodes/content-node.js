import React, { useEffect, useState } from 'react';
import { Badge, Textarea } from 'react-daisyui'
import { useQueryAndContentAndAnnotations } from '../../../store/annotated-refiner-store'
import LoadingLine from '../../loading-line';

function ContentNode() {
    const { setContent } = useQueryAndContentAndAnnotations()
    const [inputValue, setInputValue] = useState('You are a student who needs help with homework. You are struggling with a math problem and need assistance.')

    useEffect(() => {
        setContent(inputValue)
    }, [inputValue, setContent])

    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="warning" size='lg'>🌌 Original Result</Badge>
                </div>
                <Textarea
                    className='mb-2'
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    autoFocus
                    rows={6}
                    style={{ resize: 'none', width: '80%' }}
                />
            </div>
            <LoadingLine />
        </>
    );
}

export default ContentNode;