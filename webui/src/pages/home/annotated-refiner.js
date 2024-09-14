import AnnotatedFlow from '../../components/annotated-flow-block/annotated-flow-block'
import { Button } from 'react-daisyui'
import { useGenerateStore, useQueryAndContentAndAnnotations } from '../../store/annotated-refiner-store'
import axiosInstance from '../../api/axios-instance'

const AnnotatedRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { query, content, annotations } = useQueryAndContentAndAnnotations()

    const refine = () => {
        setStatus('refining')
        console.log(query, content, annotations)
        axiosInstance.post('/refine/annotated', {
            prompt: query,
            content: content,
            annotations: annotations
        })
            .then((response) => {
                console.log(response)
                setStatus('generated')
                setGenerated(response.refined_prompt)
            })
            .catch((error) => {
                console.log(error)
            })
    }

    return (
        <>
            <div className="w-1/3 m-5 h-auto">
                <p className="text-2xl text-center"><b>Simple Refiner</b></p>
                <AnnotatedFlow />
                <div className="text-center">
                    <Button
                        onClick={refine}
                        color='info' className='m-5'>Refine</Button>
                    <Button
                        onClick={() => setStatus('idle')}
                        color='neutral' className='m-5'>Clear</Button>
                </div>
            </div>
        </>
    )
}

export default AnnotatedRefiner