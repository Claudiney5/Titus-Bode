import tb_law
from csv import DictReader


with open('compositepars.csv') as data:
    reader_plan = DictReader(data)  # for each line a dict of a planet

    # cleaning data ------------------------------------------------
    system = {}  # dict of dicts
    list_sys = []
    i = 0
    for line in reader_plan:
        list_sys.append(line['fpl_hostname'])
        system[i] = {'name': line['fpl_hostname'], 'planet ' + line['fpl_letter']: line['fpl_letter'], 'dist ' + line['fpl_letter']: line['fpl_smax']}
        i = i + 1

    # list of systems name (only one for each system)---------------
    list_sys = list(set(list_sys))
    list_sys.sort()

    # creating a planet list --------------------------------------
    planets = list(system.values())

    # creating a dict with systems assembled -----------------------------
    j = 0
    sys_work = {}
    for name in list_sys:
        sys_work[name] = {}

        for j in range(0, i):
            if name == planets[j]['name']:
                sys_work[name].update(planets[j])
    print(sys_work)
    print(system)
