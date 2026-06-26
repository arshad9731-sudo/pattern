def print_mirrored_triangle(rows):
    # Loop through each row
    for i in range(1, rows + 1):
        # Print the leading spaces
        print(" " * (rows - i), end="")
        # Print the stars
        print("*" * i)

# Set the number of rows for the triangle
num_rows = 5
print_mirrored_triangle(num_rows)
