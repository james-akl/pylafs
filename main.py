from lafs.matrix import Matrix, dim, identity

def main():
    data = [[1, 2, 4, 5], [2,4,2,1], [3,-2,-3,-1], [4,111,231,12]]
    mat = Matrix(4, 4, data)
    # mat = Matrix(1, 2, [[1, 2]])

    print(mat)
    print(mat + mat.identity())

if __name__ == "__main__":
    main()
