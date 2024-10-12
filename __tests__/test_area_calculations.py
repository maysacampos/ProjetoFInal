import pytest # framworks de teste de unidade
from area.area import area_cubo, area_paralelogramo, area_piramide
from utils.utils import ler_csv    # função de leitura de arquivo csv

import csv

def ler_csv(caminho):
    with open(caminho, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Retorna uma lista de dicionários

# 2 - Testes

def test_area_cubo_positivo():
    """Teste positivo: área de um cubo com lado 3."""
    assert area_cubo(3) == 54  # 6 * (3 ** 2) = 54

def test_area_cubo_negativo():
    """Teste negativo: lado negativo."""
    with pytest.raises(ValueError, match="O lado não pode ser negativo."):
        area_cubo(-2)

def test_area_piramide_positivo():
    """Teste de unidade usando dados positivos de um arquivo CSV."""
    dados_positivos = ler_csv('fixtures/test_data_piramide_positivo.csv')
    for row in dados_positivos:
        aresta = float(row['aresta'])
        altura_lateral = float(row['altura_lateral'])
        resultado_esperado = float(row['resultado_esperado'])
        
        # Chama a função area_piramide e verifica se o resultado é o esperado
        resultado_obtido = area_piramide(aresta, altura_lateral)
        assert resultado_obtido == resultado_esperado, (
            f"Esperado {resultado_esperado}, mas obteve {resultado_obtido} "
            f"para aresta={aresta}, altura_lateral={altura_lateral}"
        )

def test_area_piramide_negativo():
    """Teste de unidade usando dados negativos de um arquivo CSV."""
    dados_negativos = ler_csv('fixtures/test_data_piramide_negativo.csv')
    for row in dados_negativos:
        aresta = float(row['aresta'])
        altura_lateral = float(row['altura_lateral'])
        with pytest.raises(ValueError):
            area_piramide(aresta, altura_lateral)
