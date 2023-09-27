#ingrese una distancia en metros
distancia = float(input())

# velocidad de la luz =  299792458 m/s 
t_vLuz = distancia/299792458
print("El tiempo que le tomaría a la luz recorrer",distancia,"metros es:",t_vLuz,"segundos")

# velocidad del sonido en el aire = 343.2 m/s (1235.5 km/h)
t_vSonido = distancia/343.2
print("El tiempo que le tomaría al sonido recorrer",distancia,"metros es:",t_vSonido,"segundos")

# velocidad del vehiculo comercial más veloz (SSC Tuatara) = 141.111 m/s (508 km/h)
t_vAuto = distancia/141.111
print("El tiempo que le tomaría al vehiculo comercial más veloz recorrer",distancia,"metros es:",t_vAuto,"segundos")

# velocidad de Usain Bolt = 11.6667 m/s (42 km/h)
t_vBolt = distancia/11.6667
print("El tiempo que le tomaría a Bolt recorrer",distancia,"metros es:",t_vBolt,"segundos")