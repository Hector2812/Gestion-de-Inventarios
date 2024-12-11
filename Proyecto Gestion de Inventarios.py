# -*- coding: utf-8 -*-
"""
Created on Sat Jul 1 20:01:44 2023

@author: Hector Arrasco
"""

import random

productos = []
ventas = []

def generar_codigo_inventario():
    while True:
        codigo = random.randint(20000, 90000)
        if codigo % 7 == 0:
            return codigo

def agregar_producto():
    tipo = input("Ingrese el tipo de producto (Laptop, Desktop, Impresora): ").strip().upper()
    if tipo not in ["LAPTOP", "DESKTOP", "IMPRESORA"]:
        print("Tipo de producto no válido.")
        return

    descripcion = input("Ingrese la descripción del producto: ")
    importado = input("¿Es importado? (S/N): ").strip().upper()
    if importado not in ["S", "N"]:
        print("Respuesta inválida para importado.")
        return

    codigo = generar_codigo_inventario()

    if tipo == "LAPTOP":
        costo_almacenamiento = random.choice(range(200, 451, 2))
        costo_funda = random.randint(80, 150)
    elif tipo == "DESKTOP":
        costo_almacenamiento = random.choice([x for x in range(180, 251) if x % 3 == 0])
        costo_funda = random.randint(150, 250)
    else:  # IMPRESORA
        costo_almacenamiento = random.choice(range(91, 156, 2))
        costo_funda = None

    producto = {
        "tipo": tipo,
        "descripcion": descripcion,
        "importado": importado,
        "costo_almacenamiento": costo_almacenamiento,
        "codigo": codigo,
        "costo_funda": costo_funda
    }
    productos.append(producto)
    print("Producto agregado correctamente:", producto)

def registrar_venta():
    if not productos:
        print("No hay productos registrados.")
        return

    tipo = input("Ingrese el tipo de producto para la venta (Laptop, Desktop, Impresora): ").strip().upper()
    productos_tipo = [p for p in productos if p["tipo"] == tipo]

    if not productos_tipo:
        print("No hay productos disponibles de este tipo.")
        return

    cantidad = int(input("Ingrese la cantidad de productos vendidos: "))
    precio_almacenamiento = productos_tipo[0]["costo_almacenamiento"]
    precio_venta = round(precio_almacenamiento * 1.25, 2)
    total_venta = cantidad * precio_venta
    numero_venta = 20000 + len(ventas)

    venta = {
        "numero": numero_venta,
        "tipo": tipo,
        "cantidad": cantidad,
        "precio_venta": precio_venta,
        "total_venta": total_venta
    }
    ventas.append(venta)
    print("Venta registrada correctamente:", venta)

def modificar_venta():
    numero = int(input("Ingrese el número de la venta a modificar: "))
    venta = next((v for v in ventas if v["numero"] == numero), None)

    if not venta:
        print("Venta no encontrada.")
        return

    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    venta["cantidad"] = nueva_cantidad
    venta["total_venta"] = nueva_cantidad * venta["precio_venta"]
    print("Venta modificada correctamente:", venta)

def ordenar_ventas():
    n = len(ventas)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ventas[j]["total_venta"] > ventas[j + 1]["total_venta"]:
                ventas[j], ventas[j + 1] = ventas[j + 1], ventas[j]
    print("Ventas ordenadas por total:", ventas)

def mostrar_venta_maxima():
    if not ventas:
        print("No hay ventas registradas.")
        return

    venta_maxima = max(ventas, key=lambda v: v["total_venta"])
    print("Venta con el total más alto:", venta_maxima)

def guardar_datos():
    with open("datos.txt", "w") as archivo:
        archivo.write("Productos:\n")
        for producto in productos:
            archivo.write(f"{producto}\n")

        archivo.write("\nVentas:\n")
        for venta in ventas:
            archivo.write(f"{venta}\n")
    print("Datos guardados correctamente.")

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Registrar venta")
    print("3. Modificar venta")
    print("4. Ordenar ventas")
    print("5. Mostrar venta más alta")
    print("6. Guardar y salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            modificar_venta()
        elif opcion == "4":
            ordenar_ventas()
        elif opcion == "5":
            mostrar_venta_maxima()
        elif opcion == "6":
            guardar_datos()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()
