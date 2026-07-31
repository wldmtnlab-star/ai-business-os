from aibos import Validator

validator = Validator()

result = validator.validate(
    "examples/minimal/organization.yaml"
)

print("Validation:", result)