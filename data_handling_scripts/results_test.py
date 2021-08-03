import random

stations = [16606, 16607, 16611, 16613, 16614, 16619, 16622, 16624, 16627, 16632, 16641, 16642,
            16643, 16645, 16648, 16650, 16654, 16655, 16665, 16667, 16672, 16674, 16675, 16682,
            16684, 16685, 16687, 16692, 16693, 16699, 16701, 16706, 16707, 16710, 16715, 16716,
            16717, 16718, 16719, 16723, 16724, 16726, 16732, 16734, 16738, 16741, 16742, 16743,
            16744, 16746, 16749, 16750, 16754, 16756, 16757, 16758, 16759, 16760, 16766]

parameters = ['TN', 'TG', 'TX', 'DTR', 'RR']

for i in range (1, 5):
    station = random.randrange(0, 58, 1)
    parameter = random.randrange(0, 5, 1)
    month = random.randrange(1, 12, 1)
    year = random.randrange(1960, 2010, 1)

    print(f"Station: {stations[station]}, parameter: {parameters[parameter]}, month: {month}, year: {year}")
