# Asistente Virtual
# Autor: [Brantdon Andres CAlvo MArtinez]
# Fecha: [30/112025]

# Paso 1: Definición de variables y entrada del usuario
tipo_de_error = input("Ingrese el tipo de problema (falla, error de configuración, solicitud nueva, problema de acceso): ")
sistema_operativo = input("Ingrese su sistema operativo (Windows, Linux, macOS): ")
nivel_urgencia = input("Ingrese el nivel de urgencia (bajo, medio, alto): ")
modulo = input("Ingrese el módulo afectado (login, base de datos, interfaz, reportes): ")

# Paso 3: Definición de conjuntos
ErroresUsuario = ["error de configuración", "problema de acceso"]
ErroresSistema = ["falla", "solicitud nueva"]
SistemasOperativos = ["Windows", "Linux", "macOS"]
NivelesUrgencia = ["bajo", "medio", "alto"]
ModulosSoftware = ["login", "base de datos", "interfaz", "reportes"]

# Paso 2: Reglas del asistente (Modus Ponens y Modus Tollens)
if tipo_de_error in ErroresSistema and modulo == "base de datos":
    clasificacion = "Crítico"
    accion = "Informar al equipo de soporte inmediatamente"
elif tipo_de_error in ErroresUsuario and sistema_operativo == "Windows":
    clasificacion = "Revisar permisos del usuario"
    accion = "Seguir pasos sugeridos por el asistente"
elif modulo == "login" and tipo_de_error == "problema de acceso":
    clasificacion = "Soporte inmediato"
    accion = "Contactar al soporte técnico ahora mismo"
elif tipo_de_error == "solicitud nueva" and nivel_urgencia == "bajo":
    clasificacion = "Pendiente programable"
    accion = "Esperar a que soporte programe la solución"
elif modulo == "interfaz":
    clasificacion = "Enviar al equipo de diseño"
    accion = "Notificar al equipo de diseño"
else:
    clasificacion = "Caso general"
    accion = "Revisar manual de soluciones"

# Paso 4: Salida del asistente
print("\n--- Resultado del Asistente Virtual ---")
print("Clasificación del caso:", clasificacion)
print("Acción sugerida:", accion)
