import click
from project import app

@app.cli.command('hello')
def hello():
    click.echo('hello')