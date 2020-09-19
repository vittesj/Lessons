class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_mass_asphalt(self):
        return int(self._length * self._width * 25 * 5 / 1000)


road_1 = Road(int(input('Enter the length of the asphalt: ')), int(input('Enter the width of the asphalt: ')))
print('to cover the entire roadway, you will need', str(road_1.calculation_mass_asphalt()) + 'т', "asphalt's")
