# imports and global valuable


# how many rows and columns
def numbers_of_rows_cols():
    rows = int(input("Please enter the number of rows:"))
    cols = int(input("Please enter the number of columns:"))
    return rows, cols


# getting the numbers
def make_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input("Please enter every row seperetly:").split()))
        matrix.append(row)
    return matrix


# sum of rows and cols
def sum_row_col(matrix, rows, cols):
    sum_row = []
    sum_col = []
    print()
    for i in range(rows):
        sum_row_i = 0
        for j in range(cols):
            sum_row_i += matrix[i][j]
        print(f"Sum of row {i} = {sum_row_i}")
        sum_row.append(sum_row_i)

    for j in range(cols):
        sum_col_j = 0
        for i in range(rows):
            sum_col_j += matrix[i][j]
        print(f"Sum of col {j} = {sum_col_j}")
        sum_col.append(sum_col_j)

    return sum_row, sum_col


# main
def main():
    rows, cols = numbers_of_rows_cols()
    matrix = make_matrix(rows, cols)
    sum_row, sum_col = sum_row_col(matrix, rows, cols)
    print(f"sum of rows :{sum_row}\nsum of cols:{sum_col}")

# how many time do we want to repeat
answer = "y"
while answer.lower() == "y":
    main()
    answer = input("\nDo you want to do it again?(y/n):")
print("By By..")



