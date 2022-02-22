import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
import json


'''
   Database for managing books. It allows to add, delete, search and sort books in database, by keys: author, title
   or numer of pages.
'''


# Jesli w folderze znajduje sie baza danych w pliku .json, to ja wczytuje
# jesli nie ma, to tworzy nowa
try:
    with open('books.json') as f:
        data = json.load(f)
except:
    ksiazki = '''
     {
      "books": [
      ]
    }
    '''
    data = json.loads(ksiazki)
    with open('books.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)


# Zapisuje zmiany do pliku
def zapisywanie(data, filename='new_books.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


# Funkcja pozwalajaca na dodanie ksiazki do bazy
def dodawanie():
    temp = data['books']
    nowa_ksiazka = {'title': str(title.get()), 'author': author.get(), 'pages': pages.get()}
    temp.append(nowa_ksiazka)
    zapisywanie(data)
    msgbox.showinfo('Udalo sie', 'Pomyslnie dodano ksiazke')
    author.delete(0, tk.END)
    title.delete(0, tk.END)
    pages.delete(0, tk.END)


# Funkcja wypisujaca zawartosc bazy danych, posortowana wzgledem wybranego parametru
def sortowanie():
    if zmienna_check.get():
        reverse = True
    else:
        reverse = False
    sortownia = []
    temp_wart = zmienna_sort.get()
    if temp_wart == 1:
        parametr = 'title'
    elif temp_wart == 2:
        parametr = 'author'
    elif temp_wart == 3:
        parametr = 'pages'
    for i in range(len(data['books'])):
        x = data['books'][i][parametr]
        y = (x, i)
        sortownia.append(y)
    sortownia.sort(reverse=reverse)
    for i in range(len(sortownia)):
        print(sortownia[i][0], end=' ')
        print(data['books'][sortownia[i][1]])


# Funkcja usuwajaca ksiazke o podanym parametrze
def usuwanie():
    if msgbox.askyesno('Usunac?', 'Jestes pewien, ze chcesz usunac?'):
        temp_wart = zmienna_usuwanie.get()
        if temp_wart == 1:
            parametr = 'title'
        elif temp_wart == 2:
            parametr = 'author'
        elif temp_wart == 3:
            parametr = 'pages'

        wartosc = parametr_usuwany.get()
        flag = True                 # Jesli w bazie nie ma ksiazki o takim parametrze, to wyrzuca monit
        for i in range(len(data['books'])):
            if data['books'][i][parametr] == wartosc:
                flag = False
                usuniete = data['books'].pop(i)
                print('Usunieto ' + str(usuniete) + '\n')
                msgbox.showinfo('Usunieto', 'Pomyslnie usunieto' + str(usuniete))
                parametr_usuwany.delete(0, tk.END)

        if flag is True:
            msgbox.showinfo('Nie ma takiej ksiazki!', 'Nie mozna usunac - nie ma ksiazki o takiej wartosci')

        zapisywanie(data)
    else:
        msgbox.showinfo('Anulowano', 'Anulowano usuwanie')


# Funkcja wypisujaca wszystkie ksiazki o podanym parametrze
def wyszukiwanie():
    temp_wart = zmienna_szukanie.get()
    if temp_wart == 1:
        parametr = 'title'
    elif temp_wart == 2:
        parametr = 'author'
    elif temp_wart == 3:
        parametr = 'pages'

    wartosc = parametr_szukany.get()
    flag = True
    for i in range(len(data['books'])):
        if data['books'][i][parametr] == wartosc:
            print(data['books'][i])
            flag = False

    if flag is True:
        msgbox.showinfo('Nie ma takiej ksiazki!', 'Nie mozna usunac - nie ma ksiazki o takiej wartosci')


# Tworzenie glownego okna
win = tk.Tk()
win.title('Baza Danych - Ksiazki')
win.geometry('350x300')
tabControl = ttk.Notebook(win)                                            # Kontroler zakladek

tab_dodawanie = ttk.Frame(tabControl)                                     # Tworzenie zakladek
tabControl.add(tab_dodawanie, text='Dodawanie')

tab_usuwanie = ttk.Frame(tabControl)
tabControl.add(tab_usuwanie, text='Usuwanie')

tab_wyszukiwanie = ttk.Frame(tabControl)
tabControl.add(tab_wyszukiwanie, text='Wyszukiwanie')

tab_sort = ttk.Frame(tabControl)
tabControl.add(tab_sort, text='Sortowanie')

tabControl.pack(expand=1, fill='both')

author = tk.Entry(tab_dodawanie, width=30)                                  # Pola do wpisywania wraz etykietami
author.grid(row=0, column=1, pady=(20, 0), padx=20)
author_label = tk.Label(tab_dodawanie, text='Autor:')
author_label.grid(row=0, column=0, pady=(20, 10), padx=20)

title = tk.Entry(tab_dodawanie, width=30)
title.grid(row=1, column=1, padx=10)
title_label = tk.Label(tab_dodawanie, text='Tytul:')
title_label.grid(row=1, column=0, padx=10,  pady=10)

pages = tk.Entry(tab_dodawanie, width=30)
pages.grid(row=2, column=1, padx=10)
pages_label = tk.Label(tab_dodawanie, text='Liczba stron:')
pages_label.grid(row=2, column=0, padx=10, pady=10)

parametr_usuwany = tk.Entry(tab_usuwanie, width=30)
parametr_usuwany.grid(row=0, column=1, pady=20)
usuwany_label = tk.Label(tab_usuwanie, text='Wartosc:')
usuwany_label.grid(row=0, column=0, pady=20, padx=(20, 0))

parametr_szukany = tk.Entry(tab_wyszukiwanie, width=30)
parametr_szukany.grid(row=0, column=1, pady=20, padx=20, sticky=tk.W)
szukany_label = tk.Label(tab_wyszukiwanie, text='Wartosc: ')
szukany_label.grid(row=0, column=0, pady=20, padx=(20, 0))

sort_label = tk.Label(tab_sort, text='Wybierz po jakim parametrze chcesz posortowac ')
sort_label.grid(row=0, column=0, pady=20, padx=(40, 10), columnspan=3)
                                                                            # Tworzenie radiobuttonow do wybierania
                                                                            # jakiego parametru ma dotyczyc wpisana
                                                                            # wartosc
zmienna_usuwanie = tk.IntVar()
usuwanie_tytul = tk.Radiobutton(tab_usuwanie, text='Tytul', variable=zmienna_usuwanie, value=1)
usuwanie_tytul.grid(row=2, column=0, sticky=tk.W, padx=(20, 0))
usuwanie_autor = tk.Radiobutton(tab_usuwanie, text='Autor', variable=zmienna_usuwanie, value=2)
usuwanie_autor.grid(row=3, column=0, sticky=tk.W, padx=(20, 0))
usuwanie_pages = tk.Radiobutton(tab_usuwanie, text='Liczba stron', variable=zmienna_usuwanie, value=3)
usuwanie_pages.grid(row=4, column=0, sticky=tk.W, padx=(20, 0))

zmienna_szukanie = tk.IntVar()
szukanie_tytul = tk.Radiobutton(tab_wyszukiwanie, text='Tytul', variable=zmienna_szukanie, value=1)
szukanie_tytul.grid(row=2, column=0, sticky=tk.W, padx=(20, 0))
szukanie_autor = tk.Radiobutton(tab_wyszukiwanie, text='Autor', variable=zmienna_szukanie, value=2)
szukanie_autor.grid(row=3, column=0, sticky=tk.W, padx=(20, 0))
szukanie_pages = tk.Radiobutton(tab_wyszukiwanie, text='Liczba stron', variable=zmienna_szukanie, value=3)
szukanie_pages.grid(row=4, column=0, sticky=tk.W, padx=(20, 0))

zmienna_sort = tk.IntVar()
sortowanie_tytul = tk.Radiobutton(tab_sort, text='Tytul', variable=zmienna_sort, value=1)
sortowanie_tytul.grid(row=1, column=0, padx=(40, 10), sticky=tk.W)
sortowanie_autor = tk.Radiobutton(tab_sort, text='Autor', variable=zmienna_sort, value=2)
sortowanie_autor.grid(row=2, column=0, padx=(40, 10), sticky=tk.W)
sortowanie_pages = tk.Radiobutton(tab_sort, text='Liczba stron', variable=zmienna_sort, value=3)
sortowanie_pages.grid(row=3, column=0, padx=(40, 10), sticky=tk.W)

                                                                            # Tworzenie buttonow do zatwierdzania i
                                                                            # wykonywania funkcji zdeklarowanych
                                                                            # na poczatku kodu
button_dodawanie_szeroki = tk.Button(tab_dodawanie, text='Kliknij aby dodac', command=dodawanie)
button_dodawanie_szeroki.grid(row=5, column=1, pady=10, ipadx=50)

button_usuwanie_szeroki = tk.Button(tab_usuwanie, text=' Kliknij aby usunac', command=usuwanie)
button_usuwanie_szeroki.grid(row=5, column=1, pady=10, ipadx=50)

button_wyszukiwanie_szeroki = tk.Button(tab_wyszukiwanie, text='Kliknij aby wyszukac', command=wyszukiwanie)
button_wyszukiwanie_szeroki.grid(row=5, column=1, pady=10, ipadx=50)

button_sortowanie_szeroki = tk.Button(tab_sort, text='Kliknij aby posortowac', command=sortowanie)
button_sortowanie_szeroki.grid(row=10, column=0, pady=10, padx=(40, 10), ipadx=50, columnspan=2)

zmienna_check = tk.IntVar()
check_sort = tk.Checkbutton(tab_sort, text='Malejaco', variable=zmienna_check)
check_sort.deselect()
check_sort.grid(row=1, column=1, padx=20)

author.focus()
win.mainloop()
