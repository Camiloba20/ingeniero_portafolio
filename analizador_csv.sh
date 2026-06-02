#!/bin/bash
# analizador basico de archivos CSV
ARCHIVO=$1
if [ -z "$ARCHIVO" ]; then
echo "❌ Error: Debes especificar un archivo CSV"
echo "Uso: ./analizador_csv.sh archivo.csv"
exit 1
fi
echo "=== ANALIZADOR CSV ==="
echo "Archivo: $ARCHIVO"
echo ""
echo "📊 Columnas:"
head -1 "$ARCHIVO"
echo ""
echo "📋 Productos únicos:"
cut -d',' -f1 "$ARCHIVO" | sort | uniq
echo ""
echo "🔢 Cantidad total de filas (sin cabecera):"
TOTAL=$(tail -n +2 "$ARCHIVO" | wc -l)
echo "$TOTAL"
echo""
echo "📦 Producto más vendido (por cantidad):"
tail -n +2 "$ARCHIVO" | cut -d',' -f2 | sort -n | tail -1
