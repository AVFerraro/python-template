from importlib import metadata

import {{ cookiecutter.module_name }}


class TestPackageVersion:
    def test_that_package_version_is_set(self):
        package_version = metadata.version("{{ cookiecutter.package_name }}")
        assert package_version is not None

    def test_that_imported_module_version_is_set(self):
        module_version = {{ cookiecutter.module_name }}.__version__
        assert module_version is not None

    def test_that_module_version_matches_package_version(self):
        package_version = metadata.version("{{ cookiecutter.package_name }}")
        module_version = {{ cookiecutter.module_name }}.__version__
        assert module_version == package_version, (
            f"module version {module_version} does not match package version {package_version}"
        )
