from setuptools import setup, find_packages
from setuptools_scm import get_version

def load_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="trep",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="T-Rep: Representation Learning for Time-Series Using Time-Embeddings",
    url="https://github.com/let-it-care/t-rep",
    packages=find_packages(),
    install_requires=load_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8,<3.9",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
) 