# Write your solution here
def row_sums(my_matrix:list):
    [row.append(sum(row)) for row in my_matrix]


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)