import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="no3ams",
    version="0.1",
    author="Naim Salameh",
    author_email="no3ams@gmail.com",
    description="DevOps Challenge Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/no3am/devops-challenge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)