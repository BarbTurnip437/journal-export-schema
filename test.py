import json
from pathlib import Path

from jsonschema import validate, ValidationError

SCHEMA = json.loads(Path("export_data.schema.json").read_text())

for test_file in Path("tests").glob("*.json"):
    test_json = json.loads(test_file.read_text())

    print(test_file, end=": ")
    try:
        print(validate(test_json, SCHEMA))
    except ValidationError as e:
        print(e.path, "->", e.message)
