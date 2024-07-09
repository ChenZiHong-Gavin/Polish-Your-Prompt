from .schema import Schema


class TAG(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "TAG"
        self.description = (
            "TAG is a task planning and execution framework, where 'TAG' stands for Task, Action, and Goal. "
            "This framework guides users to first define the specific task, then plan the actions required, "
            "and finally set clear goals. By doing so, TAG helps break down complex projects or problems "
            "into more manageable and actionable parts."
        )
        self.components = {
            "Task": "Clearly define the specific task or project.",
            "Action": "Plan and outline the actions or steps required to complete the task.",
            "Goal": "Set clear and measurable goals or objectives for the task.",
        }
        self.schema_description = (
            "TAG is a framework for task planning and execution, which consists of the following components:\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Plan an online marketing campaign.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Task": "Plan an online marketing campaign.",\n'
            '"Action": "Identify the target audience, design the campaign theme and content, create a promotion plan, '
            'prepare marketing materials, execute and monitor the campaign progress.",\n'
            '"Goal": "Increase brand awareness, boost website traffic, and achieve at least a 10% sales growth rate."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
