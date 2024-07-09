from .template import Template

SCHEMA_REFINER_PREFIX_PROMPT = Template(
    {
        "roles": "You are a professional prompt engineer.",
        "requirements": "You need to complete the prompt according to the given framework.",
        "content": "{schema_description}",
        "examples": "For example\n" "---\n" "{schema_example}\n" "---",
        "outputs": "Please output the refined text in JSON format. Do not include any additional information.\n"
        "Refine the following text: ",
    }
).get_message()

PART_SCHEMA_REFINER_PREFIX_PROMPT = Template(
    {
        "roles": "You are a professional prompt engineer.",
        "requirements": "You need to complete the prompt according to the given framework.",
        "content": "{schema_description}",
        "examples": "For example\n" "---\n" "{schema_example}\n" "---",
        "outputs": "You only need to output a specific part of the refined prompt in JSON format. This part is {part}.\n"
        "Do not include any additional information.\n"
        "Refine the following text:",
    }
).get_message()
