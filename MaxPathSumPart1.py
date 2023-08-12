import os

def read_file_triangle(triangle_name):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    Triangle = []
    with open(os.path.join(__location__, triangle_name)) as file:
        for line in file:
            number_strings = line.strip().split()
            numbers = []
            for string in number_strings:
                number = int(string)
                numbers.append(number)
            Triangle.append(numbers)
    return Triangle

def max_path_sum(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for column in range(row + 1):
            triangle[row][column]  += max(triangle[row + 1][column], triangle[row + 1][column + 1])
    return triangle[0][0]

Triangle_part_1 = read_file_triangle('Part_1_triangle_input.txt')
result = max_path_sum(Triangle_part_1)
print(result)



