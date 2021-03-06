import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyelasticlogging-pkg-buchingerwilhelmi",
    version="0.0.1",
    author="Justin Guese",
    author_email="guese.justin@gmail.com",
    description="Allows for easy Elastic logging using the matching receiver module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BuchingerWilhelmiApp/easy-elastic-logging",
    project_urls={
        "Bug Tracker": "https://github.com/BuchingerWilhelmiApp/easy-elastic-logging/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["requests"],
    python_requires=">=3.8"
)