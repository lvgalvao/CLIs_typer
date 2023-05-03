from typer import Argument, Option, run
from rich import print

def olar (
    nome: str = Argument(..., metavar='ex: Luciano', help='seu primeiro nome'),
    email: str = Argument(..., metavar='ex: seuemail@dudu.com'),
    senha: str = Option(
    ...,
    prompt=True, 
    hide_input=True,
    confirmation_prompt=True,
    help='a senha será perguntada no prompt!'
    ),
    version: bool = Option(False, '--version', '-v', '--versao')
):
    print(f'{nome=}, {email=}, {senha=}')
    
run(olar) ## nome da função que quero rodar