from netmiko import ConnectHandler

IOSv = {
    'device_type':'cisco_ios',
    'ip':'172.16.175.73',
    'username':'cisco',
    'password':'cisco',
}

net_connect = ConnectHandler(**IOSv)

config_commands = ['int loop 3','ip address 3.3.3.3 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['int tunnel 3','ip address 10.10.0.3 255.255.255.0',
                   'no ip redirects','ip mtu 1400','ip nhrp authentication cisco123',
		   'ip nhrp map multicast 200.1.3.3','ip nhrp map 10.10.0.1 200.1.1.1',
		   'ip nhrp network-id 3','ip nhrp nhs 10.10.0.1','ip nhrp shortcut',
		   'ip tcp adjust-mss 1360','tunnel source 200.1.3.3',
		   'tunnel destination 200.1.1.1']

output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['router eigrp CHARLES','address-family ipv4 unicast autonomous-system 5',
                   'af-interface default','passive-interface','af-interface tunnel 3',
		   'no passive-interface','network 10.10.0.3 255.255.255.255',
		   'network 3.3.3.3 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['ip route 200.1.1.1 255.255.255.255 200.1.3.10',
                   'ip route 200.1.2.2 255.255.255.255 200.1.3.10']
output = net_connect.send_config_set(config_commands)
print(output)
