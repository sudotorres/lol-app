from flask import render_template
from app.main import bp
from app.models.champion import Champion
from app.extensions import db

@bp.route('/')
def list():
    champions = Champion.query.all()
    return render_template('champions/list.html', champions=champions)

@bp.route('/view/<int:champion_id>')
def view(champion_id):
    champion = db.session.get(Champion, champion_id)
    return render_template('champions/view.html', champion=champion)