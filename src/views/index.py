import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from controlers.funcionarios import cadastrar_funcionario, ver_funcionarios, deletar_funcionario, editar_funcionario, salva_excel

def menu():
    print('-'*10+' CADASTRO DE FUNCIONARIOS '+'-'*10)
    print('1) Cadastrar novo funcionario')
    print('2) Editar funcionario')
    print('3) Ver funcionarios cadastrados')
    print('4) Deletar funcionario')
    print('5) Salvar em excel')
    print('0) Sair')
    opcao = int(input('>> '))
    while opcao not in [1, 2, 3, 4, 5, 0]:
        print('Opção inválida....')
        opcao = int(input('\n>> '))
    return opcao

while True:
    match menu():
        case 1:
            cadastrar_funcionario()
        case 2:
            editar_funcionario()
        case 3:
            ver_funcionarios()
        case 4:
            deletar_funcionario()
        case 5:
            salva_excel()
        case 0:
            break
