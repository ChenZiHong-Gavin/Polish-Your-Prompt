from fastapi import APIRouter

text_to_structure_router = APIRouter()


@text_to_structure_router.post("/structure")
async def text_to_structure(query, schema):
    # 按照schema重写prompt
    # 生成structured prompt: 自定义的数据结构，用图表示 {"vertices": [], "edges": []}
    print(query)
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    text_to_structure({"query": "How many people live in Singapore?"}, {"schema": "CO-STAR"})