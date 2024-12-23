import unittest

from app import create_app, db
from config import TestConfig
from app.models.champion import Champion

class ChampionModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_champion(self):
        champion = Champion(name='Aatrox', title='the Darkin Blade', blurb='Once honored defenders of Shurima against the Void...', square='Aatrox.png')
        db.session.add(champion)
        db.session.commit()

        db_champion = Champion.query.get(champion.id)
        self.assertEqual(db_champion.name, 'Aatrox')
        self.assertEqual(db_champion.title, 'the Darkin Blade')
        self.assertEqual(db_champion.blurb, 'Once honored defenders of Shurima against the Void...')
        self.assertEqual(db_champion.square, 'Aatrox.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)
        
