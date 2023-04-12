opcion = int(input("Seleccione la opcion: \n 1.-Configurar una interfaz. \n 2.-Configurar una interfaz y crear ospf"))

if opcion == 1:
    
    interface = input("\nIngrese el numero de interfaz: ")
    ip = input("Ingrese la direccion ip: ")
    mask = input("Ingrese la mascara de subred: ")
    name = input("Ingrese nombre: ")

    print("interface gi0/", interface)
    print("no shut down")
    print("ip address", ip , mask)
    print("Description °°°", name , "°°°")
    print("speed 100")
    print("duplex full")
    print("\nshow ip interface brief")
    print("show run interface gi0/", interface)
    print("show interface gi0/", interface)

else:
    
    interface= input("\ningrese el numero de interfaz: ")
    ip= input("ingrese la direccion ip: ")
    mask= input("ingrese la mascara de subred: ")
    name= input("ingrese nombre: ")
    n_ospf= input("ingrese el numero de proceso de ospf: ")
    n_ospf= str(n_ospf)
    routerif = input("ingrese la id para ospf: ")
    area= input("Ingrese area de ospf: ")
    
    
    print("interface gi0/", interface)
    print("no shut down")
    print("ip address", ip, mask)
    print("Descripcion °°°", name, "°°°")
    print("speed 100")
    print("Duplex full")
    print("\nrouter ospf", n_ospf)
    print("network", ip, mask)
    print("passive-interface gi0/", interface)
    print("\nshow run | section ospf")
    print("show ip ospf neighbor")
    print("show ip interface brief")
    