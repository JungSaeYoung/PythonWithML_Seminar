txt = ['lamda functions are anonymous functions',
       'anonymous functions dont have a name',
       'functions are objects in Python']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))
# [(True, 'lamda functions are anonymous functions'), (True, 'anonymous functions dont have a name'), (False, 'functions are objects in Python')]