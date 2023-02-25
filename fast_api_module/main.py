from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/runner_template/")
def runner_template(data = Body()):
    #какие поля нужно передавать?
    return {'h': 'd'}

@app.post("/stopper_template/")
def stopper_template(data = Body()):
    # какие поля нужно передавать?
    # как хранить путь к файлам?
    return {'h': 'q'}

@app.post("/changes_template/")
def changes_template(data = Body()):
    # как менять уже существующий бот?
    return {'h': 'c'}

@app.post("/create_db/")
def changes_template(data = Body()):
    # как создать автоматически sqllite3?
    return {'h': 'x'}

@app.post("/add_to_db/")
def changes_template(data = Body()):
    # как добавлять данные в sqllite3?
    return {'h': 'a'}

# какие методы еще нужны?