import pytest
from pizza import Pizza, BasePizza

PIZZAS = ['Margherita', 'Pepperoni', 'Hawaiian']
SIZE_STR = ['L', 'XL']
SIZE_INT = [10, 20, 30, 35, 40, 100]


@pytest.mark.parametrize('s, exp', [
    (('Margherita', 30), 'Margherita, L'),
    (('Pepperoni', 31), 'Pepperoni, XL'),
    (('Hawaiian', 100), 'Hawaiian, XL'),
])
def test_can_make_pizza_from_recipes(s, exp):
    assert str(Pizza(*s)) == exp


@pytest.mark.parametrize('s, exp', [
    (('pomodoro', 30), 'pomodoro, L'),
    (('WHITE', 31), 'white, XL'),
])
def test_can_make_base_pizza(s, exp):
    assert str(BasePizza(*s)) == exp
