from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="rest_service",
    packages=find_packages(),
    version="0.1.0",
    description="rest_service_for_ml_project",
    author="nokrolikno",
    install_requires=required,
)
