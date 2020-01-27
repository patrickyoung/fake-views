import json
import csv
import io
import itertools
import yaml
from mimesis.schema import Field, Schema


def json_converter(data):
    return json.dumps(data)


def csv_converter(data):
    output = io.StringIO()

    writer = csv.DictWriter(output, data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    return output.getvalue()


def load_yaml_config(config_file):
    with open(config_file, 'r') as config:
        return yaml.safe_load(config)


def generate(schema_definition, start=0, iterations=1, seed=None, language='en', converter=None):
    """
    >>> user = { 'id': 'uuid','name': 'person.full_name' }

    # Should return a 3 user account records as a list
    >>> user_data = generate(user, seed='TEST_DATA', iterations=3)
    >>> print(user_data)  #doctest: +NORMALIZE_WHITESPACE
    [{'id': 'c18f49b5-38e5-7e42-6d97-7ba818bb8585', 'name': 'Robena Dawson'},
     {'id': 'fdac87eb-e7f8-ab57-da54-000115eed230', 'name': 'Elois Vasquez'},
     {'id': 'e6203b3b-2658-fb46-b336-37b48edbcd02', 'name': 'Marshall Mills'}]
    """

    data_generator = generator(schema_definition, seed=seed, language=language)
    data_list = list(itertools.islice(data_generator, start, (start + iterations)))

    if converter:
        return converter(data_list)
    else:
        return data_list


def generator(schema_definition, seed=None, language='en'):
    """
    This code currently supports only flat schemas, but Mimesis does support complex schema definition.

    # >>> user = { 'id': 'uuid','name': 'person.full_name' }

    # # Should return a single user account record
    # >>> user_data = next(generator(user, seed='TEST_DATA'))
    # >>> print(user_data)
    # {'id': 'c18f49b5-38e5-7e42-6d97-7ba818bb8585', 'name': 'Robena Dawson'}

    # # Should return account record in Japanese language
    # >>> user_data = next(generator(user, seed='TEST_DATA', language='ja'))
    # >>> print(user_data)
    # {'id': 'c18f49b5-38e5-7e42-6d97-7ba818bb8585', 'name': '\u821e \u5fd7\u8cc0'}
    """
    _ = Field(language, seed=seed)

    fake_data = Schema(
        lambda: {key:_(value) for (key,value) in schema_definition.items()}
    )

    while True:
        yield fake_data.schema()
  

if __name__ == "__main__":
    import doctest
    doctest.testmod()
