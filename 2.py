import random as rnd


def read_file(file_name):
    f = open(file_name, 'r')
    field = []
    for line in f:
        fieldline = [line[i] for i in range(len(line) - 1)]
        field.append(fieldline)
    f.close()

    return field


field1 = read_file('field.txt')


def has_ship(data, cord):
    try:
        cord = (ord(cord[0].upper()) - 65, cord[1] - 1)
        if data[cord[1]][cord[0]] == '*':
            return True
        else:
            return False
    except IndexError:
        return False


def ship_size(field, cord):
    if has_ship(field, cord):
        size = 1
        for i in range(1, 4):
            if cord[1] + i <= 10 and has_ship(field, (cord[0], cord[1] + i)):
                size += 1
            else:
                break
        for i in range(1, 4):
            if cord[1] - i >= 0 and has_ship(field, (cord[0], cord[1] - i)) and cord[1] - i >= 1:
                size += 1
            else:
                break
        for i in range(1, 4):
            if ord(cord[0].upper()) + i <= ord('J') and has_ship(field, (chr(ord(cord[0]) + i), cord[1])):
                size += 1
            else:
                break
        for i in range(1, 4):
            if ord(cord[0].upper()) - i >= ord("A") and has_ship(field, (chr(ord(cord[0]) - i), cord[1])):
                size += 1

            else:
                break

    else:
        size = 0

    return size


def is_valid(data):
    four = 0
    three = 0
    two = 0
    one = 0
    for i in range(10):
        for j in range(1, 11):
            if ship_size(data, (chr(i + 65), j)) == 1:
                one += 1
            elif ship_size(data, (chr(i + 65), j)) == 2:
                two += 1
            elif ship_size(data, (chr(i + 65), j)) == 3:
                three += 1
            elif ship_size(data, (chr(i + 65), j)) == 4:
                four += 1
    if four / 4 == 1 and three / 3 == 2 and two / 2 == 3 and one == 4:
        return True
    else:
        return False


def field_to_str(field):
    str_out = ''
    for i in range(10):
        str_out = str_out + '\n'
        for j in range(10):
            str_out = str_out + field[i][j]
    return str_out


def generate_field():
    field1 = [[' ' for i in range(10)] for j in range(10)]
    for i in range(1, 11):
        if i == 1:
            shiphead = rnd.randint(0, 99)
            y = shiphead // 10
            x = shiphead - y * 10
            field1[y][x] = '*'
            direction = rnd.randint(1, 2)
            if direction == 1:
                for j in range(4):
                    if x + j < 10:
                        field1[y][x + j] = '*'
                    else:
                        field1[y][x - (4-j)] = "*"
            else:
                for j in range(4):
                    if y + j < 10:
                        field1[y + j][x] = '*'
                    else:
                        field1[y- (4-j)][x] = '*'
        else:
            pass
    return field1


print(field_to_str(generate_field()))
