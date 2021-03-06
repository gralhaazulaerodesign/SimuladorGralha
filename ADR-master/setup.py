import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ADR",
    version="0.1",
    author="Ceu Azul Aeronaves",
    author_email="ceuazulufsc@gmail.com",
    description="This is Aircraft Design Resources",
    url="https://github.com/CeuAzul/ADR",
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=['wheel'],
    install_requires=['avlwrapper', 'numpy',
                      'matplotlib', 'pandas', 'scipy'],
    tests_requires=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
