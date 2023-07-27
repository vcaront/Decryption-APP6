import math

if __name__ == '__main__':
    n_public = 86062381025757488680496918738059554508315544797
    e_public = 13

    n_pour_dh = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    e_pour_dh = 1009

    qdh_chiffre_avec_RSA = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    pdh_chiffre_avec_RSA = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
    gdh_chiffre_avec_RSA = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308

    print("hello world")


    # étape1 trouver P,Q de N et le e tout en haut avec polar
    def isprime(n):
        n = 9
        flag = 0
        if n > 1:
            for k in range(2, int(math.sqrt(n)) + 1):
                if n % k == 0:
                    flag = 1
                break
            if flag == 0:
                return True
            else:
                return False
        else:
            return False


    """ Implementation of the pollard p-1 algorithm to find prime factors of the number"""


    def pollardPMO(n):
        a = 2
        i = 2
        """ continue operation till a prime factor is obtained """
        while True:
            a = (a ** i) % n
            d = math.gcd((a - 1), n)
            """check if factor obtained"""
            if d > 1:
                """factor found, return it"""
                return d
                break
            """ exponent increment """
            i += 1


    n = n_pour_dh
    """temporarily storing n"""
    num = n
    """list for storing prime factors of the number"""
    res = []
    """iterated till all prime factors are obtained"""
    while True:
        d = pollardPMO(num)
        """ adding the prime number to the result array """
        res.append(d)
        """ exhausting the provided number """
        r = int(num / d)
        """ primality check """
        if isprime(r):
            """inserting the prime factor"""
            res.append(r)
            break
        else:
            num = r

    print("Factors of the number:", n, "are", *res)
    # étape2 trouver phi de n = (p-1)(q-1)
    # étape3 trouver d d = inverse e ....
    # étape4 décryper G P Q avec le d trouver
    # note g est potentiellment mauvais
    # étape5 trouver xy de G^xy 0,1,-1 peut-être
    # étape6 déchiffre le document par flux
    # étape7 décryperter le salaire avec le N et e publique avec la méthode. méthode p-1
