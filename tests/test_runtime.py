from aibos.runtime import Runtime

runtime = Runtime("examples/minimal")

prompt = runtime.build_prompt(
    playbook="greeting",
    inputs={
        "name": "MTN",
    },
)

print(prompt)