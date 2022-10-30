import json
import time

path = 'Staff.json'
with open(path, 'r', encoding='utf-8') as f:
    jsondata = json.loads(f.read())

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
values = [tuple(jsondata[d].values()) + (t,) for d in jsondata]

print(values)

for i, r in enumerate(values):

    delete from TESTDB.Staff;
    insert into TESTDB.Staff
    values
    ('001', 'Mike', '002', 45, 'M', '60000', '2022-10-30 15:26:23'),
    ('002', 'Judy', '002', 30, 'F', '48000', '2022-10-30 15:26:23'),
    ('003', 'Allen', '001', 22, 'M', '50000', '2022-10-30 15:26:23'),
    ('004', 'Tom', '002', 47, 'M', '47000', '2022-10-30 15:26:23'),
    ('005', 'Jack', '003', 36, 'M', '52000', '2022-10-30 15:26:23'),
    ('006', 'Abby', '002', 24, 'F', '45000', '2022-10-30 15:26:23'),
    ('007', 'Trump', '001', 80, 'M', '80000', '2022-10-30 15:26:23'),
    ('008', 'Marry', '003', 29, 'F', '87000', '2022-10-30 15:26:23');
