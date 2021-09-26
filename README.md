<h3 align="center">
    This is a REST API project written in Python, Flask and used MySQL as Database
</h3>

| Request                                                                 | Type   | Process               |
|-------------------------------------------------------------------------|--------|-----------------------|
| http://localhost:5000/recipe/api/title=USER_INPUT                       | GET    | Search by title       |
| http://localhost:5000/recipe/api/title=USER_INPUT_1&recipe=USER_INPUT_2 | POST   | Add by title & recipe |
| http://localhost:5000/recipe/api/title=USER_INPUT                       | DELETE | Delete with           |
| http://localhost:5000/recipes                                           | GET    | Get All               |