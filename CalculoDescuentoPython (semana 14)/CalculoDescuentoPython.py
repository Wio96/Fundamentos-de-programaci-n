# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total de la compra
monto1 = 150.00
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
monto2 = 200.00
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2

# Mostrar los resultados
print(f"Compra 1: Monto = ${monto1}, Descuento = ${descuento1}, Monto final = ${monto_final1}")
print(f"Compra 2: Monto = ${monto2}, Descuento = ${descuento2}, Monto final = ${monto_final2}")