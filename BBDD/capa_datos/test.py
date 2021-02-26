from personaDAO import PersonaDao
from persona import Persona

#Insertamos un nuevo registro
persona = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
personas_insertadas = PersonaDao.insertar(persona)
print(f'Personas insertados: {personas_insertadas}')