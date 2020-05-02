from csv import DictReader

with open('compositepars.csv') as data:
    reader_plan = DictReader(data)  # cada linha uma lista

    system = {}  # dict of dicts
    list_sys = []
    i = 0
    for line in reader_plan:
        list_sys.append(line['fpl_hostname'])
        system[i] = {'name': line['fpl_hostname'], 'planet ' + line['fpl_letter']: line['fpl_letter'], 'dist ' + line['fpl_letter']: line['fpl_smax']}
        i = i + 1

    list_sys = list(set(list_sys))
    list_sys.sort()

    sys_work = {}
    i = 0
    for name in list_sys:
        sys_work[name] = {'name': name}

    for line in system:
        for name in list_sys:
            if name == system[line]['name']:
                sys_work[name] = sys_work[name].update(system[line])

        print(sys_work)


''' for n in range(0, i):
        try:
            system[n]['planet b'] == 'planet b'
            for m in range(n + 1, i):
                if system[n]['name'] == system[m]['name']:
                    print(system[n].update(system[m]))
        except:
            pass
'''



