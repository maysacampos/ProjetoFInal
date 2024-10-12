import math

# Funções Area do Cubo, Area do Paralelogramo e Area da Piramide

def area_cubo(lado):
    """Calcula a área de um cubo."""
    if lado < 0:
        raise ValueError("O lado não pode ser negativo.")
    return 6 * (lado ** 2)

def area_paralelogramo(base, altura):
    """Calcula a área de um paralelogramo."""
    if base < 0 or altura < 0:
        raise ValueError("Base e altura não podem ser negativos.")
    return base * altura

def area_piramide(aresta, altura_lateral):
    """Calcula a área total da pirâmide com base quadrada."""
    if aresta < 0 or altura_lateral < 0:
        raise ValueError("Aresta e altura não podem ser negativos.")
    area_base = aresta ** 2
    area_faces = 2 * aresta * altura_lateral  # Área lateral simplificada
    return area_base + area_faces


