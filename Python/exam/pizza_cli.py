from time import sleep
from random import randint
from deco import log
import click

from pizza import Pizza

"""
Pizza restaurant CLI - a system to order, deliver
and store pizza before delivery.
"""


@click.group()
def cli() -> None:
    """CLI of a restaurant"""
    pass


@log('Baked in {:.2f} s!')
def bake(pizza: str) -> None:
    """
    Bakes pizza
    :param pizza: Pizza recipe
    :return: None
    """
    if pizza in Pizza.RECIPES:
        print(f'Start baking {pizza}!')
        sleep(randint(3, 5))
        print(f'Pizza {pizza} is ready to delivery!')
    else:
        print(f"Sorry, we don't have recipe of {pizza}!")


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Order some type of pizza with delivery option
    :param pizza: Type of pizza ('Margherita', 'Pepperoni', 'Hawaiian')
    :param delivery: is delivery order, default = False
    :return: None
    """
    print(f'Your order is {pizza}! Start baking...')
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@log('Pizza is delivered in {:.2f} s!'
     'Thank you for the order!')
def deliver(pizza: str) -> None:
    """Delivers baked pizza to customer"""
    print(f'{pizza} is coming!')
    sleep(randint(2, 5))


@log('picked up in {}s!')
def pickup(pizza: str) -> None:
    """Controls process of customer pick-up."""
    print(f'{pizza} is ready for pick-up!')
    sleep(randint(3, 7))


@cli.command()
def menu() -> None:
    """Shows pizza menu"""
    for pizza, ingr in Pizza.RECIPES.items():
        print(f'{pizza}: {" ".join(ingr.values())}')


if __name__ == '__main__':
    cli()
