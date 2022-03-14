# melihat representasi string JSON dengan sebaris kode
import json
x = [1, 'simple', 'list']
json.dumps(x)

json.dump(x, f)

# memecahkan kode obje
x = json.load(f)