from .schema import Schema


class RISE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "RISE"
        self.description = (
            "RISE is a framework for providing clear instructions to ChatGPT by defining roles, inputs, steps, "
            "and expectations."
        )
        self.components = {
            "Role": "Define the role or position of the user in the given scenario. This helps set the context for "
            "the instructions.",
            "Input": "Provide the necessary description or resources required for the task. This could include "
            "relevant information or data.",
            "Steps": "Outline the detailed steps to be followed in order to accomplish the task. Break down the "
            "process into clear instructions.",
            "Expectation": "Describe the desired outcome or result of the task. This helps clarify the goal or "
            "objective to be achieved.",
        }
        self.schema_description = (
            "RISE is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )

        self.schema_example = (
            "Text: Create a summary of the key points discussed in the meeting.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Role": "Meeting participant",\n'
            '"Input": "The meeting was about the upcoming product launch and marketing strategy.",\n'
            '"Steps": "1. Review the meeting notes and identify key discussion points.\\n2. Summarize the main '
            'topics and decisions made during the meeting.\\n3. Organize the summary in a clear and concise manner.",\n'
            '"Expectation": "The summary should capture the main ideas and action items from the meeting."\n'
            "}\n"
            "```"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
