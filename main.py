from sqlalchemy.ext.delcarative import declarative_base
from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy import Column



def cria_tabelas():
    Base = declarative_base()


    class Cliente(Base):
        __tablename__ = 'cliente'

        _id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(50),nullable=False)
        cpf = Column(String(11),nullable=False)
        endereco = Column(String(50),nullable=True)



    class Conta(Base):
        __tablename__ = 'conta'

        _id = Column(Integer, primary_key=True, autoincrement=True)
        tipo = Column(String,nullable=False)
        agencia = Column(String,nullable=False)
        numero = Column(Integer,nullable=False)
        id_cliente = Column(ForeignKey('cliente._id'),nullable=False)
        saldo = Column(Float,default=0)


def exemplo_popular_tabelas():
    ...


def exemplo_consultar_tabelas():
    ...