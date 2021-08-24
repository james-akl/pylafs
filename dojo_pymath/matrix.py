import sys

def dim(matrix, k = None):
    #TODO: Add type checking
    return matrix.dim(k)

def identity(n, n_col = None):
    if n_col == None:
        n_col = n
    rows = []
    col = []
    for i in range(n):
        for j in range(n_col):
            col.append(int(i == j))
        rows.append(col)
        col = []
    return Matrix(n, n_col, rows)

class Matrix:
    _dim = None
    _vals = None

    def __init__(self, n_row, n_col, vals = None):
        if vals == None:
            vals = n_row * [n_col * [0]]
        else:
            # Validate data dimensions and data types
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

    def __add__(self, matrix):
        #TODO: dimension check
        if self.dim() == matrix.dim():
            n_row, n_col = self.dim()
            ret = Matrix(*self.dim())
            for i in range(n_row):
                for j in range(n_col):
                    ret._vals[i][j] = self(i,j) + matrix(i,j)
            return ret

        else:
            print("ERROR: Dimensions must match.")
            #sys.exit(1)

    def __neg__(self):
        for i in range(self.dim(0)):
            for j in range(self.dim(1)):
                self._vals[i][j] *= -1
        return self

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