import requests
from pydantic import BaseModel

response = requests.get(url='https://www.mercadolivre.com.br')

# print(response)

class PokemonSchema(BaseModel):
    name:str
    type:str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)

    return PokemonSchema(name = data['name'], type = types)

    # return(data['name', types])

# print(pegar_pokemon(25))

if __name__ == '__main__':
    print(pegar_pokemon(10))