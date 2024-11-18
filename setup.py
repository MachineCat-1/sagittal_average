from setuptools import setup, find_packages

setup(
    name="sagittal_average",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any package dependencies here, e.g., 'numpy'
    ],
    author="Charlene",
    description="A package for calculating sagittal averages.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
