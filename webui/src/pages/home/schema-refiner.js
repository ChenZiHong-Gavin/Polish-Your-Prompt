import SchemaFlow from '../../components/schema-flow-block/schema-flow-block'
import { Button, Toast, Alert } from 'react-daisyui'
import { useGenerateStore, useQueryAndSchemaAndModeStore } from '../../store/schema-refiner-store'
import axiosInstance from '../../api/axios-instance'
import { handleAddToast, handleRemoveToast } from '../../utils/alert'
import { useState } from 'react'

const SchemaRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { query, schema, mode } = useQueryAndSchemaAndModeStore()

    const [alerts, setAlerts] = useState([])

    const refine = () => {
        setStatus('refining')
        axiosInstance.post('/refine/schema', {
            prompt: query,
            schema: schema,
            mode: mode
        })
            .then((response) => {
                console.log(response)
                setGenerated(response.prompt)
                setStatus('generated')
            })
            .catch((error) => {
                console.error(error)
                setStatus('idle')
                handleAddToast(alerts, setAlerts)
            }
            )
    }

    return (
        <>
            <div className="w-1/3 m-5">
                <p className="text-2xl text-center"><b>Schema Refiner</b></p>
                <SchemaFlow />
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
                        <Button color="ghost" onClick={() => handleRemoveToast(index, alerts, setAlerts)}>
                            X
                        </Button>
                    </Alert>)}
                </Toast>
            </div>
        </>
    )
}

export default SchemaRefiner