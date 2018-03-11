import unittest
import coverage
from project import create_app, db
from project.api.models import User
from flask_migrate import MigrateCommand

COV = coverage.coverage(
    branch=True, 
    include='project/*',
    omit=[
        'project/tests/*'
    ]
)
COV.start()

app = create_app()
app.cli.add_command('db', MigrateCommand)

@app.cli.command('hello')
def hello():
    click.echo('hello')

@app.cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@app.cli.command()
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@app.cli.command()
def seed_db():
    db.session.add(User(username='aaron', email='aaron@gmail.com'))
    db.session.add(User(username='jeff', email='jeff@gmail.com'))
    db.session.commit()

@app.cli.command()
def cov():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1
