import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="y",
    version="0.0.1",
    author="MatteGary",
    description="Python interface with Shelly Relay IOT Device.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/MatteGary/shellypy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)