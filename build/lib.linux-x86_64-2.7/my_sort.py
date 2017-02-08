import pdb

def sortowanie_babelkowe(napis):
    if not isinstance(napis, str):
        raise TypeError('Napis musi byc stringiem!')

    lista_liter = list(napis)

    pdb.set_trace()
    for po_lewej in range(len(lista_liter) - 1, 0, -1):
        for indeks in range(po_lewej):
            if lista_liter[indeks] > lista_liter[indeks + 1]:
                lista_liter[indeks], lista_liter[indeks + 1] = lista_liter[indeks + 1], lista_liter[indeks]
    return ''.join(lista_liter)


def sortowanie_przez_wstawianie(napis):
    if not isinstance(napis, str):
        raise TypeError('Napis musi byc stringiem!')

    lista_liter = list(napis)

    for indeks in range(1, len(lista_liter)):
        usun = lista_liter[indeks]
        insert_indeks = indeks
        while insert_indeks > 0 and lista_liter[insert_indeks - 1] > usun:
            lista_liter[insert_indeks] = lista_liter[insert_indeks - 1]
            insert_indeks = insert_indeks - 1
        lista_liter[insert_indeks] = usun
    return ''.join(lista_liter)


def szybkie_sortowanie(napis):
    if not isinstance(napis, str):
        raise TypeError('Napis musi byc stringiem!')

    lista_liter = list(napis)

    if len(lista_liter) <= 1:
        return lista_liter
    p = lista_liter.pop()
    lewa_lista = [a for a in lista_liter if a < p]
    prawa_lista = [a for a in lista_liter if a >= p]

    lewy_napis = ''.join(lewa_lista)
    prawy_napis = ''.join(prawa_lista)

    return szybkie_sortowanie(lewy_napis) + [p] + szybkie_sortowanie(prawy_napis)
