from .schema import Schema


class COSTAR(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CO-STAR"
        self.description = (
            "CO-STAR is a prompt template proposed by Sheila Teo in Singapore’s first ever "
            "GPT-4 Prompt Engineering competition organized by the Government Technology "
            "Agency of Singapore (GovTech). Check out the [article]("
            "https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering"
            "-competition-34c195a93d41) for more details."
        )
        self.components = {
            "Context": "Provide background information relevant to the task. This helps the LLM understand the "
            "specific scenario being discussed, ensuring its response is relevant.",
            "Objective": "Define the task you want the LLM to perform. Clearly stating the objective helps the LLM "
            "focus its response on completing the specific task.",
            "Style": "Specify the writing style you want the LLM to use. This could be the style of a particular "
            "person or a professional expert (e.g., a business analyst or CEO). This guides the LLM to use "
            "language and phrasing that fit your needs",
            "Tone": "Set the desired attitude for the response. This ensures the LLM's response matches the required "
            "emotional or attitudinal context, such as formal, humorous, understanding, etc.",
            "Audience": "Identify the target audience for the response. Customizing the LLM's response for a specific "
            "audience (e.g., domain experts, beginners, children) ensures it is appropriate and "
            "understandable in the context you need",
            "Response": "Provide the format for the response. This ensures the LLM outputs the format required for "
            "your downstream task, such as a list, JSON, professional report, etc.",
        }
        self.schema_description = (
            "CO-STAR is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Write a professional email to a client requesting a meeting.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Context": "You are a business analyst at a consulting firm.",\n'
            '"Objective": "Request a meeting with a client to discuss the project timeline.",\n'
            '"Style": "Formal business email.",\n'
            '"Tone": "Professional and respectful.",\n'
            '"Audience": "Client, a senior executive at a tech company.",\n'
            '"Response": "Email format with clear meeting request and availability."\n'
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
