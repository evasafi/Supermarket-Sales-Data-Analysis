from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="supermarket-analytics",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Professional-grade supermarket sales analytics with RFM segmentation and business intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/supermarket-analytics",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "black>=21.0",
            "flake8>=3.9.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
        ],
    },
    keywords=[
        "data-science",
        "analytics",
        "business-intelligence",
        "retail",
        "rfm-analysis",
        "customer-segmentation",
        "visualization",
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/supermarket-analytics/issues",
        "Source": "https://github.com/yourusername/supermarket-analytics",
        "Documentation": "https://github.com/yourusername/supermarket-analytics#documentation",
    },
)
