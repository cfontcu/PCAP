"""
Actividad relacionada con la lección 2
Programa que calcule el sueldo 
neto anual de una pareja trabajadora dado el sueldo bruto de ambos salarios 
descontando el IRPF.
autor: Carmen Fontcuberta
"""
def calcular_sueldo_neto(salario_bruto):
    """
    Calcula el sueldo neto anual para un salario bruto dado, descontando el IRPF.
    """
    tramos = [(12450, 0.19), (20200, 0.24), (28000, 0.3), (35200, 0.303),(50000, 0.371), (float('inf'), 0.372)]
    for limite, tipo in tramos:
        if salario_bruto <= limite:
            return salario_bruto * (1 - tipo)

def solicitar_salario(conyugue):
    """
    Solicita un salario al usuario y comprueba que sea válido (no negativo).
    """
    while True:
        salario_str = input("Introduzca el salario bruto anual del conyugue   " + str(conyugue ))
        try:
            salario = float(salario_str)
            if salario >= 0:
                return salario
            else:
                print("Error: el salario debe ser un valor positivo o cero.")
        except ValueError:
            print("Error: introduce un valor numérico válido.")

# Solicitar salario del primer trabajador
while True:
    salario1 = solicitar_salario(1)
    if salario1 >= 0:
        break
    else:
        print("Error: el salario debe ser un valor positivo o cero.")

# Solicitar salario del segundo trabajador
while True:
    salario2 = solicitar_salario(2)
    if salario2 >= 0:
        break
    else:
        print("Error: el salario debe ser un valor positivo o cero.")

# Calcular sueldo neto anual de cada trabajador
sueldo_neto1 = calcular_sueldo_neto(salario1)
sueldo_neto2 = calcular_sueldo_neto(salario2)

# Calcular sueldo neto anual conjunto de la pareja
sueldo_neto_pareja = sueldo_neto1 + sueldo_neto2

# Mostrar resultados
print("Sueldo neto anual del primer trabajador: {:.2f}".format(sueldo_neto1))
print("Sueldo neto anual del segundo trabajador: {:.2f}".format(sueldo_neto2))
print("Sueldo neto anual de la pareja: {:.2f}".format(sueldo_neto_pareja))
