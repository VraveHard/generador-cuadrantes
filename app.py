

!pip install ortools

from ortools.sat.python import cp_model

# Datos: nombres de los empleados y días de la semana
empleados = ['xavi', 'lyan', 'axel', 'waqas', 'atif', 'mosi', 'xenia', 'edu']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo' ]
turnos_por_dia = 3  # Número de turnos que necesitas cubrir cada día

# Crear el modelo de optimización
modelo = cp_model.CpModel()

# Crear variables de asignación de turnos (1 si un trabajador está asignado, 0 si no)
asignaciones = {}
for e in empleados:
    for d in dias:
        for t in range(turnos_por_dia):
            asignaciones[(e, d, t)] = modelo.NewBoolVar(f'asignacion_{e}_{d}_{t}')

# Restricción: un empleado solo puede estar asignado a un turno por día
for e in empleados:
    for d in dias:
        modelo.Add(sum(asignaciones[(e, d, t)] for t in range(turnos_por_dia)) <= 1)

# Restricción: necesitamos cubrir todos los turnos
for d in dias:
    for t in range(turnos_por_dia):
        modelo.Add(sum(asignaciones[(e, d, t)] for e in empleados) == 1)

# Resolver el problema
solver = cp_model.CpSolver()
status = solver.Solve(modelo)

# Mostrar el resultado
if status == cp_model.OPTIMAL:
    for d in dias:
        print(f'Turnos del {d}:')
        for t in range(turnos_por_dia):
            for e in empleados:
                if solver.BooleanValue(asignaciones[(e, d, t)]):
                    print(f'  Turno {t + 1}: {e}')


!pip install streamlit


import streamlit as st

# Título de la app
st.title('Generador Automático de Cuadrantes')

# Entrada de datos de empleados
empleados_input = st.text_area("Introduce los nombres de los empleados (separados por comas):")
empleados = empleados_input.split(',')

# Definir los días y los turnos por día
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
turnos_por_dia = st.slider('Número de turnos por día', 1, 5, 2)

# Botón para generar el cuadrante
if st.button('Generar cuadrante'):
    # Lógica del generador de turnos (el código de OR-Tools que ya implementaste)
    # Puedes copiar la lógica del paso anterior aquí
    st.write("Cuadrante generado:")
    for d in dias:
        st.write(f"Turnos del {d}:")
        for t in range(turnos_por_dia):
            st.write(f"Turno {t + 1}: {empleados[t % len(empleados)]}")
