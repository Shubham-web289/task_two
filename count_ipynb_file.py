def count_files():
    import os
    ls = os.listdir()

    py_ls = list(filter(lambda x : x.endswith("py"),ls))

    return("The number of python file is: " + str(len(py_ls)))

count_files()