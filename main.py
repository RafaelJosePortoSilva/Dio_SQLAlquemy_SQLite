from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy import Column
from sqlalchemy import create_engine 
from sqlalchemy import inspect
from sqlalchemy.sql import select


from faker import Faker
from random import randint

def gerar_cpf():
    cpf = ''.join([str(randint(0,9)) for _ in range(11)])
    return cpf

# Instanciando base para o banco
Base = declarative_base()

# Criando Tabelas

class Cliente(Base):
    __tablename__ = 'cliente'

    _id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50),nullable=False)
    cpf = Column(String(11),nullable=False)
    endereco = Column(String(50),nullable=True)

    conta = relationship(
        'Conta',
        back_populates='cliente',
        cascade = 'all, delete-orphan'
    )

    def __repr__(self):
        return f"""
        ID: {self._id}
        Nome: {self.nome}
        CPF: {self.cpf}
        Endereço: {self.endereco}
        """


class Conta(Base):
    __tablename__ = 'conta'

    _id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String,nullable=False)
    agencia = Column(String,nullable=False)
    numero = Column(Integer,nullable=False)
    id_cliente = Column(ForeignKey('cliente._id'),nullable=False)
    saldo = Column(Float,default=0)

    cliente = relationship(
        'Cliente',
        back_populates='conta'
    )

    def __repr__(self):
        return f"""
        ID: {self._id}
        Tipo: {self.tipo}
        Agencia: {self.agencia}
        Numero: {self.numero}
        ID_Cliente: {self.id_cliente}
        Saldo: {self.saldo}
        """



# Instanciando conexão com sqlite 
engine = create_engine('sqlite://')
# Passando as classes para serem criadas no banco
Base.metadata.create_all(engine)


faker = Faker('pt_BR')

with Session(engine) as session:
    clientes = list()
    for _ in range(10):
        clientes.append(Cliente(
            nome = faker.name(),
            cpf = gerar_cpf(),
            endereco = faker.address(),
            conta = [
                Conta(
                    tipo = 'corrente',
                    agencia = ''.join([str(randint(0,9)) for _ in range(4)]),
                    numero = randint(0,99)
                ) for _ in range(2)]
        ))
    
    # Enviando para o SGBD
    session.add_all(clientes)
    session.commit()



inspector = inspect(engine)
print(f'Todas as tabelas:\n{inspector.get_table_names()}')

stmt = select(Cliente)
print(f'\nTodos os dados na tabela Cliente: \n')
for cli in session.scalars(stmt):
    print(cli)
