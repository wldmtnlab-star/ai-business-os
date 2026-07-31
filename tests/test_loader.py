from aibos.loader import Loader

loader = Loader()

data = loader.load("examples/minimal")

print("=== Organization ===")
print(data["organization"])

print()

print("=== Knowledge ===")
print(data["knowledge"]["company"])

print()

print("=== Worker ===")
print(data["workers"]["assistant"])

print()

print("=== Playbook ===")
print(data["playbooks"]["greeting"])