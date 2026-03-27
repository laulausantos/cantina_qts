from cantina import calcular_total, validar_pedido

def test_calcular_total_normal():
    assert calcular_total(2, 5) == 10


def test_calcular_total_zero():
    assert calcular_total(0, 10) == 0


def test_calcular_total_errado():
    assert calcular_total(2, 5) == 20 


def test_validar_pedido_valido():
    assert validar_pedido("Coxinha", 2, 5) == "Pedido válido"


def test_validar_pedido_item_vazio():
    assert validar_pedido("", 2, 5) == "Pedido inválido"


def test_validar_pedido_quantidade_invalida():
    assert validar_pedido("Suco", 0, 5) == "Pedido inválido"