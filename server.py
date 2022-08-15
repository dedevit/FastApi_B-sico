from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI() # Cria a "Instancia FASTAPI"

class Animal(BaseModel): # Classe que herda de Base model e cria os atributos.
    id:Optional[str]
    nome: str
    sexo: str
    cor: str

banco:List[Animal] = [] # cria uma lista vazia do tipo lista que contera a lista de animais criada

@app.get ('/') # endpoint que da pagina inicial
def root():
    return {'EXERCICIO WOMAKERSCODE - FASTAPI'}

@app.get ('/animais') # endpoint que lista os aninamis criados 
def listar_animais():
    return banco

@app.get ('/animais/{animal_id}') # define  o path que será utilizado como filtro de busca dentro do obejto animal
def obter_animal(animal_id :str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return{'error' : "Animal não localizado"}

@app.delete ('/animais/{animal_id}') # para deletar o elemento também é utilizado o parâmentro Path
def remover_animal(animal_id :str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'error' : "Animal não localizado"}


@app.post ('/animais') # cria o endipoint que irá fazer o cadastro.
def criar_animal(animal: Animal):
   animal.id = str(uuid4())
   banco.append(animal)
   return None
