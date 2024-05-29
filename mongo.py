
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def conecta_cliente(passwd):

    uri = f"mongodb+srv://rafaelportodev:{passwd}@cluster0.rj4ytcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    finally:
        return client


def cliente(str: nome, str:cpf, str:endereco, list:contas):
    post = {
        'nome':nome,
        'cpf':cpf,
        'endereco':endereco,
        'contas':contas
    }
    return post

def conta(str:tipo, str:agencia, int:numero, int:saldo=0):
    post = {
        'tipo':tipo,
        'agencia':agencia,
        'numero':numero,
        'saldo':saldo
    }
    return post

passwd = input('Senha: \n')

client = conecta_cliente(passwd)

db = client.dio
collection = db.bank

print(collection)
