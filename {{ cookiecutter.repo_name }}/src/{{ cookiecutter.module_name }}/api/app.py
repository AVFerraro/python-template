import logging
from contextlib import asynccontextmanager
from datetime import datetime

import psutil
from fastapi import FastAPI, HTTPException, Request, status

from {{ cookiecutter.module_name }} import __version__
from {{ cookiecutter.module_name }}.api import models, settings

logger = logging.getLogger(__name__)

APP_NAME = "{{ cookiecutter.package_name | upper | replace('-', '') }}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage API startup and shutdown."""
    try:
        app.state.settings = settings.load_settings()
        logger.info("API startup complete. Ready to serve requests.")
    except Exception as e:
        msg = "Failed to load API settings during startup: %s" % e
        logger.exception(msg)
        raise RuntimeError(msg) from e

    yield
    app.state.setting = None


def get_app_settings(request: Request) -> settings.AppSettings:
    """Get the API settings from FastAPI's app.state."""
    return request.app.state.settings


app = FastAPI(
    title=APP_NAME,
    description=f"Application Programming Interface for {APP_NAME}",
    version=__version__,
    lifespan=lifespan,
)


@app.get("/", response_model=models.RootResponse, tags=["General"])
def root() -> models.RootResponse:
    """Provide a welcome message for the API root endpoint."""
    return models.RootResponse(
        message=f"Welcome to {APP_NAME} API. Visit /docs for API documentation."
    )


@app.get("/health", response_model=models.HealthResponse, tags=["General"])
def health_check() -> models.HealthResponse:
    """Perform a health check on the API's system."""
    try:
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent
        cpu_usage = psutil.cpu_percent(interval=None)
        return models.HealthResponse(
            status=status.HTTP_200_OK,
            timestamp=datetime.now().isoformat(),
            components=models.HealthComponents(
                memory_usage=memory_usage, disk_usage=disk_usage, cpu_usage=cpu_usage
            ),
        )
    except Exception as e:
        msg = "Failed health check with error: %s" % e
        logger.exception(msg)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg) from e
