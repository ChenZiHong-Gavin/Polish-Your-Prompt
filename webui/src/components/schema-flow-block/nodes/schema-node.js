import { Badge, Form, Timeline, Radio } from "react-daisyui";
import LoadingLine from "../../loading-line";
import axiosInstance from "../../../api/axios-instance";
import { useState, useEffect } from "react";
import { useCheckedSchemaStore } from "../../../store/schema-refiner-store";
import { useQueryAndSchemaAndModeStore } from '../../../store/schema-refiner-store'

const Structure = ({ schema }) => {
    const schema_structure = schema.components;
    return (
        <div>
            <h2 className="md-2"><b>{schema.schema_name}</b></h2>
            <div>
                <Timeline snap={true} vertical={true} compact={true}>
                    {
                        Object.keys(schema_structure).map((key, index) => {
                            return (
                                <Timeline.Item connect="end" key={index}>
                                    <Timeline.Start className="md:text-start">
                                        <div className="text-lg font-black">{key}</div>
                                        {schema_structure[key]}
                                    </Timeline.Start>
                                    <Timeline.Middle />
                                </Timeline.Item>
                            );
                        })
                    }
                </Timeline>
            </div>
        </div>

    )
}

function SchemaNode() {
    const { setSchema } = useQueryAndSchemaAndModeStore();
    const [schemas, setSchemas] = useState([]);
    const { checkedSchema, setCheckedSchema } = useCheckedSchemaStore();

    useEffect(() => {
        axiosInstance.get('/schemas')
            .then((response) => {
                setSchemas(response.schemas);
                if (response.schemas.length > 0) {
                    setCheckedSchema(response.schemas[0].schema_name);
                }
            })
            .catch((error) => {
                console.error(error);
            });
    }, [setCheckedSchema]);

    useEffect(() => {
        setSchema(checkedSchema);
    }, [checkedSchema, setSchema]);

    const handleSchemaChange = (schema_name) => {
        setCheckedSchema(schema_name);
    }


    return (
        <div>
            <div className='text-center text-lg border-dashed border-2 border-solid border-gray-250 p-1 h-auto'>
                <div className='mb-1'>
                    <Badge color="info" size='lg'>🌈 Schema</Badge>
                </div>
                {
                    schemas.length > 0 && (
                        <div className="bg-base-200 p-4 rounded-lg shadow">
                            <Form>
                                {
                                    schemas.map((schema, index) => {
                                        return (
                                            <Form.Label title={schema.schema_name} key={index} className="mb-1">
                                                <Radio name="schema" className="checked:bg-blue-500" checked={checkedSchema === schema.schema_name}
                                                    onChange={() => handleSchemaChange(schema.schema_name)} />
                                            </Form.Label>
                                        );
                                    })
                                }
                            </Form>
                            <Structure schema={schemas.find(schema => schema.schema_name === checkedSchema)} />
                        </div>
                    )
                }
            </div>
            <LoadingLine />
        </div >
    );
}

export default SchemaNode;
