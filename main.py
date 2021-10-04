def get_leap_years(start, end):
    #returneaza o lista de intregi cu toti anii bisecti din intervalul [start, end]
    lista = []
    if start > end:
        aux = start
        start = end
        end = aux
    for an in range(start , end + 1):
        if an % 4 == 0 and an % 100 != 0:
            lista.append(an)
        if an % 400 == 0:
            lista.append(an)
    return lista
        

def test_get_leap_years():
    assert get_leap_years(2000, 2004) == [2000, 2004]
    assert get_leap_years(1998, 2008) == [2000, 2004, 2008]
    assert get_leap_years(2100, 2105) == [2104]
    assert get_leap_years(1832, 1874) == [1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872]

def get_perfect_squares(start, end):
    # returneaza o lista de intregi cu toate patratele perfecte cuprinse in intervalul [start, end]
    lista = []
    if start > end:
        aux = start
        start = end
        end = aux
    i = 1
    while i * i <= end:
        if i* i >= start:
            lista.append(i * i)
        i+=1
    return lista

def test_get_perfect_squares():
    assert get_perfect_squares(2, 34) == [4, 9, 16, 25]
    assert get_perfect_squares(63, 100) == [64, 81, 100]
    assert get_perfect_squares(134, 231) == [144, 169, 196, 225]
    assert get_perfect_squares(235, 236) == []
    assert get_perfect_squares(1232, 1643) == [1296, 1369, 1444, 1521, 1600]

def main():
    test_get_leap_years()
    test_get_perfect_squares()
    print('1. Afiseaza toti anii bisecti intre doi ani dati (inclusiv anii dati)')
    print('2. Afiseaza toate patratele perfecte dintr-un interval inchis')
    print('x. inchide aplicatia')
    optiune = input('Selectati actiunea dorita:')
    while optiune != 'x':
        if optiune == '1':
            ani = input('Introduceti anii separati prin spatiu: ').split(' ')
            an_inceput = int(ani[0])
            an_final = int(ani[1])
            lista_ani = get_leap_years(an_inceput, an_final)
            lista_ani_string = ''
            if len(lista_ani) > 0:
                print(f'Anii bisecti cuprinsi intre anii {an_inceput} si {an_final} sunt: ')
                for an in lista_ani:
                    lista_ani_string += str(an) + ' '
                print(lista_ani_string)
            else:
                print(f'Nu exista ani bisecti intre anii {an_inceput} si {an_final}')
        elif optiune == '2':
            interval = input('Introduceti marginile intervalului separate prin spatiu: ').split(' ')
            lim_inf = int(interval[0])
            lim_sup = int(interval[1])
            lista_pp = get_perfect_squares(lim_inf, lim_sup)
            lista_pp_string = ''
            if len(lista_pp) > 0:
                print(f'Patratele perfecte cuprinse intre {lim_inf} si {lim_sup} sunt: ')
                for pp in lista_pp:
                    lista_pp_string += str(pp) + ' '
                print(lista_pp_string)
            else:
                print(f'Nu exista patrate perfecte in intervalul [{lim_inf} ,{lim_sup}]')
        else:
            print('Optiune invalida!')
        optiune = input('Selectati actiunea dorita:')

if __name__ == '__main__':
    main()