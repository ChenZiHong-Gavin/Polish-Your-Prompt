from polish_your_prompt.llm import OpenAIChat
from polish_your_prompt.schemas import *
from polish_your_prompt.templates import *
from polish_your_prompt.utils import extract_json_from_text
from polish_your_prompt.core.types import MODE


class Refiner:
    def __init__(self):
        self.llm_client = OpenAIChat()

    def refine(self):
        pass


class SimpleRefiner(Refiner):
    def refine(self, prompt: str = None, prefix: str = SIMPLE_REFINER_PREFIX_PROMPT):
        """
        :param prompt: the prompt to be refined
        :param prefix: the prefix to be added to the prompt for refinement
        :return: refined prompt
        """
        return self.llm_client.generate(prompt=prefix + prompt)


class SchemaRefiner(Refiner):
    def _one_step_refine(self, prompt: str, schema: Schema):
        prompt = (
            SCHEMA_REFINER_PREFIX_PROMPT.format(
                schema_description=schema.schema_description,
                schema_example=schema.schema_example,
            )
            + prompt
        )
        response = self.llm_client.generate(prompt=prompt)
        structure = extract_json_from_text(response)
        prompt = schema.format(structure)
        return structure, prompt

    def _step_by_step_refine(self, prompt: str, schema: Schema):
        res = {}
        components = schema.components
        for key in components.keys():
            prompt = (
                PART_SCHEMA_REFINER_PREFIX_PROMPT.format(
                    schema_description=schema.schema_description,
                    schema_example=schema.schema_example,
                    part=key,
                )
                + prompt
            )
            response = self.llm_client.generate(prompt=prompt)
            content = extract_json_from_text(response)
            res[key] = list(content.values())[0]
        prompt = schema.format(res)
        return res, prompt

    def refine(
        self, prompt: str = None, schema: Schema = COSTAR(), mode: MODE = MODE.ONE_STEP
    ):
        """
        :param mode: refining mode
        :param prompt: the prompt to be refined
        :param schema: the schema to be used for refining the prompt, default is CO-STAR schema
        :return: refined structure, refined prompt
        """
        if mode == MODE.ONE_STEP:
            return self._one_step_refine(prompt, schema)
        elif mode == MODE.STEP_BY_STEP:
            return self._step_by_step_refine(prompt, schema)
        else:
            raise ValueError("Invalid mode")


class AnnotatedRefiner(Refiner):
    def refine(self, prompt: str = None, content: str = None, annotations: dict = None):
        """
        :param prompt: the prompt to be refined
        :param content: generated text from the prompt
        :param annotations: the annotations to be used for refining the prompt
        :return: refined prompt
        """
        annotations_text = "\n".join(
            [f"- **{k}**: {v}" for k, v in annotations.items()]
        )
        prompt = ANNOTATED_REFINER_PREFIX_PROMPT.format(
            prompt=prompt, content=content, annotations=annotations_text
        )
        return self.llm_client.generate(prompt=prompt)
