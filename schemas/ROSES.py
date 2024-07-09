from .schema import Schema


class ROSES(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "ROSES"
        self.description = (
            "ROSES is a framework for structuring prompts by defining the Role, Objective, Scenario, Expected "
            "Solution, and Steps."
        )
        self.components = {
            "Role": "Define the role or position of the user in the given scenario. This helps set the context for "
            "the instructions.",
            "Objective": "Clearly state the goal or objective to be achieved. This helps focus the response on "
            "completing the specific task.",
            "Scenario": "Provide relevant information or context for the given situation. This ensures the response "
            "takes into account the specific scenario.",
            "Expected Solution": "Describe the desired outcome or solution. This helps clarify the goal to be achieved.",
            "Steps": "Outline the specific steps or actions to be taken to accomplish the objective. Break down the "
            "process into clear instructions.",
        }
        self.schema_description = (
            "ROSES is a framework for structuring prompts, which has the following components:\n\n"
            + "\n".join([f"- **{k}**: {v}" for k, v in self.components.items()])
        )
        self.schema_example = (
            "Text: Analyze current market trends and develop marketing strategies for a new product.\n"
            "Output: "
            "```json\n"
            "{\n"
            '"Role": "Market Analyst",\n'
            '"Objective": "Analyze current market trends and develop marketing strategies for a new product.",\n'
            '"Scenario": "A new product is about to be launched and market demand needs to be understood.",\n'
            '"Expected Solution": "Provide marketing strategy recommendations based on market data.",\n'
            '"Steps": "Collect market data, analyze consumer behavior, develop marketing plans."\n'
            "}\n"
        )

    def format(self, structure):
        keys = structure.keys()
        res = ""
        for k in keys:
            res += f"# {k.upper()} #\n"
            res += f"{structure[k]}\n"
        return res
