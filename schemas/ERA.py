from .schema import Schema


class ERA(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "ERA"
        self.schema_description = (
            "ERA is a structured prompt framework designed for prompt engineering. It consists of three key components:"
            "Expectation, Requirement, and Action. This framework aims to help users clearly communicate their "
            "expectations from AI models, specify their requirements, and suggest the appropriate actions for the "
            "models to take."
        )
        self.components = {
            "Expectation": "Define the desired outcome or result expected from the AI model.",
            "Requirement": "Specify the specific requirements or criteria the AI model needs to fulfill.",
            "Action": "Describe the recommended action or steps for the AI model to execute in order to meet the "
            "requirements.",
        }
        self.schema_example = (
            "Text: Generate an article about the future development of artificial intelligence.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Expectation": "Generate an article about the future development of artificial intelligence.",\n'
            '"Requirement": "The article should include predictions on the future trends of AI technology, discuss its '
            'impact on society and the economy, and provide concrete examples to support the viewpoints.",\n'
            '"Action": "Compose the article ensuring it meets the aforementioned requirements, incorporating the '
            "latest "
            'research and industry trends."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
