import json
from pathlib import Path

from jsonschema import validate

schema = json.loads(Path("export_data.schema.json").read_text())
test_file = json.loads(Path("test_file.json").read_text())

print(validate(test_file, schema))
