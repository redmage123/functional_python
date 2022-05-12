f = open('c:/users/bbrel/basicpython/labs/lab4/data/ALbb.salaries.2003.formatted.csv')
team_dict = {}

def read_file(f):
    while f:
        line = f.readline()
        if len(line) == 4:
            break
        else:
            yield line.strip().split(',')

def build_items(seq):
    for l in seq:
        yield (l[0],l[3])

def build_dict(items):
    while items:
        try:
            (key,value) = next(items)
        except StopIteration:
            break
        if key not in team_dict:
            team_dict[key] = int(value)
        else:
            team_dict[key] += int(value)
        yield team_dict




pipeline  = build_dict(build_items(read_file(f)))

for team_dict in pipeline:
    pass

print (team_dict)
