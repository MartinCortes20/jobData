import pandas as pd

# ===================================
# PASO 1: Cargar el archivo CSV
# ===================================
print("📂 Cargando archivo ventas.csv...")
df = pd.read_csv('ventas.csv')

print(f"✅ Archivo cargado: {len(df)} filas encontradas")
print("\n👀 Primeras 5 filas del archivo original:")
print(df.head())

# ===================================
# PASO 2: Limpieza de texto
# ===================================
print("\n🧹 Limpiando espacios y mayúsculas...")

# Eliminar espacios extra y normalizar a formato Title (Primera Letra Mayúscula)
df['Sucursal'] = df['Sucursal'].str.strip().str.title()
df['Producto'] = df['Producto'].str.strip().str.title()

print("✅ Columnas Sucursal y Producto normalizadas")

# ===================================
# PASO 3: Rellenar valores vacíos
# ===================================
print("\n🔧 Rellenando valores vacíos...")

# Si no hay vendedor, poner "Desconocido"
df['Vendedor'] = df['Vendedor'].fillna('Desconocido')

# Si no hay cantidad o precio, poner 0
df['Cantidad'] = df['Cantidad'].fillna(0)
df['PrecioUnitario'] = df['PrecioUnitario'].fillna(0)

print("✅ Valores vacíos rellenados")

# ===================================
# PASO 4: Recalcular el Total correcto
# ===================================
print("\n🧮 Recalculando totales...")

# Calcular el total correcto: Cantidad × PrecioUnitario
df['Total'] = df['Cantidad'] * df['PrecioUnitario']

print("✅ Columna Total recalculada correctamente")

# ===================================
# PASO 5: Convertir fechas
# ===================================
print("\n📅 Convirtiendo fechas a formato correcto...")

# Convertir la columna Fecha a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Eliminar filas donde la fecha no sea válida
df = df.dropna(subset=['Fecha'])

print(f"✅ Fechas convertidas. Filas restantes: {len(df)}")

# ===================================
# PASO 6: Guardar archivo limpio
# ===================================
print("\n💾 Guardando archivo limpio...")

df.to_excel('ventas_limpias.xlsx', index=False)

print("✅ ¡LISTO! Datos limpios exportados a ventas_limpias.xlsx")

# ===================================
# PASO 7: Mostrar resumen final
# ===================================
print("\n" + "="*50)
print("📊 RESUMEN DE LA LIMPIEZA")
print("="*50)
print(f"Total de registros: {len(df)}")
print(f"Sucursales únicas: {df['Sucursal'].nunique()}")
print(f"Productos únicos: {df['Producto'].nunique()}")
print(f"Total de ventas: ${df['Total'].sum():,.2f}")
print("\n👀 Primeras 5 filas del archivo limpio:")
print(df.head())