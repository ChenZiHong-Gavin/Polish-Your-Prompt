from .schema import Schema


class CRISPE(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CRISPE"
        self.description = (
            "CRISPE is a prompt engineering framework that helps create structured prompts for large language "
            "models. It defines the Capacity and Role, Insight, Statement, Personality, and Experiment "
            "components to ensure prompts have a clear purpose and structure."
        )
        self.components = {
            "Capacity and Role": "Specify the capabilities the language model should have and the persona or "
            "perspective it should adopt to address the task.",
            "Insight": "Provide the background, context, and relevant information that informs the prompt.",
            "Statement": "Clearly articulate the specific task, request, or objective you want the language "
            "model to address.",
            "Personality": "Define the style, tone, and personality you want the language model to exhibit "
            "in its response.",
            "Experiment": "Outline the process of iterating on the prompt, trying different approaches, and "
            "evaluating the results to refine the prompt and improve the output.",
        }
        self.schema_description = (
            "CRISPE is a framework for structuring prompts, which has the following components:"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Provide a market analysis report on sustainable consumer trends.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Capacity and Role": "As a market analyst, analyze the latest consumer trends.",\n'
            '"Insight": "The target audience is young consumers interested in sustainable products.",\n'
            '"Statement": "Provide an analysis report on sustainable consumption trends.",\n'
            '"Personality": "The report should include data visualizations and clear conclusions.",\n'
            '"Experiment": "Explore different data sources and analysis methods to provide multiple perspectives."\n'
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
