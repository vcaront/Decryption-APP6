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


# soustraire 2 listes
def soustraire(liste1, liste2):
    liste = liste1
    for i in range(len(liste1)):
        liste[i] = liste1[i] - liste2[i]
    return liste


# multiplier les éléments d'une liste par un scalaire
def multiplier(liste, scalaire):
    new_liste = []
    for i in range(len(liste)):
        new_liste.append(scalaire * liste[i])
    return new_liste


# fonction pour trouver d à partir de lambda de n et e
def trouver_d(lambda_de_n, e):
    nombre1 = lambda_de_n
    composition1 = [1, 0]
    nombre2 = e
    composition2 = [0, 1]
    reste = nombre1 % nombre2
    composition_reste = soustraire(composition1, multiplier(composition2, nombre1 // nombre2))
    while reste > 1:
        nombre1 = nombre2
        composition1 = composition2
        nombre2 = reste
        composition2 = composition_reste
        reste = nombre1 % nombre2
        composition_reste = soustraire(composition1, multiplier(composition2, nombre1 // nombre2))

    if composition_reste[1] < 0:
        return lambda_de_n + composition_reste[1]
    else:
        return composition_reste[1]


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


def decrypter(message_chiffre, d, n):
    message_decrypte = pow(message_chiffre, d, n)
    return message_decrypte


def phi_indicatrice_euler(n, facteurs):
    indicatrice = n
    for x in facteurs:
        indicatrice *= Fraction(x-1, x)
    return indicatrice


if __name__ == '__main__':
    # variables importantes
    n_public = 86062381025757488680496918738059554508315544797
    e_public = 13

    n_pour_dh = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    e_pour_dh = 1009

    qdh_chiffre_avec_RSA = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    pdh_chiffre_avec_RSA = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
    gdh_chiffre_avec_RSA = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308

    # Test d avec valeurs procédurale 1 exercice 3
    d = trouver_d(37038, 5)
    print("d : ------------------")
    print(d)

    # étape1 trouver P,Q de N et le e tout en haut avec Pollard

    factorP = pollard(n_pour_dh)
    print("P : ------------------------")
    print(factorP)
    factorQ = Fraction(n_pour_dh, factorP)
    print("Q : ------------------------")
    print(factorQ)

    # étape2 trouver phi de n = (p-1)(q-1)

    phi_de_n = (factorP - 1) * (factorQ - 1)
    print("Phi de n : ------------------------")
    print(phi_de_n)

    # étape3 trouver d d = inverse e ....

    lambda_de_n = int(phi_de_n / 2)
    print("Lambda de n : ------------------------")
    print(lambda_de_n)

    print("d : ------------------------")
    d = trouver_d(lambda_de_n, e_pour_dh)
    print(d)

    # étape4 décryper G P Q avec le d trouver

    qdh_chiffre_dechiffrer = decrypter(qdh_chiffre_avec_RSA, d, n_pour_dh)
    print("dechiffre q")
    print(qdh_chiffre_dechiffrer)

    gdh_chiffre_dechiffrer = decrypter(gdh_chiffre_avec_RSA, d, n_pour_dh)
    print("dechiffre g")
    print(gdh_chiffre_dechiffrer)

    pdh_chiffre_dechiffrer = decrypter(pdh_chiffre_avec_RSA, d, n_pour_dh)
    print("dechiffre p")
    print(pdh_chiffre_dechiffrer)


    # notre g est potentiellement mauvais ( g = p - 1)

    # étape 5 trouver xy de G^xy 0,1,-1 peut-être
    # g^xy mod p = 1 ou p - 1

    # étape6 déchiffre le document par flux

    # étape7 décrypter le salaire avec le N et e public avec la méthode p-1
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
            d = pgcd(x - y, n)
        return d


    p_public = rho_pollard(n_public)
    print("P clé publique : ------------------")
    print(p_public)
    q_public = Fraction(n_public, p_public)
    print("Q clé publique : ------------------")
    print(q_public)
    print("Q clé publique n'est pas premier")
    q_public_fact1 = 1200001573
    q_public_fact2 = 1800002359
    q_public_fact3 = 66405897020462343733
    facteurs_de_n_public = [p_public, q_public_fact1, q_public_fact2, q_public_fact3]
    phi_de_n_public = phi_indicatrice_euler(n_public, facteurs_de_n_public)
    print("Phi de n public : ------------")
    print(phi_de_n_public)

    d = 33100915677995941255459401914535119858511166597

    salaire_Alain_crypte = 81530476374664351124876242644701327168836407987
    salaire_Michele_crypte = 83740877821201430552252653974153238737996745098
    salaire_Stephanie_crypte = 51373667846507963545859239582447701017826406175
    salaire_Fernand_crypte = 61167846837720209456441528754183777549647735855
    salaire_Angele_crypte = 42340513171888188994504759277496496710896088718
    salaire_Bernard_crypte = 65069303637151076134861115122997306654987857614
    salaire_Claude_crypte = 32785990179062766920584737848735367794508677603

    salaire_Alain = decrypter(salaire_Alain_crypte, d, n_public)
    print("Salaire de Alain")
    print(salaire_Alain)

    salaire_Michele = decrypter(salaire_Michele_crypte, d, n_public)
    print("Salaire de Michele")
    print(salaire_Michele)

    salaire_Stephanie = decrypter(salaire_Stephanie_crypte, d, n_public)
    print("Salaire de Stephanie")
    print(salaire_Stephanie)

    salaire_Fernand = decrypter(salaire_Fernand_crypte, d, n_public)
    print("Salaire de Fernand")
    print(salaire_Fernand)

    salaire_Angele = decrypter(salaire_Angele_crypte, d, n_public)
    print("Salaire de Angele")
    print(salaire_Angele)

    salaire_Bernard = decrypter(salaire_Bernard_crypte, d, n_public)
    print("Salaire de Bernard")
    print(salaire_Bernard)

    salaire_Claude = decrypter(salaire_Claude_crypte, d, n_public)
    print("Salaire de Claude")
    print(salaire_Claude)




