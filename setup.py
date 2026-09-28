from setuptools import setup, find_packages

setup(
    name="mjlang",
    version="1.0.0",
    author="MJLang Developer",
    description="An esoteric programming language based on Michael Jackson",
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    py_modules=["mjlang"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "mjlang=mjlang:main",
        ],
    },
)
