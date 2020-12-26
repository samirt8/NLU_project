import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg-Samir-Tanfous-NLU",
    version="0.0.3",
    author="Samir Tanfous",
    author_email="samir.tanfous@gmail.com",
    description="RUN NLU pipeline",
    url="https://github.com/samirt8/NLU_project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=["tqdm", "pandas", "numpy", "sklearn", "torch", "transformers", "keras", "snips_nlu", "snips_nlu_metrics"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/train_samir_tanfous", "bin/test_benchmark_solution_samir_tanfous"],
    python_requires='>=3.6',
)
