import AnnotatedFlow from '../../components/annotated-flow-block/annotated-flow-block'
import { Button, Toast, Alert } from 'react-daisyui'
import { useGenerateStore, useQueryAndContentAndAnnotations } from '../../store/annotated-refiner-store'
import axiosInstance from '../../api/axios-instance'
import { handleAddToast, handleRemoveToast } from '../../utils/alert'
import { useState } from 'react'

const AnnotatedRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { query, content, annotations } = useQueryAndContentAndAnnotations()

    const [alerts, setAlerts] = useState([])

    const refine = () => {
        setStatus('refining')
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
                setStatus('idle')
                handleAddToast(alerts, setAlerts)
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
                <Toast>
                    {alerts.map((alert, index) => <Alert key={index} status={alert.status}>
                        <div className="w-full flex-row justify-between gap-2">
                            <h3>{alert.text}</h3>
                        </div>
                        <Button color="ghost" onClick={() => handleRemoveToast(alerts, setAlerts, index)}>
                            X
                        </Button>
                    </Alert>)}
                </Toast>
            </div>
        </>
    )
}

export default AnnotatedRefiner