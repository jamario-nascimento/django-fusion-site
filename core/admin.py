from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Feature, Expense


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'icone_feature', 'ativo', 'modificado')

    @admin.register(Expense)
    class FeatureAdmin(admin.ModelAdmin):
        list_display = ('expense', 'value', 'date', 'ativo', 'modificado')
