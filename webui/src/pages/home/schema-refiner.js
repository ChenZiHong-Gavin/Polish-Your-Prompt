import SchemaFlow from '../../components/schema-flow-block/schema-flow-block'
import { Button } from 'react-daisyui'
import { useGenerateStore, useQueryAndSchemaAndModeStore } from '../../store/schema-refiner-store'
import axiosInstance from '../../api/axios-instance'

const SchemaRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { query, schema, mode } = useQueryAndSchemaAndModeStore()

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
            </div>
        </>
    )
}

export default SchemaRefiner