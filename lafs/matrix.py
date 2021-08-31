import sys, itertools

#TODO: Expand functionality to complex numbers
#TODO: Maybe implement an 'ans' system
# ans = 0

# Function ideas:
# lowertriangular, extracts lower triangular portion
# uppertrianguglar, similar but upper
# transforms in the same spirit

# Returns the dimension
def dim(matrix, k = None):
    if type(matrix) == Matrix:
        return matrix.dim(k)
    elif type(matrix) == int or type(matrix) == float:
        return 1
    else:
        print("ERROR: Input dimension not defined.")

# Returns the transpose
def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input transpose not defined.")

# Returns an Identity Matrix of dimensions (n, n_col)
def I(n, n_col = None):
    if n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(min(n, n_col)):
        ret._vals[i][i] = 1
    return ret

# Returns an Ones Matrix of dimensions (n, n_col)
def U(n, n_col = None):
    if n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret._vals[i][j] = 1
    return ret

# Returns an Zeros Matrix of dimensions (n, n_col)
def Z(n, n_col = None):
    if n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret._vals[i][j] = 0
    return ret

def is_square():
    pass


class Matrix:
    _dim = None
    _vals = None

    #TODO: Refactor __init__
    def __init__(self, *args):
        success = True
        if len(args) == 1 and type(args[0]) == str:
            rows = args[0].split(sep=';')
            vals = []
            for k in range(len(rows)):
                vals.append(list(map(int, rows[k].split())))
            n_row = len(vals)
            n_col = len(vals[0])
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            # Create a zero matrix
            n_row, n_col = args[0], args[1]
            vals = [[0] * n_col for _ in range(n_row)]
        elif len(args) == 1 and type(args[0]) == list:
            vals = args[0]
            n_row = len(vals)
            n_col = len(vals[0])
        elif len(args) == 3 and type(args[0]) == int and type(args[1]) == int and type(args[2]) == list:
            n_row, n_col, vals = args[0], args[1], args[2]
        else:
            print("ERROR: Invalid input")
            success = False
            # Validate data dimensions and data types
        if success:
            self.validate_data(n_row, n_col, vals)
            self._dim = (n_row, n_col)
            self._vals = vals

    #TODO: Refactor __init__
    def validate_data(self, n_row, n_col, vals):
        try:
            value_error = False

            # Number of rows must equal size of columns
            if n_row != len(vals):
                value_error = True
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
                if col_width[j] < len(str(self._vals[i][j])):
                    col_width[j] = len(str(self._vals[i][j]))

        for i in range(self.dim(0)):
            ret += "[ "
            for j in range (self.dim(1)):
                space_pad = " " * ( col_width[j] - len(str(self._vals[i][j])) )
                ret += space_pad + str(self._vals[i][j]) + "     "
            ret += "\b\b\b\b]\n"

        return ret

    #TODO: Refactor __call__
    def __call__(self, i, j):
        return self._vals[i][j]

    #### TODO: REMOVE SCALAR SUPPORT; NOT MATHEMATICALLY DEFINED. ####

    # Defines matrix-scalar and matrix-matrix left-addition:  <matrix> + <scalar|matrix>
    def __add__(self, summand):
        # Matrix-Scalar addition
        if type(summand) == int or type(summand) == float:
            ret = Matrix(*self.dim())
            for i in range(self.dim(0)):
                for j in range(self.dim(1)):
                    ret._vals[i][j] = self(i,j) + summand
            return ret

        # Matrix-Matrix addition
        elif type(summand) == Matrix:
            if self.dim() == summand.dim():
                ret = Matrix(*self.dim())
                for i in range(self.dim(0)):
                    for j in range(self.dim(1)):
                        ret._vals[i][j] = self(i,j) + summand(i,j)
                return ret
            else:
                print("ERROR: Matrix dimensions must match for addition.")
                #sys.exit(1)
        else:
            print("ERROR: Summand must be either scalar or matrix of same dimension.")
            raise ValueError()

    # Defines scalar-matrix right-addition: <scalar> + <matrix>
    def __radd__(self, summand):
        return self + summand

    # Defines matrix negation: -<matrix>
    def __neg__(self):
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                self._vals[i][j] *= -1
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
                    ret._vals[i][j] = self(i,j) * multiplicand
            return ret

        # Matrix-Matrix multiplication
        elif type(multiplicand) == Matrix:
            if self.dim(1) == multiplicand.dim(0):
                ret = Matrix(self.dim(0), multiplicand.dim(1))
                for i in range(self.dim(0)):
                    for j in range(multiplicand.dim(1)):
                        for k in range(self.dim(1)):
                            ret._vals[i][j] += self(i,k) * multiplicand(k, j)
                return ret
            else:
                print("ERROR: Incorrect matrix dimensions for matrix multiplication.")

    # Defines scalar-matrix right-multplication:  <scalar> * <matrix>
    def __rmul__(self, multiplier):
       return self * multiplier

    #TODO: Describe self.dim
    def dim(self, k = None):
        if k == None:
            return self._dim
        else:
            return self._dim[k]

    # Returns identity matrix of the same dimensions.
    def identity(self):
        return I(self.dim(0), self.dim(1))

    # Returns matrix transpose.
    def T(self):
        ret = Matrix(self.dim(1), self.dim(0))
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                ret._vals[j][i] = self._vals[i][j]
        return ret

if __name__ == "__main__":
    pass