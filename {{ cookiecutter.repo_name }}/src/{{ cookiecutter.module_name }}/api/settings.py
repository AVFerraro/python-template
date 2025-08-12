from dataclasses import dataclass

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from {{ cookiecutter.module_name }} import __version__


class Settings(BaseSettings):
    """API Configuration Settings."""

    api_version: str = Field(
        default=__version__,
        description="Version of the API. Defaults to the version of {{ cookiecutter.package_name }}.",
    )

    config = SettingsConfigDict(env_file=".env")


@dataclass
class AppSettings:
    """Container for API settings."""

    settings: Settings


def load_settings() -> AppSettings:
    """Load the API state."""
    settings = Settings()

    return AppSettings(settings=settings)
