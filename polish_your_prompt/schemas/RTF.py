from .schema import Schema


class RTF(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "RTF"
        self.description = "RTF (Role-Task-Format) is a framework for structuring prompts by defining the Role, Task, and Format."
        self.components = {
            "Role": "Define the role or position of the user in the given scenario. This helps set the context for "
            "the instructions.",
            "Task": "Clearly state the task or objective to be achieved. This helps focus the response on completing "
            "the specific task.",
            "Format": "Specify the desired output format or structure. This guides the response to be in a specific "
            "format that meets the requirements.",
        }
        self.schema_description = (
            "RTF is a framework for structuring prompts, which has the following components:\n\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Analyze the stock market performance for the recent quarter.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Role": "Financial Analyst",\n'
            '"Task": "Analyze the stock market performance for the recent quarter.",\n'
            '"Format": "Provide a summary report containing key findings and trends."\n'
            "}\n"
        )
