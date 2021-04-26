from setuptools import find_packages, setup

setup(
    name="my_package_with_extra",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Logbook~=1.5",
    ],
    extras_require={
        "extra": [
            "requests",
        ],
    },
)
