import os

root = os.getcwd().replace("\\","/")
root = root.split('/scripts')[0]

config_1 = None
config_2 = None
config_3 = None
config_4 = None

httpd_config_path = "../Apache24/conf/httpd.conf"
begin = True

with open('config_1.dat', 'r') as f:
    config_1 = f.read().format(root)
with open('config_2.dat', 'r') as f:
    config_2 = f.read()
with open('config_3.dat', 'r') as f:
    config_3 = f.read().format(root)
with open('config_4.dat', 'r') as f:
    config_4 = f.read().format(root)

def update_part_config(config):
    global httpd_config_path, begin
    flag = 'a'
    if begin:
        flag = 'w'
        begin = False
    with open(httpd_config_path, flag) as f:
        f.write(config)

update_part_config(config_1)
update_part_config(config_2)
update_part_config(config_3)
update_part_config(config_4)
