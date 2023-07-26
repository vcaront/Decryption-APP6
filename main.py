if __name__ == '__main__':
    n_public = 86062381025757488680496918738059554508315544797
    e_public = 13
    print("hello world")


    # étape1 trouver P,Q de N et le e tout en haut avec polar
    def pgcd(a, b):
        if b == 0:
            return a
        else:
            r = a % b
            return pgcd(b, r)


    def rho_pollard(n):
        def f(x):
            return x * x + 1
        x = 2
        y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            print(x, y)
            d = pgcd(x-y, n)
        return d

    p = rho_pollard(n_public)
    print(p)
    q = n_public / p
    print(q)
    # étape2 trouver phi de n = (p-1)(q-1)
    # étape3 trouver d d = inverse e ....
    # étape4 décryper G P Q avec le d trouver
    # note g est potentiellment mauvais
    # étape5 trouver xy de G^xy 0,1,-1 peut-être
    # étape6 déchiffre le document par flux
    # étape7 décryperter le salaire avec le N et e publique avec la méthode. méthode p-1
