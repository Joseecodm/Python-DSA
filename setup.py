from setuptools import setup, find_packages

setup(
    name="Python-DSA", 
    version="0.1.0", 
    author="José Manuel Cortes Cerón",
    author_email="230110688@itsoeh.edu.mx", 
    description="DSA Library for Python 3.13",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joseecodm/Python-DSA",  # Actualiza con la URL de tu repositorio
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
