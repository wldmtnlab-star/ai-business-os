from aibos.loader import Loader
from aibos.prompt_builder import PromptBuilder

loader = Loader()

data = loader.load("examples/minimal")

builder = PromptBuilder()

prompt = builder.build(
    worker=data["workers"]["assistant"],
    knowledge=[
        data["knowledge"]["company"]
    ],
    playbook=data["playbooks"]["greeting"],
    inputs={
        "name": "MTN"
    },
)

print(prompt)