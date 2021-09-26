from recipe_api import db

class RecipeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=120), nullable=False, unique=True)
    recipe = db.Column(db.String(length=2048), nullable=False, unique=True)

    def __repr__(self):
        return f"Recipe('{self.id}', '{self.title}', '{self.recipe}')"

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': self.recipe
        }