from flask_migrate import Migrate
from app import create_app, db
import click

app = create_app()
migrate = Migrate(app, db)

@app.cli.command()
@click.argument('command')
def db(command):
    """Run migration commands."""
    from flask_migrate import MigrateCommand
    if command == 'init':
        MigrateCommand.init()
    elif command == 'migrate':
        MigrateCommand.migrate()
    elif command == 'upgrade':
        MigrateCommand.upgrade()
    else:
        print("Invalid command")

if __name__ == "__main__":
    app.run(debug=True)
