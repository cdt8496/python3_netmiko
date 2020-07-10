from netmiko import ConnectHandler

vios_l2 = {
    'device_type':'cisco_ios',
    'ip':'172.16.175.81',
    'username':'cisco',
    'password':'cisco',
}

net_connect = ConnectHandler(**vios_l2)

config_commands = ['ip routing']
config_commands = ['int G1/0','no switchport','ip address 200.1.1.10 255.255.255.0','no shut']
output = net_connect.send_config_set(config_commands)
print(output)
config_commands = ['int G1/1','no switchport','ip address 200.1.2.10 255.255.255.0','no shut']
output = net_connect.send_config_set(config_commands)
print(output)
config_commands = ['int G1/2','no switchport','ip address 200.1.3.10 255.255.255.0','no shut']
output = net_connect.send_config_set(config_commands)
print(output)
