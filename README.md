# Fake Views

A simple way to generate fake data using Mimesis => https://github.com/lk-geimfari/mimesis

## Run tests

```bash
python3 -m venv .env
source .env/bin/activate

python ./fake_views/generator.py -v
```

## Usage

Load a configuration and then print the rults of generate as CSV.

```python
from fake_views import generator

# Config currently supports simple flat tables, but Mimesis does support complext types. 
# https://github.com/lk-geimfari/mimesis

config = generator.load_yaml_config('./samples/user_table.yaml')

# Retrieve a Python list
print(generator.generate(config['schema'], 
               start=config['start'],
               iterations=config['iterations'],
               seed=config['seed'],
               language=config['language']))

# Retrieve a CSV string
print(generator.generate(config['schema'], 
               start=config['start'],
               iterations=config['iterations'],
               seed=config['seed'],
               language=config['language'],
               converter=generator.csv_converter))

# Start at the 5th item
print(generator.generate(config['schema'], 
               start=4,
               iterations=config['iterations'],
               seed=config['seed'],
               language=config['language'],
               converter=generator.csv_converter))

# Start at the 10,000th item
print(generator.generate(config['schema'], 
               start=9999,
               iterations=config['iterations'],
               seed=config['seed'],
               language=config['language'],
               converter=generator.csv_converter))

# Retrieve a generator instead of a list
import itertools
data = generator.generator(
    {'name': 'person.full_name', 'telephone': 'person.telephone' },
    seed='TEST_DATA_SEED',
    language='ja')

# Print the first 3 items from the generator
print(next(data))
print(next(data))
print(next(data))

# Print the next 5 items.  Note the pointer has moved ahead 3
first_five = itertools.islice(data, 0, 5)
print(list(first_five))
```

Load a configuration and then print the first 10 results then print results 5-10.

```python
from fake_views import generator

first_ten_results = 

print(generator.generate(config['schema'], 
               iterations=config['iterations'],
               seed=config['seed'],
               language=config['language'],
               converter=generator.csv_converter))
```