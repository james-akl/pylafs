import sys

def dim(matrix, k = None):
    #TODO: Add type checking
    return matrix.dim(k)

def identity(n, n_col = None):
    if n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(min(n, n_col)):
        ret._vals[i][i] = 1
    return ret

class Matrix:
    _dim = None
    _vals = None

#NEW CONSTRUCTOR
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

    def __call__(self, i, j):
        return self._vals[i][j]

    #Override binary addition operator "+"
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
                print("ERROR: Dimensions must match.")
                #sys.exit(1)
        else:
            print("ERROR: Summand must be either scalar or matrix of same dimension.")
            raise ValueError()

    #Override unary negation operator "-"
    def __neg__(self):
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                self._vals[i][j] *= -1
        return self

    #Override binary substraction operator "-"
    def __sub__(self, matrix):
        return self + (-matrix)

    def dim(self, k = None):
        if k == None:
            return self._dim
        else:
            return self._dim[k]

    def identity(self):
        return identity(self.dim(0), self.dim(1))

if __name__ == "__main__":
    pass