from .schema import Schema


class RACE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "RACE"
        self.description = (
            "RACE is a prompt engineering framework that helps users define the Role, Action, "
            "Result, and Example for a given task or scenario. It provides a structured approach "
            "to creating prompts that enable large language models to provide more accurate and "
            "relevant responses."
        )
        self.components = {
            "Role": "Specify the persona or perspective the language model should adopt, such as "
            "a subject matter expert, a customer, or a particular professional role.",
            "Action": "Describe the specific task or activity the language model should perform, "
            "such as writing, analyzing, or providing recommendations.",
            "Result": "Define the desired output or outcome the language model should produce, "
            "such as a report, a creative piece, or a set of recommendations.",
            "Example": "Provide a sample prompt or input that demonstrates the expected format "
            "and content of the desired output.",
        }
        self.schema_description = (
            "RACE is a framework for structuring prompts, which has the following components:\n\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Write a travel blog for me.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Role": "Travel blogger",\n'
            '"Action": "Write a blog post about the latest travel destination.",\n'
            '"Result": "The blog post should include a detailed overview of the destination and travel '
            'recommendations.",\n'
            '"Example": "Refer to previous blog posts about popular travel destinations."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
