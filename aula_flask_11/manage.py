import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate

app = create_app(os.getenv("FLASK_CONFIG") or "default")

@app.cli.command()
def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)