import React, { useEffect, useState } from 'react';
import { Badge, Input } from 'react-daisyui'
import { useQueryAndContentAndAnnotations } from '../../../store/annotated-refiner-store'
import JsonView from 'react18-json-view'
import 'react18-json-view/src/style.css'

function AnnotationNode() {
    const { setAnnotations } = useQueryAndContentAndAnnotations()
    const [inputValue, setInputValue] = useState({
        "math": "not math, but english",
    })

    useEffect(() => {
        setAnnotations(inputValue)
    }, [inputValue, setAnnotations])


    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="error" size='lg'>🐉 Annotations</Badge>
                </div>
                <JsonView src={inputValue} editable={true} className='ml-10 mr-10'
                onChange={
                    (e) => {
                        setInputValue(e.src)
                    }
                } />
            </div>
        </>
    );
}

export default AnnotationNode;