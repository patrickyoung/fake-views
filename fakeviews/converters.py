import json
import csv
import io


def json_converter(data):
    return json.dumps(data)


def csv_converter(data, header=True):
    output = io.StringIO()

    writer = csv.DictWriter(output, data[0].keys())
    if header:
        writer.writeheader()
    writer.writerows(data)

    return output.getvalue()