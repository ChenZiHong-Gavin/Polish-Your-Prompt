import { Badge, Form, Radio } from "react-daisyui"
import { useCheckedModeStore } from "../../../store/schema-refiner-store"
import { useQueryAndSchemaAndModeStore } from '../../../store/schema-refiner-store'
import { useEffect } from "react"

function ModeNode() {
    const { setMode } = useQueryAndSchemaAndModeStore()
    const { checkedMode, setCheckedMode } = useCheckedModeStore()

    useEffect(() => {
        setMode(checkedMode)
    }, [checkedMode, setMode])

    return (
        <>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1'>
                <div className='mb-1'>
                    <Badge color="success" size='lg'>🍕 Mode</Badge>
                    <Form>
                        <Form.Label title="One Step">
                            <Radio name="mode" className="checked:bg-blue-500" checked={checkedMode === "ONE_STEP"}
                                onChange={() => setCheckedMode("ONE_STEP")} />
                        </Form.Label>
                        <Form.Label title="Step by Step">
                            <Radio name="mode" className="checked:bg-blue-500" checked={checkedMode === "STEP_BY_STEP"}
                                onChange={() => setCheckedMode("STEP_BY_STEP")} />
                        </Form.Label>
                    </Form>

                </div>
            </div>
        </>
    )
}

export default ModeNode
