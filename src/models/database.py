from peewee import *

db = SqliteDatabase('funcionarios.db')

class Funcionario(Model):
    nome = CharField()
    idade = IntegerField()
    cargo = CharField()
    salario = DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        database = db