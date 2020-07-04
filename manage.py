
#from flask.ext.script import Manager
#from flask.ext.migrate import Migrate, MigrateCommand
import unittest

from config.settings import db, Migrate, Manager, MigrateCommand, init_app

init_app.app.app_context().push()

migrate = Migrate(init_app.app, db)
manager = Manager(init_app.app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    init_app.app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='services.py')
    #tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
