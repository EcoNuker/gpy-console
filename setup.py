from setuptools import setup

setup(
    name="guilded.py-Console",
    version="0.1.2",
    description="Executes commands from console while your bot is running.",
    long_description=open("README.md").read(),
    url="https://github.com/EcoNuker/guilded.py-console",
    long_description_content_type="text/markdown",
    author="YumYummity",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.7"],
    packages=["gpyConsole"],
    install_requires = [
        "google-re2"
    ],
    include_package_data=True,
    extras_require={"gil.py": ["gil.py"], "guilded.py": ["guilded.py"]},
)
