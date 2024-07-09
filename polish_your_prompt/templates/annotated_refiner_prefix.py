from .template import Template

ANNOTATED_REFINER_PREFIX_PROMPT = Template(
    {
        "roles": "You are a professional prompt engineer.",
        "requirements": "You need to improve the prompt according to the given annotations.",
        "content": "---original prompt---\n"
        "{prompt}\n"
        "---original prompt---\n"
        "---original generated content---\n"
        "{content}\n"
        "---original generated content---\n"
        "the prompt needs to be refined based on the following annotations:\n"
        "{annotations}",
        "examples": None,
        "outputs": "You need to refine the prompt based on the given annotations. "
        "Please output the refined prompt. "
        "Do not include any additional information.",
    }
).get_message()
