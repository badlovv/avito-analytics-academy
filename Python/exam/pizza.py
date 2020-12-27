from deco import splitter

"""
Pizza module for a pizza restaurant.
"""

STRIP_CHARS = [' ', '.', ',', '-', '(', ')',
               '!', '"', "'", '#', "@", "$",
               '%', '^', '&', '*', '+', '`']


class BasePizza:
    """
    Pizza base class.
    Used for preparing base of a pizza using sauce and size.
    """

    def __init__(self, base_sauce: str = 'pomodoro', size: str = 'L'):
        if base_sauce.lower() in ['pomodoro', 'white', 'white sauce']:
            self.sauce = base_sauce.lower()
        else:
            raise ValueError('Cannot make base pizza with this base sauce!')
        if isinstance(size, int):
            self.size = 'L' if size < 31 else 'XL'
        else:
            self.size = size

    def __eq__(self, other):
        if self.sauce == other.sauce and self.size == other.size:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.sauce + self.size)

    def __iter__(self):
        yield 'sauce', self.sauce
        yield 'size', self.size

    def __repr__(self):
        return f'{self.sauce}, {self.size}'


class Pizza(BasePizza):
    """
    Pizza class.
    Used for preparing  a pizza using BasePizza and other ingredients.
    """

    PIZZAS = ['Margherita', 'Pepperoni', 'Hawaiian']
    RECIPES = dict({'Margherita ': {'sauce': 'pomodoro',
                                   'cheese': 'mozzarella',
                                   0: 'tomatoes'},
                    'Pepperoni': {'sauce': 'pomodoro',
                                  'cheese': 'mozzarella',
                                  0: 'pepperoni'},
                    'Hawaiian': {'sauce': 'pomodoro',
                                 'cheese': 'mozzarella',
                                 0: 'chicken',
                                 1: 'pineapples'}})

    def __init__(self, pizza: str, size):
        super().__init__(Pizza.RECIPES[pizza]['sauce'], size)
        self.pizza = pizza

    def __iter__(self):
        yield self.pizza, Pizza.RECIPES[self.pizza]

    def __repr__(self):
        return f'{self.pizza}, {self.size}'


if __name__ == '__main__':
    # info = splitter(input().split())
    info = splitter('pomodoro 30')
    print(info)
    for i, word in enumerate(info):
        info[i] = word.strip(''.join(STRIP_CHARS))
    sauce, size = info[:2]
    try:
        if size not in ['L', 'XL']:
            size = int(size)
    except ValueError:
        raise ValueError('Please use integer size to set base pizza'
                         ' or use "L" or "XL" instead')
    finally:
        if sauce not in ['pomodoro', 'white']:
            raise ValueError('Please, choose sauce from ["pomodoro", "white"]')

    print(sauce, size)
    pizza = Pizza('Margherita', 'XL')
    print(dict(pizza))
