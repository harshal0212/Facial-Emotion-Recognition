from setuptools import setup, find_packages
import os

# Read the contents of README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read the contents of requirements file
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="facial-emotion-recognition",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A real-time facial emotion recognition system with GUI",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/facial-emotion-recognition",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "facial-emotion-recognition=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="facial recognition, emotion detection, computer vision, opencv, deepface, ai, machine learning",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/facial-emotion-recognition/issues",
        "Source": "https://github.com/yourusername/facial-emotion-recognition",
        "Documentation": "https://github.com/yourusername/facial-emotion-recognition#readme",
    },
) 