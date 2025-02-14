from setuptools import setup, find_packages

setup(
  name="jane_api",
  version="0.1.0",
  packages=find_packages(),
  install_requires=["pydantic", "requests"],
  author="@enyineer",
  author_email="hi@enking.dev",
  description="A package for interacting with the Grow with Jane Web API (Read-Only)",
  url="https://github.com/enyineer/jane_api",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)
