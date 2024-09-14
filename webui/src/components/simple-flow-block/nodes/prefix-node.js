import React, { useEffect, useState } from 'react';
import { Textarea, Badge } from 'react-daisyui'
import LoadingLine from '../../loading-line';
import { usePrefixAndQueryStore } from '../../../store/simple-refiner-store'

function PrefixNode() {
    const { setPrefix } = usePrefixAndQueryStore()
    const [inputValue, setInputValue] = useState(`You are a professional prompt engineer.
Think carefully, you need to refine the following text to make it more formal and professional.
You need to add more details to the text for better generation.
Please directly output the refined text. Do not include any additional information.
Refine the following text:`);

    useEffect(() => {
        setPrefix(inputValue)
    }, [inputValue, setPrefix])


    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="ghost" size='lg'>✨ Prefix</Badge>
                </div>
                <Textarea
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

export default PrefixNode;