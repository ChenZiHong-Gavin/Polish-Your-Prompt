import SimpleFlow from '../../components/simple-flow-block/simple-flow-block'
import { Button } from 'react-daisyui'
import { useGenerateStore, usePrefixAndQueryStore } from '../../store/simple-refiner-store'
import axiosInstance from '../../api/axios-instance'

const SimpleRefiner = () => {
    const { setStatus, setGenerated } = useGenerateStore()
    const { prefix, query } = usePrefixAndQueryStore()

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
                console.log(error)
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
            </div>
        </>
    )
}

export default SimpleRefiner