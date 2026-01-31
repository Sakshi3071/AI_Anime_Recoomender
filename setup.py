from setuptools import setup,find_packages

with open("Requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.3",
    author="Sakshi-Satre",
    packages=find_packages(),
    install_requires = requirements,
)