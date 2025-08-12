from pydantic import BaseModel


class RootResponse(BaseModel):
    """Root response model."""

    message: str


class HealthComponents(BaseModel):
    """Components for health check."""

    memory_usage: str
    disk_usage: str
    cpu_usage: str


class HealthResponse(BaseModel):
    """Health response model."""

    status: int
    timestamp: str
    components: HealthComponents
