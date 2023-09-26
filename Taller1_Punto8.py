frec = float(input())

if frec < 30E3:
    print("Muy Baja Frecuencia - Radio")
    
elif  30E3 <= frec < 650E3:
    print("Onda Larga - Radio")
    
elif  650E3 <= frec < 1.7E6 :
    print("Onda Media - Radio")
#
elif  1.7E6 <= frec < 30E6 :
    print("Onda Corta - Radio")

elif  30E6 <= frec < 300E6 :
    print("Muy Alta Frecuencia-Radio")
    
elif  300E6 <= frec < 3E8 :
    print("Ultra Alta Frecuencia-Radio")
    
elif  3E8 <= frec < 300E9 :
    print("Microondas")
    
elif  300E9 <= frec < 6E12 :
    print("Infrarrojo lejano/submilimétrico")
    
elif  6E12 <= frec < 120E12 :
    print("Infrarrojo medio")
    
elif  120E12 <= frec < 384E12 :
    print("Infrarrojo cercano")
    
elif  384E12 <= frec < 7.89E14 :
    print("Espectro Visible")
    
elif  7.89E14 <= frec < 1.5E15 :
    print("Ultravioleta cercano")
    
elif  1.5E15 <= frec < 30E15 :
    print("Ultravioleta extremo")
    
elif  30E15 <= frec < 30E18 :
    print("Rayos X")
    
elif  30E18 <= frec :
    print("Rayos gamma")
