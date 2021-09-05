from typing import NewType
import lafs
import copy
# import sys

#TODO: replace some ValueError with TypeError

def Mat(*args):
    return Matrix(*args)

#TODO: Expand functionality to complex numbers
class Matrix:
    #TODO: Make member attributes private using "__"
    #TODO: Implement accessor/mutator methods
    __dim = None
    __rowlist = None # Replace with __rows

    def __init__(self, *args):

        # Option 1: String input; Matrix('1 2; 3 4') yields [[1, 2], [3, 4]].
        if len(args) == 1 and type(args[0]) == str:
            rows = args[0].split(sep=';')
            vals = []
            for k in range(len(rows)):
                vals.append(list(map(int, rows[k].split())))
            n_row = len(vals)
            n_col = len(vals[0])

        # Option 2: Dimensions input; Matrix(2, 3) yields 2-by-3 zeros matrix.
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            n_row, n_col = args[0], args[1]
            vals = [[0] * n_col for _ in range(n_row)]

        # Option 3: Square dimension input; Matrix(2) yields 2 zeros matrix.
        elif len(args) == 1 and type(args[0]) == int:
            n_row, n_col = args[0], args[0]
            vals = [[0] * n_col for _ in range(n_row)]

        # Option 4: 2D List input; Matrix([[1, 2], [3, 4]]).
        elif len(args) == 1 and type(args[0]) == list:
            vals = args[0]
            n_row = len(vals)
            n_col = len(vals[0])

        # Option 5: Redundant ('secure') input; Matrix(2, 1, [[1], [2]])
        elif len(args) == 3 and type(args[0]) == int and type(args[1]) == int and type(args[2]) == list:
            n_row, n_col, vals = args[0], args[1], args[2]

        # Raise error for invalid input.
        else:
            raise ValueError("Invalid input.")

        # Validate data dimensions and data types.
        self.validate_data(n_row, n_col, vals)
        self.__dim = (n_row, n_col)
        self.__rowlist = vals #Replace with __rows

    def validate_data(self, n_row, n_col, vals):
        try:
            value_error = False

            # Number of rows must equal size of columns
            if n_row != len(vals):
                value_error = True
                raise ValueError("Number of rows must equal length of columns")
            for i in range(n_row):
                # Number of columns must equal size of rows
                if n_col != len(vals[i]):
                    value_error = True
                    break
                # All data entries must be numbers
                for j in range(n_col):
                    if type(vals[i][j]) != int and type(vals[i][j]) != float:
                        raise ValueError("All data entries must be numbers.")
            if value_error:
                raise ValueError("Matrix and data dimensions do not match.")

        except ValueError:
            print("ERROR: Input data is invalid.")
            raise
            sys.exit(1)

    #TODO: Refactor __repr__
    def __repr__(self):
        ret = ""
        col_width = self.dim(1) * [1]

        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                if col_width[j] < len(str(self[i][j])):
                    col_width[j] = len(str(self[i][j]))

        for i in range(self.dim(0)):
            ret += "[ "
            for j in range (self.dim(1)):
                space_pad = " " * ( col_width[j] - len(str(self[i][j])) )
                ret += space_pad + str(self[i][j]) + "     "
            ret += "\b\b\b\b]\n"

        return ret

    #TODO: Refactor __call__
    def __call__(self, i=None, j=None):
        if i != None and j != None:
            return self[i][j]
        if i != None:
            return self[i]
        return self.__rowlist

    def __getitem__(self, row):
        return self.__rowlist[row]

    def __setitem__(self, row, new_value):
        if type(new_value) != list or len(new_value) != self.dim(0):
            raise TypeError("Input must be list of same length as matrix row.")
        self.__rowlist[row] = new_value

    # Defines matrix-matrix addition:  <matrix> + <matrix>
    def __add__(self, summand):
        # Matrix-Matrix addition
        if type(summand) == Matrix:
            if self.dim() == summand.dim():
                ret = Matrix(*self.dim())
                for i in range(self.dim(0)):
                    for j in range(self.dim(1)):
                        ret[i][j] = self(i,j) + summand(i,j)
                return ret
            else:
                raise ValueError("Matrix dimensions must match for addition.")
                #sys.exit(1)

        # UNDEFINED IN MATHEMATICS; USE <matrix> + <scalar> * U(matrix) INSTEAD.
        # # Matrix-Scalar addition
        # elif type(summand) == int or type(summand) == float:
        #     print
        #     ret = Matrix(*self.dim())
        #     for i in range(self.dim(0)):
        #         for j in range(self.dim(1)):
        #             ret[i][j] = self(i,j) + summand
        #     return ret

        else:
            raise ValueError("Summand must be matrix of same dimension.")

    # Handles scalar-matrix right-addition: <scalar> + <matrix>
    def __radd__(self, summand):
        return self + summand

    # Defines matrix negation: -<matrix>
    def __neg__(self):
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                self[i][j] *= -1
        return self

    # Defines matrix-matrix and matrix-scalar subtraction <matrix> - <scalar|matrix>
    def __sub__(self, subtrahend):
        return self + (-subtrahend)

    # Defines matrix-matrix and scalar-matrix subtraction <scalar> - <matrix>
    def __rsub__(self, minuend):
        return minuend + (-self)

    # Defines matrix-scalar and matrix-matrix left-multplication:  <matrix> * <scalar|matrix>
    def __mul__(self, multiplicand):
        # Matrix-Scalar multiplication
        if type(multiplicand) == int or type(multiplicand) == float:
            ret = Matrix(*self.dim())
            for i in range(self.dim(0)):
                for j in range(self.dim(1)):
                    ret[i][j] = self(i,j) * multiplicand
            return ret

        # Matrix-Matrix multiplication
        elif type(multiplicand) == Matrix:
            if self.dim(1) == multiplicand.dim(0):
                ret = Matrix(self.dim(0), multiplicand.dim(1))
                for i in range(self.dim(0)):
                    for j in range(multiplicand.dim(1)):
                        for k in range(self.dim(1)):
                            ret[i][j] += self(i,k) * multiplicand(k, j)
                return ret
            else:
                print("ERROR: Incorrect matrix dimensions for matrix multiplication.")

    # Defines scalar-matrix right-multplication:  <scalar> * <matrix>
    def __rmul__(self, multiplier):
       return self * multiplier   

    # Defines equality: <matrix> == <right>
    def __eq__(self, right):
        if type(right) == Matrix:
            if self.dim() == right.dim():
                for i in range(self.dim(0)):
                    for j in range(self.dim(1)):
                        if self(i,j) != right(i,j):
                            return False
                return True
        return False

    # Defines matrix power: <matrix> ** <int>
    #TODO: Implement negative integers
    def __pow__(self, n):
        if type(n) != int:
            raise ValueError("Exponent must be an integer.")
        if self.dim(0) != self.dim(1):
            raise ValueError("Matrix must be square for exponentiation.")
        ret = self.identity()   
        multiplicand = self if n >= 0 else lafs.gauss.inv(self)
        for k in range(abs(n)):
            ret *= multiplicand
        return ret

    # Defines array-wise/Hadamard multiplication: <matrix> @ <matrix>
    def __matmul__(self, multiplicand):
        if type(multiplicand) == Matrix:
            if self.dim() == multiplicand.dim():
                ret = Matrix(*self.dim())
                for i in range(self.dim(0)):
                    for j in range(self.dim(1)):
                        ret[i][j] = self(i,j) * multiplicand(i,j)
                return ret
            else:
                raise ValueError("Matrix dimensions must match for addition.")
                #sys.exit(1)

        else:
            raise ValueError("ERROR: multiplicand must be matrix of same dimension.")

    #TODO: Describe self.dim
    def dim(self, k = None):
        if k == None:
            return self.__dim
        else:
            return self.__dim[k]

    # Returns identity matrix of the same dimensions.
    def identity(self):
        ret = Matrix(self.dim(0), self.dim(1))
        for i in range(min(self.dim(0), self.dim(1))):
            ret[i][i] = 1
        return ret

    # Returns matrix transpose.
    def T(self):
        ret = Matrix(self.dim(1), self.dim(0))
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                ret[j][i] = self[i][j]
        return ret

    # Swaps rows in-place.
    def swap_rows(self, r1, r2):
        row = self[r1]
        self[r1] = self[r2]
        self[r2] = row

    #TEMPORARY;
    def r(self, d):
        ret = copy.deepcopy(self)
        for i in range(ret.dim(0)):
            for j in range(ret.dim(1)):
                ret[i][j] = round(ret(i,j), d)
        return ret

    #REFACTOR
    def sub(self, r1, r2, c1, c2):
        return Matrix([mat[c1:(c2 + 1)] for mat in self[r1:(r2 + 1)]])

    #REFACTOR
    def inner(self, matrix):
        ret = (self.T() * matrix)
        if self.dim(1) == 1:
           return ret(0,0)
        return ret

if __name__ == "__main__":
    pass