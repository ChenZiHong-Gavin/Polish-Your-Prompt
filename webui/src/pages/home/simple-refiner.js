import SimpleFlow from '../../components/simple-flow-block/simple-flow-block'
import { Button, Toast, Alert } from 'react-daisyui'
import { useGenerateStore, usePrefixAndQueryStore } from '../../store/simple-refiner-store'
import axiosInstance from '../../api/axios-instance'
import { useState } from 'react'
import { handleAddToast, handleRemoveToast } from '../../utils/alert'

const SimpleRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { prefix, query } = usePrefixAndQueryStore()

    const [alerts, setAlerts] = useState([])

    const refine = () => {
        setStatus('refining')
        axiosInstance.post('/refine/simple', {
            prompt: query,
            prefix: prefix
        })
            .then((response) => {
                setStatus('generated')
                setGenerated(response.refined_prompt)
            })
            .catch((error) => {
                setStatus('idle')
                console.log(error)
                handleAddToast(alerts, setAlerts)
            })
    }

    return (
        <>
            <div className="w-1/3 m-5 h-auto">
                <p className="text-2xl text-center"><b>Simple Refiner</b></p>
                <SimpleFlow />
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

export default SimpleRefiner