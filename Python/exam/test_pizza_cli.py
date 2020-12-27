import pytest
from click.testing import CliRunner
from pizza_cli import order, menu

PIZZAS = ['Margherita', 'Pepperoni', 'Hawaiian']
SIZE_STR = ['L', 'XL']
SIZE_INT = [10, 20, 30, 35, 40, 100]


def test_can_show_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert 'Hawaiian' in result.output


@pytest.mark.parametrize('s, exp', [
    (PIZZAS[0], f'Pizza {PIZZAS[0]} is ready to delivery!'),
    (PIZZAS[1], f'Pizza {PIZZAS[1]} is ready to delivery!'),
    (PIZZAS[2], f'Pizza {PIZZAS[2]} is ready to delivery!'),
])
def test_can_bake_pizzas(s, exp):
    runner = CliRunner()
    result = runner.invoke(order, [s])
    assert result.exit_code == 0
    assert exp in result.output


# @pytest.fixture()
@pytest.mark.parametrize('s, exp', [
    (PIZZAS[0], f'Your order is {PIZZAS[0]}'),
    (PIZZAS[1], f'Your order is {PIZZAS[1]}'),
    (PIZZAS[2], f'Your order is {PIZZAS[2]}'),
])
def test_can_order_pizzas(s, exp):
    runner = CliRunner()
    result = runner.invoke(order, [s])
    assert result.exit_code == 0
    assert exp in result.output


def test_can_order_pizza_with_delivery():
    runner = CliRunner()
    result = runner.invoke(order, [PIZZAS[0], '--delivery'])
    assert result.exit_code == 0
    assert f'Your order is {PIZZAS[0]}!' in result.output
    assert f'{PIZZAS[0]} is coming!' in result.output
    assert 'Pizza is delivered' in result.output


def test_can_order_pizza_with_pickup_and_log_seconds():
    runner = CliRunner()
    result = runner.invoke(order, [PIZZAS[0]])
    assert result.exit_code == 0
    assert f'Your order is {PIZZAS[0]}!' in result.output
    assert f'{PIZZAS[0]} is ready for pick-up!' in result.output
    assert 'picked up in' in result.output
