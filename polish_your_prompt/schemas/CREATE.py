from .schema import Schema


class CREATE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CREATE"
        self.description = (
            "CREATE is a prompt engineering framework that focuses on creating high-quality and effective prompts. "
            "It is based on five key principles: Clarity, Relevant Information, Examples, Avoiding Ambiguity, and "
            "Tinkering. By adhering to these principles, the CREATE framework helps to ensure that prompts are "
            "clear, informative, and easy to understand, while also allowing for iterative improvement."
        )
        self.components = {
            "Clarity": "Clearly define the task or intent that the prompt is designed to address.",
            "Relevant Info": "Provide all the necessary details and context for the prompt to be meaningful and useful.",
            "Examples": "Include relevant examples to illustrate the expected input and output format.",
            "Avoid Ambiguity": "Use precise language and avoid vague or ambiguous terms to ensure the prompt is "
            "unambiguous.",
            "Tinker": "Continuously refine and iterate on the prompt based on feedback and evaluation of the responses.",
        }
        self.schema_description = (
            "The CREATE framework comprises the following components:\n\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Provide a comprehensive market trend analysis report.\n"
            "Output:\n"
            "json\n"
            "{\n"
            '"Clarity": "The goal is to produce a detailed report analyzing the latest market trends and forecasts.",\n'
            '"Relevant Info": "The report should include the following sections:\n'
            "    - Executive summary\n"
            "    - Current market data and statistics\n"
            "    - Emerging trends and their potential impact\n"
            "    - Short-term and long-term market projections\n"
            '    - Recommendations for businesses to adapt to the changing market.",\n'
            '"Examples": "Here are examples of similar market trend analysis reports from the past year:",\n'
            "    - [Example Report 1 Link]\n"
            "    - [Example Report 2 Link]\n"
            '"Avoid Ambiguity": "Avoid using industry-specific jargon and acronyms. Ensure the report is easy to '
            'understand for a general audience.",\n'
            '"Tinker": "Based on feedback, refine the report structure, content, and language to make it more '
            'informative and actionable."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
