"""CLI entry point — run or validate a customer ETL pipeline."""
import click
from src.utils import load_config
from src.pipeline import Pipeline


@click.group()
def cli():
    """customer-etl — Run YAML-driven customer ETL pipelines."""
    pass


@cli.command()
@click.option("--config", "-c", required=True, help="Path to pipeline YAML config")
@click.option("--dry-run", is_flag=True, help="Validate config without executing")
def run(config, dry_run):
    """Execute the customer ETL pipeline."""
    cfg = load_config(config)
    pipeline = Pipeline(cfg)
    if dry_run:
        pipeline.validate()
    else:
        pipeline.execute()


@cli.command()
@click.option("--config", "-c", required=True, help="Path to pipeline YAML config")
def validate(config):
    """Validate pipeline YAML without running."""
    cfg = load_config(config)
    Pipeline(cfg).validate()


if __name__ == "__main__":
    cli()
