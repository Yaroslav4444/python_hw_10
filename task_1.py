"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class NonNegative:
    """class for filtering attributes"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение этого аттрибута не может быть "
                             "отрицательным!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    """creating a road class"""
    _length = NonNegative()
    _width = NonNegative()
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


asphalt_mass = Road(20, -5000)
asphalt_mass.calculation_asphalt_mass()
