#the function to calculate the coefficent
def approx(x, y, n, w):
    x = np.matrix(x).transpose()
    y = np.matrix(y).transpose()

    f, b = x.shape
    c, d = y.shape

    if c != f or b != d:
        print('The Input vector have wrong dimension')
        return -1

    j = np.matrix(np.arange(1,n+1))
    V1 = np.cos(w*x*j)
    j = np.matrix(np.arange(n+1,2*n+1))
    V2 = np.sin(w*x*(j-n))

    V = np.concatenate([V1,V2],axis=1)

    Q, R = linalg.qr(V)

    R = R[:2 * n, :2 * n]
    Q = Q[:f, :2 * n]
    # coeff = linalg.solve_triangular(R, (np.dot(Q.transpose(), y)),check_finite=False)
    coeff = linalg.solve_triangular(R, (np.dot(Q.transpose(), y)))

    n = int(len(coeff) / 2)
    mag = np.sqrt(coeff[:n]**2+coeff[n:]**2)
    angle = np.arctan2(coeff[:n],coeff[n:])

    r = []
    for i,(m,a) in enumerate(zip(mag,angle)):
        r.append([float(m),i+1,float(a)])
    return r

#the function to calculate the reconstructed function from the coefficent
def calc_fourier(X,coeff,vmed,w=0.5):
    y = np.zeros_like(X) + vmed
    for (m,i,p) in coeff:
            y += m*np.sin(w*i*X+p)
    return y

#approx a function and get both the coefficent and the reconstructed function
def fourier_approx(funzione,n=0,w=0.5):

    fmean = np.mean(funzione)

    funzione = list(funzione)

    funzione = funzione + funzione[::-1]

    mean = np.mean(funzione)

    funzione = [z - mean for z in funzione]

    T = np.linspace( 0, 4 * np.pi, num=len(funzione), endpoint=True)
    if n == 0:
        n = int(len(T) / 2) - 1

    if n < 1:
        return -1

    coeff = approx(T, funzione, n, w)

    T =  np.array(T [:int(len(T)/2)])
    funzione =  np.array(funzione [:int(len(funzione)/2)])

    y = calc_fourier(T,coeff[:index+1],0)

    return y,coeff