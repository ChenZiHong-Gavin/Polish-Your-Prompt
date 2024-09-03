from .schema import Schema


class CHAT(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CHAT"
        self.description = (
            "CHAT is a prompt engineering framework that focuses on the four core elements of Character, History, "
            "Ambition, and Task to provide comprehensive interaction guidance."
        )
        self.components = {
            "Character": "Define the persona or role the language model should adopt, such as a professional, "
            "a student, or a specific character from a story.",
            "History": "Provide the contextual information relevant to the task, including the problem to be solved,"
            "the domain, and any other pertinent details.",
            "Ambition": "Outlines the intended goal or purpose that the language model should aim to achieve with its "
            "response. This provides a clear target for the model to work towards.",
            "Task": "The task is the specific action or deliverable that the language model is asked to perform or "
            "provide. This gives the model a clear and tangible instruction for the kind of output that is "
            "expected.",
        }
        self.schema_description = (
            "CHAT is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Design a healthy meal plan for a client with diabetes.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Character": "A nutritionist specializing in dietary plans for clients with diabetes.",\n'
            '"Background": "The client wants to eat healthy, but is allergic to certain foods.",\n'
            '"Ambition": "Create a balanced meal plan that meets the client\'s nutritional needs and dietary '
            'restrictions.",\n'
            '"Task": "Design a weekly meal plan with breakfast, lunch, dinner, and snacks for the client."\n'
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
