from typing import Annotated

from fastapi import APIRouter, Depends, Request

from {{ cookiecutter.module_name }}.api import models, settings

router = APIRouter(prefix="/examples")


def get_app_settings(request: Request) -> settings.AppSettings:
    """Get the API settings from FastAPI's app.state."""
    return request.app.state.settings


@router.get("/get", response_model=models.ExampleGetResponse)
def example_get():
    """Example get endpoint."""
    return models.ExampleGetResponse(result="An example GET response")


@router.post("/post", response_model=models.ExamplePostResponse)
def example_post(app_settings: Annotated[settings.AppSettings, Depends(get_app_settings)]):
    """Example post endpoint."""
    return models.ExamplePostResponse(
        settings=app_settings.settings.model_dump(), result="An example POST response (with input)"
    )
