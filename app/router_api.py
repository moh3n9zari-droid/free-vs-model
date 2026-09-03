from fastapi import APIRouter

from router.router_service import RouterService


router = APIRouter()

service = RouterService()


@router.get("/route/{task}")
def route_model(task: str):

    model = service.route(task)

    return {
        "task": task,
        "selected_model": model
    }
