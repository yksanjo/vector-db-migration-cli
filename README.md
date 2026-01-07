# Vector DB Migration CLI Tool

![License](https://img.shields.io/github/license/yksanjo/vector-db-migration-cli)
![GitHub stars](https://img.shields.io/github/stars/yksanjo/vector-db-migration-cli?style=social)
![GitHub issues](https://img.shields.io/github/issues/yksanjo/vector-db-migration-cli)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![CLI](https://img.shields.io/badge/CLI-Tool-green)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

CLI tool that exports embeddings from source DB, re-embeds if needed (with batching), maintains metadata mappings, and validates data integrity post-migration.

## Features

- Migrate between different vector databases (Pinecone, Weaviate, Qdrant, etc.)
- Export embeddings from source DB
- Re-embed if needed (with batching for efficiency)
- Maintain metadata mappings during migration
- Validate data integrity post-migration
- Batch processing for large datasets

## Installation

```bash
pip install vector-db-migration-cli
```

## Usage

```bash
vector-migrate --source pinecone --destination weaviate --config migration.yaml
```

## Configuration

Create a `migration.yaml` file:

```yaml
source:
  type: "pinecone"
  apiKey: "your-source-api-key"
  environment: "us-west1-gcp"
  index: "source-index"
Destination:
  type: "weaviate"
  apiKey: "your-destination-api-key"
  endpoint: "https://your-instance.weaviate.network"
  class: "DestinationClass"
batchSize: 100
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT