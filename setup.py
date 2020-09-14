import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tests_generator_json", # Replace with your own username
    version="0.0.1",
    author="Alberto Carbognin",
    author_email="carbogninalberto@gmail.com",
    description="This package helps to speedup test writing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carbogninalberto/tests-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)