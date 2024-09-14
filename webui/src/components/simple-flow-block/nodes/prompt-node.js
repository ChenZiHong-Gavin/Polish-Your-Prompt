import React from 'react';
import { Textarea, Badge, Loading } from 'react-daisyui'
import { useGenerateStore } from '../../../store/simple-refiner-store'

function PromptNode() {
    const { status, generated, setGenerated } = useGenerateStore()
    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="primary" size='lg'>✨ Generated Prompt</Badge>
                </div>
                <div className='mb-2'>
                    {
                        status === 'refining' && <Loading variant="ring" size="lg" />
                    }
                    {
                        status === 'generated' && <Textarea
                            value={generated}
                            onChange={(e) => setGenerated(e.target.value)}
                            autoFocus
                            rows={6}
                            style={{ resize: 'none', width: '80%' }}
                        />
                    }
                </div>
            </div>
        </>
    );
}

export default PromptNode;