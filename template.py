import os


dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, '.gitkeep')) as f:
        pass

files = [
    "dvc.yaml",
    "parameters.yaml",
    ".gitignore",
    os.path.join("src", "___init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass