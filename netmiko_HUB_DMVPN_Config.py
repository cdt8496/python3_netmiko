from netmiko import ConnectHandler

IOSv = {
    'device_type':'cisco_ios',
    'ip':'172.16.175.71',
    'username':'cisco',
    'password':'cisco',
}

net_connect = ConnectHandler(**IOSv)

config_commands = ['int loop 1','ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['int tunnel 1','ip address 10.10.0.1 255.255.255.0',
                   'no ip redirects','ip mtu 1400','ip nhrp authentication cisco123',
		   'ip nhrp network-id 1','ip nhrp redirect','ip tcp adjust-mss 1360',
		   'tunnel source 200.1.1.1','tunnel mode gre multipoint']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['router eigrp CHARLES','address-family ipv4 unicast autonomous-system 5',
                   'af-interface default','passive-interface','af-interface tunnel 1',
		   'no passive-interface','no split-horizon','network 10.10.0.1 255.255.255.255',
		   'network 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['ip route 200.1.2.2 255.255.255.255 200.1.1.10',
                   'ip route 200.1.3.3 255.255.255.255 200.1.1.10']
output = net_connect.send_config_set(config_commands)
print(output)
