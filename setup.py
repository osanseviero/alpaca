from setuptools import find_packages, setup

install_requires = [
    "gradio",
]

extras = {}

extras["quality"] = [
    "black~=23.1",
    "ruff>=0.0.241",
    "mypy==0.982",
]

setup(
    name="alpaca_ml",
    version="0.0.1",
    author="Omar Sanseviero.",
    author_email="omar@huggingface.co",
    description="Minimalistic Modular library for API model inference",
    keywords="machine-learning models natural-language-processing deep-learning pytorch pretrained-models",
    license="Apache",
    url="https://github.com/osanseviero/alpaca",
    package_dir={"": "src"},
    packages=find_packages("src"),
    extras_require=extras,
    python_requires=">=3.7.0",
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
)