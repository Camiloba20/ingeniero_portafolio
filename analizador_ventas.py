#!/usr/bin/env python3

import csv
from collections import defaultdict

def analizar_ventas(archivo_csv):
    productos = defaultdict(lambda: {"cantidad": 0, "precio_unitario": 0})
    
    with open(archivo_csv, 'r') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            producto = fila['producto']
            cantidad = int(fila['cantidad'])
            precio = int(fila['precio'])
            
            productos[producto]["cantidad"] += cantidad
            productos[producto]["precio_unitario"] = precio
    
    return productos

def generar_reporte(productos):
    print("=" * 50)
    print("REPORTE DE VENTAS - PYTHON")
    print("=" * 50)
    
    total_unidades = sum(p["cantidad"] for p in productos.values())
    print(f"\n📊 Total de unidades vendidas: {total_unidades}")
    
    print("\n📋 Ventas por producto:")
    for producto, datos in sorted(productos.items()):
        print(f"   - {producto:10} → {datos['cantidad']} unidades (${datos['precio_unitario']} c/u)")
    
    mas_vendido = max(productos.items(), key=lambda x: x[1]["cantidad"])
    print(f"\n🏆 Producto estrella: {mas_vendido[0]} con {mas_vendido[1]['cantidad']} unidades")

if __name__ == "__main__":
    datos = analizar_ventas("/home/camilo/ingeniero_portafolio/ventas_correcto.csv")
    generar_reporte(datos)
