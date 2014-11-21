#!venv/bin/python
from app import app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.mail import Mail

def make_shell_context():
    from app.models import User, Role
    return dict(app=app, db=db, User=User, Role=Role)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()    
