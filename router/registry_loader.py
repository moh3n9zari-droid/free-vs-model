import yaml


def load_registry(path="models/model_registry.yaml"):

    with open(path, "r") as file:

        data = yaml.safe_load(file)

    return data["models"]


if __name__ == "__main__":

    registry = load_registry()

    print(registry.keys())
