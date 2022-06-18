import time


def name_definition():
    name = {}
    if 'bob' not in name:
        name['bob'] = name
    for k in name:
        for k1 in name[k]:
            for k2 in name[k][k1]:
                print(name[k][k1][k2])


name_definition()


def password_dev():
    password = input('tafadhali weka password yako: ')
    rule_number = ['rule1', 'rule2', 'rule3']
    rule = ['wakilisha nambari katika password yako', 'wakilisha majina', 'wakilisha majina na nambari']
    rules_dict = {x: k for (x, k) in zip(rule_number, rule)}
    print('THE RULES/MAAGIZO: ' + str(rules_dict).rjust(20, 'x'))
    while True:
        if password.isalpha():
            print('password haijafuata maagizo kikamilifu: majina tupu')
            break
        elif password.isdecimal():
            print('password haijafuata maagizo kikamilifu: nambari tupu')
            break
        elif password.endswith('123') and password.startswith('Destinne'):
            print('password haijafuata maagizo kikamilifu: hii ni password ya kawaida')
            break
        break
    print('password missing all the above!')


password_dev()

starter = {'njugu': 3, 'kashata': 2, 'jaba': 2, 'chaser': 3}  # this represents a global variables used in two functions


def string_justification(itemsDict, leftwidth, rightwidth):  # key argumaents then make up the local variables
    """string justification is considered during data arrangements"""
    man1 = 'Niaje si tushike jaba leo'
    man2 = 'Poa sana unadai tubuy starter inakaaje?'
    print(man1.rjust(5, '='))
    time.sleep(3)
    print(man2.ljust(5, '*'))
    if itemsDict['jaba'] >= 3:
        print('hio ndo size fiti ya jaba inatutosha sote!')
    else:
        print('Hio size ni kidogo labda tushike tena')

    print('EVENTS ZA SIKU YA JABA'.center(leftwidth + rightwidth))

    starter_ya_jaba = 'njugu'
    ni_ngapi = itemsDict[starter_ya_jaba]  # 'jaba' becomes the returned value in the starter dict
    for start in itemsDict:
        print('ndo hi jaba tools zetu ni gani?')
        time.sleep(2)
        print(f'baadhi ya tools zetu ndo hizi...{start}')
        if start == 'njugu' or start == 'kashata' and start == 'chaser':
            print('tools zote ziko inadi!')
            time.sleep(2)
            return ni_ngapi


string_justification(starter, 10, 5)


def list_ya_jabling(itemsDict, leftwidth, rightwidth):
    print('Jaba Items In Cart'.center(leftwidth + rightwidth))
    for k, v in itemsDict.items():
        print(k.ljust(leftwidth, '-') + str(v).rjust(rightwidth))


list_ya_jabling(starter, 20, 5)
list_ya_jabling(starter, 30, 10)
