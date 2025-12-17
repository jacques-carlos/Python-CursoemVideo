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
        print('ERRO ao ler o arquivo')
    else:
        título('Pessoas cadastradas')
        print(linha('~', 50))
        for l in arquivo:
            dados = l.split(';')
            dados[1] = dados[1].replace('\n','') 
            print(f'{dados[0]:<40}{dados[1]:<3}anos')
        print(linha('~', 50))
    finally:
        arquivo.close


def cadastrar(arq, nome, idade):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do Arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao cadastrar os dados no Arquivo')
        else:
            print('Dados adicionados com sucesso!')
    finally:
        arquivo.close