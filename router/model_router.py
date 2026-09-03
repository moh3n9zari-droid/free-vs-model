class ModelRouter:

    def __init__(self, registry):
        self.registry = registry


    def select_model(self, task):

        for model, config in self.registry.items():

            if task in config.get("tasks", []):
                return model

        return "deepseek-coder"



if __name__ == "__main__":

    router = ModelRouter({})

    print(router.select_model("coding"))
