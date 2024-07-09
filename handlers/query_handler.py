from fastapi import APIRouter

query_router = APIRouter()


@query_router.post("/structure")
async def query_to_structure(query, schema):
    # 根据schema生成structure: 自定义的数据结构，用图表示 {"vertices": [], "edges": []}
    print(query)
    # TODO
    # schema中有vertice的定义
    return {"vertices": [], "edges": []}


@query_router.post("/prompt")
async def structure_to_prompt(structure, schema):
    # 根据schema生成prompt
    print(structure)
    # TODO
    return "prompt"
