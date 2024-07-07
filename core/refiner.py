from llm import OpenAIChat
from schemas import *
from templates import *
from utils import extract_json_from_text


class Refiner:
    def __init__(self):
        self.llm_client = OpenAIChat()

    def refine(self):
        pass


class SimpleRefiner(Refiner):
    def refine(self, prompt: str = None, prefix: str = None):
        """
        :param prompt: the prompt to be refined
        :param prefix: the prefix to be added to the prompt for refinement
        :return: refined prompt
        """
        if not prefix:
            prefix = SIMPLE_REFINER_PREFIX_PROMPT
        return self.llm_client.generate(prompt=prefix + prompt)


class SchemaRefiner(Refiner):
    def refine(self, prompt: str = None, schema: Schema = COSTAR(), mode: str = None):
        """
        :param mode: refining mode
        :param prompt: the prompt to be refined
        :param schema: the schema to be used for refining the prompt, default is CO-STAR schema
        :return: refined structure, refined prompt
        """
        prompt = SCHEMA_REFINER_PREFIX_PROMPT.format(schema_description=schema.schema_description,
                                                     schema_example=schema.schema_example) + prompt
        response = self.llm_client.generate(prompt=prompt)
        structure = extract_json_from_text(response)
        prompt = schema.format(structure)
        return structure, prompt


class AnnotatedRefiner(Refiner):
    def refine(self, prompt: str = None, annotations: dict = None):
        """
        :param prompt: the prompt to be refined
        :param annotations: the annotations to be used for refining the prompt
        :return:
        """
        pass


if __name__ == "__main__":
    refiner = SchemaRefiner()
    print(refiner.refine("help me do my homework"))
