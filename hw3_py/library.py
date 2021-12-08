def load_matrix_from_file(path):
    with open(path, "r") as f:
        m = []

        for i, l in enumerate(f.readlines()):
            m.append([])
            for n in l.split(","):
                m[i].append(int(n))

    return m

def save_martrix_to_file(path, m):
    with open(path, "w") as f:
        for i, l in enumerate(m):

            for j in range(len(l)):
                l[j] = str(l[j])

            f.write(",".join(l))

            if(i != len(m) - 1):
                f.write("\n")

        
