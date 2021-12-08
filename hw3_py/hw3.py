

from library import load_matrix_from_file, save_martrix_to_file


def calculate_euclid_distance(p1, p2):
    """ Assuming points are from the same N space"""
    square_diff_sum = 0
    for i in range(len(p1)):
        square_diff_sum += (p1[i] - p2[i])**2

    return square_diff_sum ** 0.5


def problem1():
    """ Euclidean distance for two points """
    
    print("Distance: ", calculate_euclid_distance((0, 0, 0), (1, 0, 0)))
    print("Distance: ", calculate_euclid_distance((0, 0, 0), (1, 1, 0)))
    print("Distance: ", calculate_euclid_distance((0, 0, 0), (1, 1, 1)))


def determine_matrix_type(m):
    l1 = len(m)
    l2 = 0

    for i in range(l1):
        if(type(m[i]) is not list):
            return -1

        if(i > 0 and l2 != len(m[i])):
            return 0

        l2 = len(m[i])

    return 2 if l1 == l2 else 1


def problem2():
    """ Matrix type determination """

    ragged = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

    square = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rect = [[1, 2, 3], [4, 5, 6]]

    not_matrix = ["", ""]

    print("Ragged: ", determine_matrix_type(ragged))
    print("Square: ", determine_matrix_type(square))
    print("Rectangle: ", determine_matrix_type(rect))
    print("Not matrix: ", determine_matrix_type(not_matrix))


def transpose(m):
    if determine_matrix_type(m) != 1:
        return None

    l1, l2 = len(m), len(m[0])

    transposed = []
    for i in range(l2):
        transposed.append([])
        for j in range(l1):
            transposed[i].append(m[j][i])
    
    return transposed


def problem3():
    """ Transpose a rectangular matrix """

    square = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rect = [[1, 2, 3, 4], 
            [5, 6, 7, 8],
            [9, 10, 11, 12]]

    print("Transpose: ", transpose(square))
    print("Transpose: ", transpose(rect))


def generate_spiral_matrix(n):
    if n % 2 == 0:
        raise ValueError("N must be an even number")

    




def problem4():
    """ Spiral Matrix """



def problem5c_demo():
    """ Demo, using library functions """

    square = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rect = [[1, 2, 3, 4], 
            [5, 6, 7, 8],
            [9, 10, 11, 12]]

    save_martrix_to_file("sqr.txt", square)
    save_martrix_to_file("rect.txt", rect)

    loaded1 = load_matrix_from_file("sqr.txt")
    loaded2 = load_matrix_from_file("rect.txt")

    print("Loaded matrix: ", loaded1)
    print("Loaded matrix: ", loaded2)

# ======  RUNNING PROBLEM FUNCTIONS BELOW  =======

# problem5c_demo()
# problem4()
# problem3()
# problem2()
# problem1()