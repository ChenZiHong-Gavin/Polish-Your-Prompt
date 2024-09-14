import QueryNode from "./nodes/query-node";
import ContentNode from "./nodes/content-node";
import AnnotationNode from "./nodes/annotation-node";
import PromptNode from "./nodes/prompt-node";
import { useGenerateStore } from "../../store/annotated-refiner-store";
import LoadingLine from "../loading-line";

function AnnotatedFlow() {
    const { status } = useGenerateStore()
    return (
        <div className='w-full mt-5'>
            <QueryNode />
            <ContentNode />
            <AnnotationNode />
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

export default AnnotatedFlow;
