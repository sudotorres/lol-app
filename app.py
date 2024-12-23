import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app
from app.models.champion import Champion

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'Champion': Champion}