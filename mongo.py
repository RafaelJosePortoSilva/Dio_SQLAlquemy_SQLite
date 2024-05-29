
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker
from random import randint
import pprint



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


def cliente(nome:str,cpf:str,endereco:str,contas:list):
    post = {
        'nome':nome,
        'cpf':cpf,
        'endereco':endereco,
        'contas':contas
    }
    return post

def conta(tipo:str,agencia:str,numero:int,saldo:float=0):
    post = {
        'tipo':tipo,
        'agencia':agencia,
        'numero':numero,
        'saldo':saldo
    }
    return post

def gerar_cpf():
    cpf = ''.join([str(randint(0,9)) for _ in range(11)])
    return cpf



passwd = input('Senha: \n')

client = conecta_cliente(passwd)

db = client.dio
collection = db.bank

print(f"{collection}\n{'-'*60}\n")

fake = Faker('pt_BR')
for _ in range(2):
    post = cliente(
        nome=fake.name(),
        cpf=gerar_cpf(),
        endereco=fake.address(),
        contas=[conta(
            tipo='corrente',
            agencia=''.join([str(randint(0,9)) for _ in range(4)]),
            numero=randint(0,99)
        ) for _ in range(2)]
    )
    collection.insert_one(post)

all_data = collection.find({})
for data in all_data:
    pprint.pprint(data)


