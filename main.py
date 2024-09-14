import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from polish_your_prompt.core.refiner import SimpleRefiner, SchemaRefiner, AnnotatedRefiner, MODE
from polish_your_prompt.schemas import *
from polish_your_prompt.llm import OpenAIChat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class SimpleRefineRequest(BaseModel):
    prompt: str
    prefix: str

class SchemaRefineRequest(BaseModel):
    prompt: str
    schema: str
    mode: str

class AnnotatedRefineRequest(BaseModel):
    prompt: str
    content: str
    annotations: dict


@app.post("/refine/simple")
def refine_simple(info: SimpleRefineRequest, request: Request):
    try:
        simple_refiner = SimpleRefiner(llm_client=OpenAIChat(
            api_base=request.headers['x-api-base'],
            api_key=request.headers['x-api-key']
        ))
        refined_prompt = simple_refiner.refine(info.prompt, prefix=info.prefix)
        return {"refined_prompt": refined_prompt}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/refine/schema")
def refine_schema(info: SchemaRefineRequest, request: Request):
    try:
        schema_refiner = SchemaRefiner(llm_client=OpenAIChat(
            api_base=request.headers['x-api-base'],
            api_key=request.headers['x-api-key']
        ))
        schema = eval(info.schema)
        mode = info.mode
        if mode not in ["ONE_STEP", "STEP_BY_STEP"]:
            raise Exception("Invalid mode")
        else:
            structure, prompt = schema_refiner.refine(info.prompt, schema=schema(), mode=MODE.ONE_STEP if mode == "ONE_STEP" else MODE.STEP_BY_STEP)
        return {"structure": structure, "prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/refine/annotated")
def refine_annotated(info: AnnotatedRefineRequest, request: Request):
    try:
        annotated_refiner = AnnotatedRefiner(llm_client=OpenAIChat(
            api_base=request.headers['x-api-base'],
            api_key=request.headers['x-api-key']
        ))
        refined_prompt = annotated_refiner.refine(info.prompt, info.content, info.annotations)
        return {"refined_prompt": refined_prompt}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/schemas")
def get_schemas():
    schemas = [
        {
            "schema_name": schema.schema_name,
            "schema_description": schema.description,
            "components": schema.components
        } for schema in SCHEMAS
    ]
    return {"schemas": schemas}

@app.get("/")
def welcome():
    return {"Polish Your Prompt": "Welcome!"}


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)