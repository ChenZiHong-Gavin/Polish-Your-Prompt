class Template:
    def __init__(self, info):
        # Roles or Objectives
        self.roles = info["roles"]
        self.requirements = info["requirements"]
        # Task description
        self.content = info["content"]
        self.examples = info["examples"]
        # Output format
        self.outputs = info["outputs"]

    def get_message(self):
        infos = [
            self.roles,
            self.requirements,
            self.content,
            self.examples,
            self.outputs,
        ]
        infos = [info for info in infos if info]
        return "\n".join(infos)
