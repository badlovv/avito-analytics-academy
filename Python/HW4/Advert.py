import json


class ColorizeMixin:

    def __str__(self):
        return (
            "\033[{style};{repr_color_code};{background_color}m{text}".format(
                style=self.__class__.repr_style,
                repr_color_code=self.__class__.repr_color_code,
                background_color=self.__class__.repr_background_color,
                text=self.__repr__(),
            )
        )

    def __repr__(self):
        return (
            "\033[{style};{repr_color_code};{background_color}m{text}".format(
                style=self.__class__.repr_style,
                repr_color_code=self.__class__.repr_color_code,
                background_color=self.__class__.repr_background_color,
                text=self.__repr__(),
            )
        )


class Json2Obj:

    def __init__(self, json_dict):
        self.__dict__.update(json_dict)

    @classmethod
    def json2obj(cls, dict1):
        if isinstance(dict1, str):
            dict1 = json.loads(dict1)
        # using json.loads method and passing json.dumps
        # method and custom object hook as arguments
        return json.loads(json.dumps(dict1), object_hook=cls)


class Advert(ColorizeMixin, Json2Obj):
    repr_style = 0
    repr_color_code = 33
    repr_background_color = 40

    def __new__(cls, json_str):
        inst_obj = Json2Obj.json2obj(json_str)
        inst_cls = super().__new__(cls)
        inst_cls.__dict__ = inst_obj.__dict__
        return inst_cls

    def __init__(self, json_str):
        ColorizeMixin.__init__(self)
        self.check()

    def check(self):
        if not hasattr(self, 'price'):
            self.price = 0
        elif self.price < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 10,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    ob = Advert(lesson_str)
    print(ob.price)
    print(ob.location.address)
    print(ob)
    print(repr(ob))
    repr(ob)
