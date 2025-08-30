from pydantic import BaseModel

# print(response)

class PokemonSchema(BaseModel):
    name:str
    type:str

    class Config:
        from_attributes = True