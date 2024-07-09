from .schema import Schema


class TRACE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "TRACE"
        self.schema_description = (
            "TRACE is a structured prompt framework consisting of five key components: Task, Request, Action, "
            "Context, and Example."
            "This framework helps users express their needs clearly and specifically, guiding AI models to perform "
            "tasks more accurately."
        )
        self.components = {
            "Task": "Define the specific task or instruction you want the AI model to perform.",
            "Request": "Specify any help or resources needed to complete the task.",
            "Action": "Describe the action or steps to be taken to accomplish the task.",
            "Context": "Provide relevant background information or context for the task.",
            "Example": "Include specific examples or instances related to the task.",
        }
        self.schema_example = (
            "Text: Write an article about environmental protection.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Task": "Write an article about environmental protection.",\n'
            '"Request": "Include the importance of environmental protection, current environmental issues, '
            'and personal measures for environmental conservation.",\n'
            '"Action": "Compose the article ensuring it meets the requirements mentioned above.",\n'
            '"Context": "In recent years, global environmental problems have become increasingly serious, '
            'and everyone should contribute to environmental protection.",\n'
            '"Example": "For instance, specific environmental conservation measures such as reducing the use of '
            'disposable plastic products and conserving water and electricity can be mentioned."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
