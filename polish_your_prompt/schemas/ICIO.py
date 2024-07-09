from .schema import Schema


class ICIO(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "ICIO"
        self.description = (
            "ICIO is a prompt template designed to enhance the interaction efficiency and accuracy of AI models, where "
            "ICIO stands for Instruction, Context, Input, and Output."
        )
        self.components = {
            "Instruction": "Clearly state the task or instruction to guide the AI model in understanding the objective.",
            "Context": "Provide relevant background information to assist the AI model in responding appropriately to "
            "the specific scenario.",
            "Input": "Specify the input data or information required for the AI model to process and generate a "
            "response.",
            "Output": "Define the desired output indicators or instructions to guide the AI model in producing the "
            "expected results.",
        }
        self.schema_description = (
            "ICIO is a framework for structuring prompts, which consists of the following components:\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Generate a brief description of the D-Day Normandy landing.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Instruction": "Generate a brief description of the D-Day Normandy landing during World War II.",\n'
            '"Context": "The Normandy landing was a crucial operation that took place on June 6, 1944, during World '
            "War II. "
            "The Allied forces landed on the beaches of Normandy in France to break through the German defenses and "
            "establish "
            'a second front in Europe.",\n'
            '"Input": "None (This task involves text generation and doesn\'t require specific data analysis.)",\n'
            '"Output": "The description should include the landing time, location, parties involved, objectives, '
            "and significance, "
            'highlighting the key events and outcomes of the operation."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
