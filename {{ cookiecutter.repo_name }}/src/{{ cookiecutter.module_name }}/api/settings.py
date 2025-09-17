from dataclasses import dataclass

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """API Configuration Settings."""

    example_setting: str = Field(default="example", description="Example setting that can be set.")

    model_config = SettingsConfigDict(env_file=".env")


@dataclass
class AppSettings:
    """Container for API settings."""

    settings: Settings


def load_settings() -> AppSettings:
    """Load the API state."""
    settings = Settings()

    return AppSettings(settings=settings)
