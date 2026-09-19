# how many rows and columns
def get_rows_cols():
    while True:
        try:
            rows = int(input("Please enter the number of rows: "))
            cols = int(input("Please enter the number of columns: "))
            break
        except ValueError:
            print("Please enter a valid value")

    return rows, cols


# getting the numbers
def make_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        while True:
            row = list(map(int, input("Please enter every row separately: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} numbers.")

    return matrix


# sum of rows and cols
def calculate_sums(matrix, rows, cols):
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
    answer = "y"
    while answer.lower() == "y":

        rows, cols = get_rows_cols()
        matrix = make_matrix(rows, cols)
        sum_row, sum_col = calculate_sums(matrix, rows, cols)
        print(f"sum of rows : {sum_row}\nsum of cols: {sum_col}")

        answer = input("\nDo you want to do it again?(y/n): ")
    print("Goodbye!")
    return 0


if __name__ == "__main__":
    main()