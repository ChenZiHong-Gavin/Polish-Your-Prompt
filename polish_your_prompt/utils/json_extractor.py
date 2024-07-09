import json


def extract_json_from_text(text):
    json_start = text.find("```json")
    json_end = text.find("```", json_start + 1)
    if json_start != -1 and json_end != -1:
        json_text = text[json_start + 7 : json_end].strip()
    else:
        json_start = text.find("{")
        json_end = text.rfind("}") + 1
        json_text = text[json_start:json_end].strip()

    json_text = json_text.replace("\n", "")
    if json_text[-2] == ",":
        json_text = json_text[:-2] + json_text[-1]

    try:
        return json.loads(json_text)
    except Exception as e:
        return {"error": str(e)}
