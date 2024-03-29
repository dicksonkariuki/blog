from app import create_app,db
from flask_script import Manager, Shell, Server
from app.models import User,Post,Comment
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
# app = create_app('production')
app = create_app('production')
manager = Manager(app)

# Creating migration
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

manager.add_command('server',Server)



@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment)


if __name__ == '__main__':
    manager.run()