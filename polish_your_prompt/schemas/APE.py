from .schema import Schema


class APE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "APE"
        self.description = (
            "APE is a prompt template that consists of the core elements: Action, Purpose, and Expectation. "
            "It aims to facilitate clear communication of tasks, discuss objectives, and set expectations, "
            "enhancing the efficiency of interaction with AI models."
        )
        self.components = {
            "Action": "Specify the task or action you want the AI model to perform. Clearly defining the action helps "
            "the model understand the intended task.",
            "Purpose": "Discuss the intent or objective behind the action. This helps the model focus its response "
            "and provide relevant information.",
            "Expectation": "Define the desired outcome or success criteria for the action. Setting clear expectations "
            "helps the model generate responses that meet your specific requirements.",
        }
        self.schema_description = (
            "APE is a framework for structuring prompts, which consists of the following components:\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Plan a trip from Beijing to Shanghai for me.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Action": "Plan a trip from Beijing to Shanghai for me.",\n'
            '"Purpose": "I need to attend an important business meeting in Shanghai and would like to visit some '
            'tourist attractions during the trip.",\n'
            '"Expectation": "The planned trip should include transportation options for round-trip, recommended '
            "accommodation, a schedule for the meeting, and recommendations for at least two tourist attractions. "
            'The total budget should be kept within XX RMB."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
