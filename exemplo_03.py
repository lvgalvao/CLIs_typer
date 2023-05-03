from typer import Argument, run
from rich import print

def olar (
    nome: str = Argument(..., help='seu primeiro nome'),
    email: str = Argument(..., metavar='<email>@dudu.com'),
    senha: str = Argument(
        ..., envvar='SENHA')
):
    print(f'{nome=}, {email=}, {senha=}')
    
run(olar) ## nome da função que quero rodar