import QueryNode from "./nodes/query-node";
import SchemaNode from "./nodes/schema-node";
import ModeNode from "./nodes/mode-node";
import PromptNode from "./nodes/prompt-node";
import LoadingLine from "../loading-line";
import { useGenerateStore } from "../../store/schema-refiner-store";

function SchemaFlow() {
    const { status } = useGenerateStore();
    return (
        <div className='w-full mt-5'>
            <QueryNode />
            <SchemaNode />
            <ModeNode />
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

export default SchemaFlow;
