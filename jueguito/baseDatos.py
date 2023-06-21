import sqlite3

def create_database():
    conexion = sqlite3.connect("datos_jugadores.db")
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores (
            nombre TEXT,
            puntaje INTEGER
        )
    """)

    conexion.commit()
    conexion.close()

def insert_player(nombre, puntaje):
    conexion = sqlite3.connect("datos_jugadores.db")
    cursor = conexion.cursor()

    # Insertar nombre y puntaje en la tabla jugadores
    cursor.execute("INSERT INTO jugadores VALUES (?, ?)", (nombre, puntaje))

    conexion.commit()
    conexion.close()
