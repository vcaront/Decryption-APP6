import random
import math

import numpy as np
import sympy
from fractions import Fraction



def ppcm(a, b):
    # Calculer le PGCD en utilisant math.gcd()
    pgcd = np.gcd(a, b)

    # Calculer le PPCM en utilisant la formule
    ppcm = (a * b) // pgcd

    return ppcm
# function to generate
# prime factors
def pollard(n):
    # defining base
    a = 2

    # defining exponent
    i = 2

    # iterate till a prime factor is obtained
    while (True):

        # recomputing a as required
        a = (a ** i) % n

        # finding gcd of a-1 and n
        # using math function
        d = math.gcd((a - 1), n)

        # check if factor obtained
        if (d > 1):
            # return the factor
            return d

            break

        # else increase exponent by one
        # for next round
        i += 1


# Driver code
n = 1403

# temporarily storing n
num = n

# list for storing prime factors
ans = []

# iterated till all prime factors
# are obtained
while (True):

    # function call
    d = pollard(num)

    # add obtained factor to list
    ans.append(d)

    # reduce n
    r = int(num / d)

    # check for prime using sympy
    if sympy.isprime(r):

        # both prime factors obtained
        ans.append(r)

        break

    # reduced n is not prime, so repeat
    else:

        num = r

# print the result
print("Prime factors of", n, "are", *ans)

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
    # factor = pollard_rho(n_pour_dh)
    # factor = pollard_p_minus_1(n_pour_dh)
    factorP = pollard(n_pour_dh)
    print("P : ------------------------")
    print(factorP)
    factorQ = Fraction(n_pour_dh, factorP)
    # n_pour_dh / factorP
    print("Q : ------------------------")
    print(factorQ)

    PhiN = (factorP-1)*(facttorq-1)
    print("PhiN")
    print(PhiN)

    print("ppcm")
    ppcm = ppcm((factorP-1),(facttorq-1))
    print(ppcm)

    # a valider
    LamdaN = Fraction(PhiN,ppcm)
    print("lamdaN")
    print(LamdaN)



    # étape2 trouver phi de n = (p-1)(q-1)

    phi_de_n = (factorP - 1) * (factorQ - 1)
    print("Phi de n : ------------------------")
    print(phi_de_n)
    # étape3 trouver d d = inverse e ....
    delta_de_n = int(phi_de_n / 2)
    print("Delta de n : ------------------------")
    print(delta_de_n)
    # étape4 décryper G P Q avec le d trouver
    # note g est potentiellment mauvais
    # étape5 trouver xy de G^xy 0,1,-1 peut-être
    # étape6 déchiffre le document par flux
    # étape7 décryperter le salaire avec le N et e publique avec la méthode. méthode p-1
