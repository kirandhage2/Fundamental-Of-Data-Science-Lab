n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
 # to check accepted year is leap or not
 # also check that is it asked to write by nested if then
    print()  # Move to the next line after each row 