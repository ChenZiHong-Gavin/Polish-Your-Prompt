from .schema import Schema


class CARE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CARE"
        self.description = (
            "CARE is a prompt engineering framework that emphasizes four key elements: "
            "Context, Action, Result, and Example. It ensures clarity and effectiveness "
            "of prompts by providing contextual guidance, specifying the desired action, "
            "and outlining the expected result, along with illustrative examples."
        )
        self.components = {
            "Context": "Provide the relevant background information, including the problem "
            "to be solved, the domain, and any other pertinent details.",
            "Action": "Specify the concrete steps or actions the language model should take "
            "to address the given task or scenario.",
            "Result": "Define the desired outcome or objective that should be achieved "
            "through the language model's response.",
            "Example": "Offer one or more illustrative examples to help the language model "
            "better understand the expected input and output.",
        }
        self.schema_description = (
            "CARE is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Students are learning basic math concepts.\n"
            "Output: "
            "{\n"
            '    "Context": "Students are learning the fundamental principles of addition and subtraction.",\n'
            '    "Action": "Teach the basic rules and techniques for performing addition and subtraction.",\n'
            '    "Result": "Students will be able to solve simple arithmetic problems.",\n'
            '    "Example": [\n'
            '        "What is 5 + 3?",\n'
            '        "Answer: 5 + 3 = 8",\n'
            '        "What is 10 - 4?", \n'
            '        "Answer: 10 - 4 = 6"\n'
            "    ]\n"
            "}"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
