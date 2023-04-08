# TODO: Implement formulas
def Ochiai(e_p, n_p, e_f, n_f):
    denom = (e_f + e_p) * n_f
    denom = denom ** 0.5
    return e_f/denom

def Tarantula(e_p, n_p, e_f, n_f):
    f = e_f/n_f
    p = e_p/n_p
    return f/(p+f)

def Jaccard(e_p, n_p, e_f, n_f):
    return e_f/(e_p + n_f)
