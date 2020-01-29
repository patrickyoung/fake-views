from prefect import Flow, task, context
from schemas.customer import CustomerList
from converters import csv_converter


@task
def generate(schema, start, iterations):
    return schema.generate_list(iterations=iterations)

@task
def convert_to_csv(data, header):
    return csv_converter(data, header)

@task
def printer(data):
    print(data)

with Flow("customer-list") as flow:
    customer_list = CustomerList(seed="PATRICK")
    customer_list2 = CustomerList(seed="PATRICK")

    data = convert_to_csv(generate(customer_list, 0, 2), True)
    printer(data)

    data = convert_to_csv(generate(customer_list2, 0, 2), False)
    printer(data)

flow.run()