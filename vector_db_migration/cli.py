import click
import yaml
from vector_db_migration.migrator import VectorDBMigrator

@click.command()
@click.option('--source', type=click.Choice(['pinecone', 'weaviate', 'qdrant']), required=True, help='Source vector database type')
@click.option('--destination', type=click.Choice(['pinecone', 'weaviate', 'qdrant']), required=True, help='Destination vector database type')
@click.option('--config', type=click.Path(exists=True), required=True, help='Configuration file path')
@click.option('--batch-size', type=int, default=100, help='Batch size for migration')
def main(source, destination, config, batch_size):
    """CLI tool for migrating between vector databases."""
    with open(config, 'r') as f:
        config_data = yaml.safe_load(f)
    
    migrator = VectorDBMigrator(
        source_type=source,
        destination_type=destination,
        config=config_data,
        batch_size=batch_size
    )
    
    try:
        migrator.migrate()
        click.echo("Migration completed successfully!")
    except Exception as e:
        click.echo(f"Migration failed: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main()