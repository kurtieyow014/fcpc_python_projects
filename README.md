S1 
ena
conf t
hostname S1
no ip domain-lookup
vlan 10 
name STUDENT 
vlan 20
name TEACHER 
exit
interface fa0/1
switchport mode access 
switchport access vlan 10
exit
interface fa0/5
switchport mode access 
switchport access vlan 20
exit
interface fa0/24
switchport mode trunk
switchport trunk native vlan 50
switchport trunk allowed vlan 10,20,30,40,50
end 
write mem


S2 
ena
conf t
hostname S2
no ip domain-lookup
vlan 30 
name INSTRUCTOR 
vlan 40
name PROFESSOR
exit
interface fa0/1
switchport mode access 
switchport access vlan 10
exit
interface fa0/5
switchport mode access 
switchport access vlan 20
exit
interface fa0/24
switchport mode trunk
switchport trunk native vlan 50
switchport trunk allowed vlan 10,20,30,40,50
end 
write mem
