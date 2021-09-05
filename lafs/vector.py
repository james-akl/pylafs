import lafs

def Vec(args):
    success = True
    if type(args) == str:
        rows = args.split(sep=' ')
        vals = []
        for k in range(len(rows)):
            vals.append(list(map(int, rows[k].split(';'))))
        n_row = len(vals)
        n_col = len(vals[0])
    elif type(args) == int:
        # Create a zero matrix
        n_row, n_col = args, 1
        vals = [[0] * n_col for _ in range(n_row)]
    elif type(args) == list:
        vals = [[x] for x in args]
        n_row = len(vals)
        n_col = 1
    else:
        print("ERROR: Invalid input")
        success = False
        # Validate data dimensions and data types
    if success:
        return lafs.matrix.Matrix(n_row, n_col, vals)