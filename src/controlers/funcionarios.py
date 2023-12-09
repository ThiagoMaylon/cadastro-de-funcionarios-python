import os
import pandas as pd
import openpyxl
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.database import Funcionario, db

db.connect()
db.create_tables([Funcionario])

def clear():
    # função para limpar o terminal sempre for chamada
    os.system('cls')

def cadastrar_funcionario():
    clear()
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    cargo = str(input('Cargo: '))
    salario = float(input('Salario: '))

    try:
        Funcionario.create(nome=nome, idade=idade, cargo=cargo, salario=salario)
        print('Cadastrado com sucesso...')
    except:
        print('Houve um erro...')

def editar_funcionario():
    clear()
    id_funcionario = int(input('digite o ID do Funcionario: '))
    nome = str(input('\nNome: '))
    idade = int(input('Idade: '))
    cargo = str(input('Cargo: '))
    salario = float(input('Salario: '))

    try:
        get_funcionario = Funcionario.get(Funcionario.id == id_funcionario)
        get_funcionario.nome = nome
        get_funcionario.idade = idade
        get_funcionario.cargo = cargo
        get_funcionario.salario = salario
        get_funcionario.save()
        print('Registro Atulizado...')
    except:
        print('Houve um erro...')

def ver_funcionarios():
    clear()
    funcionarios = Funcionario.select()
    id_func = []
    nome = []
    idade = []
    cargo = []
    salario = []
    for funcionario in funcionarios:
        id_func.append(funcionario.id)
        nome.append(funcionario.nome)
        idade.append(funcionario.idade)
        cargo.append(funcionario.cargo)
        salario.append(funcionario.salario)
    df = pd.DataFrame({
        'Id': id_func,
        'Nome': nome,
        'Idade': idade,
        'Cargo': cargo,
        'Salario': salario
    })
    print(df)

def deletar_funcionario():
    clear()
    get_id = int(input('digite o ID do Funcionario: '))
    get_func = Funcionario.get(Funcionario.id == get_id)
    get_func.delete_instance()

def salva_excel():
    funcionarios = Funcionario.select()
    id_func = []
    nome = []
    idade = []
    cargo = []
    salario = []
    for funcionario in funcionarios:
        id_func.append(funcionario.id)
        nome.append(funcionario.nome)
        idade.append(funcionario.idade)
        cargo.append(funcionario.cargo)
        salario.append(funcionario.salario)
    df = pd.DataFrame({
        'Id': id_func,
        'Nome': nome,
        'Idade': idade,
        'Cargo': cargo,
        'Salario': salario
    })
    df.to_excel('funcionarios.xlsx', index=False)
    print('Planilha foi Salva...')