albums = [('Eminem', 2000, ['my mom', 'iam not afraid']),
          ('Selena', 2010, ['heart', 'same old love', 'sad']),
          ]# nested tuple

config_list = ['os', 'memory', 'system', 'model', 'year']
config_dict = dict.fromkeys(config_list, ' '); print(config_dict) # make init dict.
config_dict_init={
    'os': 'mac',
    'memory': '16GB',
    'system': '64-bit',
    'os': 'Macintosh',
    'model': None
}
config_dict_init.popitem() #LIFO pop

config_dict.update(config_dict_init); print(config_dict) # update init dict.

# dicctionary
project = {
    '1': 'fsr',
    '2' : 'tact'
}
project_tect_stack = {
    'fsr': ['java', 'angular', 'spring-boot', 'hibernate', 'rest-api'],
    'tact': ['java', 'jsp', 'thyme-leaf']
}

related_project = {
    'java': ['CSTAR'],
    'angular': ['CARS']
}

# suitable keys for dict - immutable, and hashable
t1 = 'java',10,2020;  t3 = 'nodeJs','10',2020
t2 = 'python',3,[2020, 2021]  # TypeError: unhashable type: 'list'
dict1={t1: 'value1', t3: 'value2'}
for k in dict1.keys():print(k[1])


