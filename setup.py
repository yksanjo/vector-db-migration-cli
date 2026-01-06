from setuptools import setup, find_packages

setup(
    name="vector-db-migration-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pinecone-client>=2.2.0",
        "weaviate-client>=3.15.0",
        "qdrant-client>=1.6.0",
        "pyyaml>=6.0",
        "tqdm>=4.62.0",
        "click>=8.0.0"
    ],
    entry_points={
        "console_scripts": [
            "vector-migrate=vector_db_migration.cli:main",
        ],
    },
    author="AI Engineer Community",
    description="CLI tool for migrating between vector databases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/vector-db-migration-cli",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)