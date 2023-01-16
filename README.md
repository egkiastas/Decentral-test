# Decentral-test
Short test from Decentral

### Short explanation

1. Initialize the matrix A to the coefficients of the equations in the system (rows represent equations, columns represent variables).
2. Initialize the vector b to the constant terms of the equations in the system.
3. Use Gaussian elimination to reduce the matrix A to an upper-triangular matrix.
4. Use back-substitution to find a solution for x1, x2, x3, and x4.
5. Return the solutions x1, x2, x3, and x4.

### Detailed explanation

1. The function solve_system takes two arguments: a matrix A representing the coefficients of the equations in the system, and a vector b representing the constant terms of the equations in the system.

2. The first step is to perform Gaussian elimination on the matrix A, which is done in the for-loop starting at line 8. The goal of Gaussian elimination is to convert the matrix A into an upper-triangular matrix, i.e. a matrix with zeros below the diagonal. This is done by iterating over each row and column of the matrix, and using a pivot element to eliminate the elements below it.

3. The pivot element is selected in the for-loop starting at line 10. It is the element with the largest absolute value on or below the diagonal of the current column.

4. The pivot element is then swapped with the element in the current row to bring it to the diagonal position. This is done on lines 12 and 13.

5.The elimination step is done in the for-loop starting at line 17. For each row below the current pivot row, a scalar factor is calculated to eliminate the element at the current column in that row. This is done by dividing the element by the pivot element, and then subtracting the resulting scalar multiple of the pivot row from the current row.

6. After the Gaussian elimination is completed, the matrix A is now an upper-triangular matrix and the vector b represents the constant terms of the equations in the system after being transformed accordingly.

7. The next step is to perform back-substitution, which is done in the for-loop starting at line 25. This is used to solve for the variables x1, x2, x3, and x4. The loop starts at the last row and works its way up to the first row. For each row, the value of the variable in that column is found by dividing the constant term of the equation by the coefficient of the variable. Then the value of the variable is used to eliminate the corresponding term in the equations above it.

8. When the loop is completed, the variable x will contain the values of x1, x2, x3, and x4 and the function will return it.
