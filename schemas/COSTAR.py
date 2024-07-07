from .schema import Schema


class COSTAR(Schema):
    def __init__(self):
        super().__init__()
        self.schema_name = "CO-STAR"
        self.schema_description = ("CO-STAR is a prompt template proposed by Sheila Teo in Singapore’s first ever "
                                   "GPT-4 Prompt Engineering competition organized by the Government Technology "
                                   "Agency of Singapore (GovTech). Check out the [article]("
                                   "https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering"
                                   "-competition-34c195a93d41) for more details.")
