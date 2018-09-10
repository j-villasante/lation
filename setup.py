from setuptools import setup

setup(
    name="lation",
    description="Transalation  file generator and modifier",
    package_dir={"": "src"},
    install_requires=[
        "py_mini_racer",
        "PyQt5"
    ]
)