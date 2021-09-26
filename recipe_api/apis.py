from recipe_api import app, api, Resource
from recipe_api.models import RecipeModel
from recipe_api import db

@app.route("/")
def index():
    return {'Greetings':'Welcome!'}

class RecipeAPI(Resource):

    def get(self,title):

        get_recipe = RecipeModel.query.filter_by(title=title).first()

        if get_recipe:
            return get_recipe.json()

        else:
            return {'Recipe':'There is no recipe like this!'}, 404

    def post(self,title,recipe):

        post_recipe = RecipeModel(title=title, recipe=recipe)
        db.session.add(post_recipe)
        db.session.commit()

        return post_recipe.json()

    def delete(self,title):

        del_recipe = RecipeModel.query.filter_by(title=title).first()

        try:
            db.session.delete(del_recipe)
            db.session.commit()

            return {'Delete':'Success!'}

        except:
            return {'Delete':'Failed!'}



class AllRecipesAPI(Resource):

    def get(self):

        get_all = RecipeModel.query.all()

        recipe_list = []

        for each_recipe in get_all:
            recipe_list.append(each_recipe.json())

        return recipe_list

api.add_resource(RecipeAPI,
                 '/recipe/api/title=<string:title>',
                 '/recipe/api/title=<string:title>',
                 '/recipe/api/title=<string:title>&recipe=<string:recipe>')

api.add_resource(AllRecipesAPI, '/recipes')