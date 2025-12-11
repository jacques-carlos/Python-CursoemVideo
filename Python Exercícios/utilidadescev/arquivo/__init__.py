from utilidadescev.interface import *


def procurarArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close
    except:
        print('Houve um ERRO na criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    

def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        return 'ERRO ao ler o arquivo'
    else:
        título('Pessoas cadastradas')
        print(linha('~', 50))
        print(arquivo.read())
        print(linha('~', 50))
        arquivo.close


def adicionarNome(nome):
    try:
        arquivo = open(nome, 'wt')
        arquivo.close
    except:
        return 'Houve um ERRO ao tentar adicionar os dados no Arquivo!'
    else:
        título('Cadastrar nova pessoa')
        print(linha('~', 50))
        pessoa = leiaStr('Nome: ')
        idade = leiaInt('Idade: ')
        print(linha('~', 50))
        arquivo.write(pessoa, idade)
        arquivo.close
        return 'Dados adicionados com sucesso!'
        