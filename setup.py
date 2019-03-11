import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="servo_control",
    version="0.0.1",
    author="Scott Woodend",
    author_email="woodend_scott@gmail.com",
    description="Lightweight library for passing simple controls to a -model- servo using the Raspberry Pi Zero",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/servo_control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
