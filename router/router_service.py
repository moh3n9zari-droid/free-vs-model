from router.registry_loader import load_registry
from router.model_router import ModelRouter
class RouterService:
    def __init__(self):
        registry = load_registry()
        self.router = ModelRouter(registry)
    def route(self, task: str):
        return self.router.select_model(task)
if __name__ == "__main__":
    service = RouterService()
    print(service.route("coding"))
    print(service.route("architecture"))
