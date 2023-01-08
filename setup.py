from setuptools import find_namespace_packages, setup

setup(
    name="mani_skill2",
    version="0.3.0",
    author="SU Lab at UC San Diego",
    packages=find_namespace_packages(include=["mani_skill2*", "warp_maniskill*"]),
    extras_require={
        "tests": ["pytest", "black", "isort"],
        "docs": [
            "sphinx",
            "sphinx-autobuild",
            "sphinx-rtd-theme",
            # For spelling
            "sphinxcontrib.spelling",
            # Type hints support
            "sphinx-autodoc-typehints",
            # Copy button for code snippets
            "sphinx_copybutton",
            # Markdown parser
            "myst-parser",
        ],
    },
)
