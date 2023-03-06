birthdays = {'Chidiebere' : 'March 4',
            'Pastor Enoch Adeboye' : 'March 3',
            'victor Imeh':'March 3',
            'Reuben Peter':'March 4',
            'Stephanie':'January 10',  'Lily-Precious':'August 14',
            'Rev Godswill Umanah':'Feb 6', 
            'Sr. Alpheus':'October 2', 
            'Miss Rebecca Ikpe':'Dec 3', 
            'Miss Emem Bassey':'August 13',
            'Utibeabasi Umanah':'August 9',
            'Atada Joseph':'',
            'Godstime Godswill':'January 16',
            'Aunty Victoria Udoette':' January 12',
            'Uncle Abraham Umanah':'',
            'Uncle Ufot Umanah':'',
            'Aunty Monique':'',
            'Godswill Godswill':'August',
            'Emmanuel P':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':''}

while True:
    print('Enter a name: (blank to quit) ')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + '_____is the birthday of ' + name + ' because the are no values for this person stored in the database.')
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')