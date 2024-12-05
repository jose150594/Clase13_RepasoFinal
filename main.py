# Proyecto clase 13 Repaso Final
# Autor: Jose Pablo Delgado.
# Fecha: 4/12/2024
import csv
import pandas as pd
import os
def menu():
    ventas = []  # Lista donde se almacenarán las ventas ingresadas
    while True:
        print('\n---- Menú Principal ---')
        print('1. Ingresar datos de ventas.')
        print('2. Guardar datos en un archivo CSV.')
        print('3. Analizar los datos guardados.')
        print('4. Salir del sistema.')
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            print('\n---- Ingreso de Ventas ---')
            ingresar_datos(ventas)
        elif opcion == '2':
            print('\n---- Guardar CSV ---')
            guardar_csv(ventas)
        elif opcion == '3':
            # Aquí iría la funcionalidad para analizar los datos guardados
            analizar_ventas(ventas)
        elif opcion == '4':
            print('Saliendo del sistema.')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')

def analizar_ventas(ventas):
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv('ventas.csv', encoding='latin-1') 
    print('\n--- Resumen de Ventas ---')
    
    # ¿Cuál fue el total de ingresos generados?
    df['Subtotal'] = df['Cantidad'] * df['Precio']
    total = df['Subtotal'].sum()
    print(f'Total de ingresos: ₡{total:.2f}')
    
    # ¿Cuál fue el producto más vendido?
    producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum().idxmax()
    cantidad_vendida = df.groupby('Producto')['Cantidad'].sum().max()
    print(f'El producto más vendido es "{producto_mas_vendido}" con {cantidad_vendida} unidades.')

    # ¿Quién fue el cliente con más compras?
    cliente_mas_compras = df.groupby('Cliente')['Subtotal'].sum().idxmax()
    total_compras_cliente = df.groupby('Cliente')['Subtotal'].sum().max()
    print(f'El cliente con más compras es "{cliente_mas_compras}" con un total de ₡{total_compras_cliente:.2f}.')

    # ¿Cuáles fueron las ventas por fecha?
    print('\nVentas por fecha:')
    ventas_por_fecha = df.groupby('Fecha')['Subtotal'].sum()
    print(ventas_por_fecha)
#groupby
 
  # cliente con mas ventas

def guardar_csv(ventas):
    if not ventas:
        print('No hay datos para guardar')
        return

   # with open('ventas.csv', mode='w', newline='') as file:
    #    guardado = csv.DictWriter(file, fieldnames=['Producto', 'Cantidad', 'Precio', 'Fecha', 'Cliente'])
     #   guardado.writeheader()
      #  guardado.writerows(ventas)
    
    #print('Datos guardados en el archivo.')

    # Guardar los datos en un archivo CSV
    with open('ventas.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Producto', 'Cantidad', 'Precio', 'Fecha', 'Cliente'])
        writer.writeheader()  # Escribir los nombres de las columnas
        for venta in ventas:
            writer.writerow(venta)  # Escribir cada venta en una fila del archivo CSV
    print("Datos guardados en 'ventas.csv' correctamente.\n")



def ingresar_datos(ventas):
    while True:
        # Entrada de datos
        producto = input('Ingrese el nombre del producto: ')
        cantidad = int(input('Ingrese la cantidad vendida: '))
        precio = float(input('Ingrese precio por unidad: '))
        fecha = input('Ingrese la fecha de la venta (YYYY-MM-DD): ')  # Fecha de la venta en formato YYYY-MM-DD
        cliente = input('Ingrese el nombre del cliente: ')  # Nombre del cliente que realizó la compra

        # Validaciones con if
        if cantidad <= 0: 
            print('La cantidad debe ser mayor a 0. Inténtelo nuevamente.')
            continue
        if precio <= 0:
            print('El precio no es válido. Inténtelo nuevamente.')
            continue

        # Crear el diccionario de la venta
        venta = {
            'Producto': producto,
            'Cantidad': cantidad,
            'Precio': precio,
            'Fecha': fecha,
            'Cliente': cliente
        }
        ventas.append(venta)

        # Preguntar si desea ingresar otra venta
        continuar = input('¿Desea ingresar otra venta? (s/n): ').lower()
        if continuar == 'n':
            break

# Validar la ejecución del archivo principal
if __name__ == '__main__':
    print('Bienvenido al sistema de Gestión de Ventas')
    menu()
