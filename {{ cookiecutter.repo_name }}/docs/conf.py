import time
from importlib import metadata

distribution = metadata.distribution("{{ cookiecutter.package_name }}")
project = distribution.metadata["Name"]
author = distribution.metadata["Author"]
copyright = f"{time.strftime('%Y')}, {author} and contributors"
release = distribution.version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

napoleon_include_init_with_doc = True
