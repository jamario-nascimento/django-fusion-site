import uuid
from django.db import models
from django.db.models import IntegerField

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'devices'),
        ('lni-leaf', 'folha'),
        ('lni-package', 'caixa'),
        ('lni-drop', 'gota'),
        ('lni-star', 'estrela'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES2 = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'devices'),
        ('lni-leaf', 'folha'),
        ('lni-package', 'caixa'),
        ('lni-drop', 'gota'),
        ('lni-star', 'estrela'),

    )
    feature = models.CharField('Feature', max_length=100)
    descricao_feature = models.TextField('Descrição', max_length=200)
    icone_feature = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES2)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature


class Expense(Base):
    ICONE_CHOICES3 = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'devices'),
        ('lni-leaf', 'folha'),
        ('lni-package', 'caixa'),
        ('lni-drop', 'gota'),
        ('lni-star', 'estrela'),
    )
    CATEGORY_CHOICES = (
        ('combustivel', 'Combustível'),
        ('mecanica', 'Mecânica'),
        ('alimentacao', 'Alimentação'),
        ('devocional', 'Devocional'),
        ('recreacao', 'Recreação'),
    )
    expense = models.CharField('Expense', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES3)
    date = models.DateTimeField(auto_now=True)
    value = models.FloatField('Valor')
    category = models.CharField('Categoria', max_length=16, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField('Quantidade')
    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.expense