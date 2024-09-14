import PrefixNode from "./nodes/prefix-node";
import QueryNode from "./nodes/query-node";
import PromptNode from "./nodes/prompt-node";
import LoadingLine from "../loading-line";
import { useGenerateStore } from '../../store/simple-refiner-store'

function SimpleFlow() {
    const { status } = useGenerateStore()
    return (
        <div className='w-full mt-5'>
            <PrefixNode />
            <QueryNode />
            {
                status !== 'idle' && (
                    <>
                        <LoadingLine />
                        <PromptNode />
                    </>
                )
            }
        </div>
    );
}

export default SimpleFlow;
