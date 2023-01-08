"""
Создать метакласс для паттерна Синглтон
"""


class Singleton(type):
    """creating Singleton class"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Road(metaclass=Singleton):
    """creating a road class"""
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_asphalt_mass(self):
        """mass calculation method"""
        res = (self._length * self._width * Road.weight * Road.thickness) \
              / 1000
        print(f"Масса асфальта,необходимая для покрытия всего дорожного "
              f"полотна: {res} тонн")


asphalt_mass = Road(20, 5000)
asphalt_mass1 = Road(20, 5000)
print(asphalt_mass is asphalt_mass1)
asphalt_mass.calculation_asphalt_mass()
