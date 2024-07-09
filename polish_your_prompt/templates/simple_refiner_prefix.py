from .template import Template

SIMPLE_REFINER_PREFIX_PROMPT = Template(
    {
        "roles": "You are a professional prompt engineer.",
        "requirements": "Think carefully, you need to refine the following text to make it more formal and professional."
        "You need to add more details to the text for better generation.",
        "content": None,
        "examples": None,
        "outputs": "Please directly output the refined text. Do not include any additional information.\n"
        "Refine the following text: ",
    }
).get_message()
