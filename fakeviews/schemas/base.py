import itertools
from mimesis.schema import Schema, Field


class SchemaBase():
    def __init__(self, language='en', seed=None):
        self.language = language
        self.seed = seed
        self._ = Field(language, seed=seed)

    @property
    def schema(self):
        raise NotImplementedError('Subclass should implement this.')

    def generate(self):
        while True:
            yield self.schema.schema()

    def generate_list(self, start=0, iterations=1):
        return list(itertools.islice(self.generate(), start, (start + iterations)))
