from pydantic import BaseModel


class RootResponse(BaseModel):
    """Root response model."""

    message: str


class HealthComponents(BaseModel):
    """Components for health check."""

    memory_usage: float
    disk_usage: float
    cpu_usage: float


class HealthResponse(BaseModel):
    """Health response model."""

    status: int
    timestamp: str
    components: HealthComponents


class ExampleGetResponse(BaseModel):
    """Example get request response."""

    result: str


class ExamplePostResponse(BaseModel):
    """Example post request response."""

    settings: dict
    result: str
