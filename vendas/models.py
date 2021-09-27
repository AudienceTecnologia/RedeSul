from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

TIPO_CADASTRO = [
    ('Consórcio', 'Consórcio'),
    ('Financiamento', 'Financiamento'),
    ('Home Equity', 'Home Equity'),
]

TIPO_REGRA = [
    ('Antiga', 'Antiga'),
    ('Atual', 'Atual'),
]

TEMPO_ACOMPANHAMENTO = [
    ('1 mês', '1 mês'),
    ('2 mêses', '2 mêses'),
    ('3 mêses', '3 mêses'),
    ('4 mêses', '4 mêses'),
    ('5 mêses', '5 mêses'),
    ('6 mêses', '6 mêses'),
    ('7 mêses', '7 mêses'),
    ('8 mêses', '8 mêses'),
    ('9 mêses', '9 mêses'),
    ('10 mêses', '10 mêses'),
    ('11 mêses', '11 mêses'),
    ('12 mêses', '12 mêses'),
]

class Administradora(models.Model):
    Tipo_Cadastro = CharField(max_length=255, choices=TIPO_CADASTRO, blank=True, null=True)
    Logo = ImageField(blank=True, null=True)
    Nome = CharField(max_length=255, blank=True, null=True)
    Email = CharField(max_length=255, blank=True, null=True)
    CNPJ = CharField(max_length=255, blank=True, null=True)
    Status = CharField(max_length=255, blank=True, null=True)

class RegraComissionamento(models.Model):
    Administradora = ForeignKey(Administradora, on_delete=models.CASCADE, blank=True, null=True)
    Tipo_Regra = CharField(max_length=255, choices=TIPO_REGRA, blank=True, null=True)
    Nome = CharField(max_length=255, blank=True, null=True)
    Percentual_Comissao = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Numero_Parcelas_Comissao = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Tempo_Acompanhamento_Estorno = CharField(max_length=255, choices=TEMPO_ACOMPANHAMENTO, blank=True, null=True)
    Percentual_Estorno = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Numero_Parcelas_Estorno = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Inicio_Regra = DateField(blank=True, null=True)
    Fim_Regra = DateField(blank=True, null=True)
    Limite_Relatorio = DateField(blank=True, null=True)

CATEGORIA = [
    ('Supervisor', 'Supervisor'),
    ('Master', 'Master'),
    ('Junior I', 'Junior I'),
    ('Junior II', 'Junior II'),
    ('Interno', 'Interno'),
]

TIPO_EQUIPE = [
    ('Interna', 'Interna'),
    ('Externa', 'Externa'),
]

class Representante(models.Model):
    Foto = ImageField(blank=True, null=True)
    Nome = CharField(max_length=255, blank=True, null=True)
    Email = CharField(max_length=255, blank=True, null=True)
    CPF_CNPJ = CharField(max_length=255, blank=True, null=True)
    Status = CharField(max_length=255, blank=True, null=True)
    Percentual_Comissao = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Numero_Parcelas_Comissao = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Categoria = CharField(max_length=255, choices=CATEGORIA, blank=True, null=True)
    Tipo_Equipe = CharField(max_length=255, choices=TIPO_EQUIPE, blank=True, null=True)
    Percentual_Comissao_Equipe = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Numero_Parcelas_Estorno = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Percentual_Comissao_Estorno = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

TIPO_VENDA = [
    ('Interna', 'Interna'),
    ('Externa', 'Externa'),
]

TIPO_PESSOA = [
    ('Fisica', 'Fisica'),
    ('Juridica', 'Juridica'),
]

SEXO = [
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino'),
    ('Não optar', 'Não optar'),
]

ESTADO_CIVIL = [
    ('Solteiro', 'Solteiro'),
    ('Casado', 'Casado'),
    ('Divorciado', 'Divorciado'),
    ('Viúvo', 'Viúvo'),
]

class Consorcio(models.Model):
    Tipo_Venda = CharField(max_length=255, choices=TIPO_VENDA, blank=True, null=True)
    Tipo_Pessoa = CharField(max_length=255, choices=TIPO_PESSOA, blank=True, null=True)
    Administradora = ForeignKey(Administradora, on_delete=models.CASCADE, blank=True, null=True)
    Representante = ForeignKey(Representante, on_delete=models.CASCADE, blank=True, null=True)
    Grupo = CharField(max_length=255, blank=True, null=True)
    Cota = CharField(max_length=255, blank=True, null=True)
    Contrato = CharField(max_length=255, blank=True, null=True)
    Valor_Credito = CharField(max_length=255, blank=True, null=True)
    Status = CharField(max_length=255, blank=True, null=True)
    Nome = CharField(max_length=255, blank=True, null=True)
    Email = CharField(max_length=255, blank=True, null=True)
    CPF = CharField(max_length=255, blank=True, null=True)
    RG_CNH = CharField(max_length=255, blank=True, null=True)
    Orgao_Expedidor = CharField(max_length=255, blank=True, null=True)
    Data_Emissao = DateField(blank=True, null=True)
    Data_Nascimento = DateField(blank=True, null=True)
    Telefone = CharField(max_length=255, blank=True, null=True)
    Celular = CharField(max_length=255, blank=True, null=True)
    CEP = CharField(max_length=255, blank=True, null=True)
    Estado = CharField(max_length=255, blank=True, null=True)
    Cidade = CharField(max_length=255, blank=True, null=True)
    Rua = CharField(max_length=255, blank=True, null=True)
    Numero = CharField(max_length=255, blank=True, null=True)
    Complemento = CharField(max_length=255, blank=True, null=True)
    Bairro = CharField(max_length=255, blank=True, null=True)
    Nome_Pai = CharField(max_length=255, blank=True, null=True)
    Nome_Mae = CharField(max_length=255, blank=True, null=True)
    Sexo = CharField(max_length=255, choices=SEXO, blank=True, null=True)
    Natural_Cidade = CharField(max_length=255, blank=True, null=True)
    Nacionalidade = CharField(max_length=255, blank=True, null=True)
    Nome_Empresa = CharField(max_length=255, blank=True, null=True)
    Tempo_Empresa = CharField(max_length=255, blank=True, null=True)
    Profissao = CharField(max_length=255, blank=True, null=True)
    Renda = CharField(max_length=255, blank=True, null=True)
    CEP_Empresa = CharField(max_length=255, blank=True, null=True)
    Estado_Empresa = CharField(max_length=255, blank=True, null=True)
    Cidade_Empresa = CharField(max_length=255, blank=True, null=True)
    Rua_Empresa = CharField(max_length=255, blank=True, null=True)
    Numero_Empresa = CharField(max_length=255, blank=True, null=True)
    Complemento_Empresa = CharField(max_length=255, blank=True, null=True)
    Bairro_Empresa = CharField(max_length=255, blank=True, null=True)
    Telefone_Empresa = CharField(max_length=255, blank=True, null=True)
    Patrimonio_Total = CharField(max_length=255, blank=True, null=True)
    
