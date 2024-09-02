import tkinter as tk
from tkinter import simpledialog

# Inicializar la ventana de Tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

calificaciones = []

for i in range(5):
    calificacion = simpledialog.askstring("Input", f"Capturar la calificación {i+1}:")
    calificaciones.append(int(calificacion))

print("Calificaciones capturadas:", calificaciones)
