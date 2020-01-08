import click
from pathlib import Path
import os

# refrecnce
# @click.command()
# @click.option('-count',default=1,help='number of greetings')
# @click.argument('name')
# def hello(count,name):
#     for x in range(count):
#         click.echo('hello %s!' % name)

@click.command()
@click.argument('project')
def Create(project):
    if os.path.isdir(project):
        click.secho('the project'+' '+ project +' ' + 'already exsists',fg='red')
    else:
        os.mkdir(project)
        os.chdir(project)
        click.secho('creating folder structure ...',fg='green')
        os.mkdir('templates')
        os.mkdir('static')
        os.mkdir('static/CSS')
        os.mkdir('static/JS')
        Path('__init__.py').touch()
        Path('run.py').touch()
        Path('routes.py').touch()
        Path('models.py').touch()
        click.secho('all done.',fg='green')
if __name__ == '__main__':
    Create()