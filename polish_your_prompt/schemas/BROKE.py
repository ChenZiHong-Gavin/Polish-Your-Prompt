from .schema import Schema


class BROKE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "BROKE"
        self.description = (
            "BROKE is a prompt engineering framework that combines the principles of OKR (Objectives and Key Results) "
            "to help design effective prompts for large language models. It provides a structured approach to defining "
            "the Background, Role, Objectives, Key Results, and Evolution Steps for a given task or scenario."
        )
        self.components = {
            "Background": "Provide the contextual information relevant to the task, including the problem to be solved,"
            "the domain, and any other pertinent details.",
            "Role": "Specify the persona or perspective the language model should adopt, such as a subject matter "
            "expert, a customer, or a particular professional role.",
            "Objectives": "Define the clear and measurable goals that the language model should aim to achieve "
            "through its response.",
            "Key Results": "Outline the specific, quantifiable outcomes that would indicate the objectives have been "
            "met. These act as checkpoints to track progress and success.",
            "Evolve": "Describe the iterative process of improving the prompt, either by refining the input, "
            "adjusting the answer, or regenerating the response, based on the evaluation of the previous "
            "outputs.",
        }
        self.schema_description = (
            "BROKE is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: As a software developer, I need to improve my programming skills to adapt to new technologies.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Background": "You are an experienced software engineer who needs to upskill to stay relevant in the '
            'industry.",\n'
            '"Role": "Experienced software engineer",\n'
            '"Objectives": "Learn and master the latest programming languages and development frameworks.",\n'
            '"Key Results": "Complete 3 projects using new languages, and participate in at least 2 online '
            'programming courses.",\n'
            '"Evolve": "Adjust the learning plan monthly based on project feedback and course progress."\n'
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
