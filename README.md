# institucion-medica-django-mysql
Proyecto perteneciente al Servicio Geológico Colombiano. 

## DESCRIPCION

Una institución medica requiere dar seguimiento a sus pacientes, los procedimientos que se les han practicado y los medicamentos que les han suministrado. Para tal fin, se solicita implementar los siguientes módulos:

Institución. Desde el cual se podrá registrar la información del centro medico: nombre, dirección, teléfonos, email e icono. El nombre y el icono del centro medico deberán visualizarse desde la cabecera de la aplicación.
Pacientes. Desde el cual se podrá registrar información básica del paciente: Nombres, apellidos, tipo y numero de documento de identificación, dirección ,correo electrónico, celular y persona de contacto con su respectivo numero celular. Adicionalmente, se podrá listar, consultar, modificar o eliminar un registro de paciente.
Médicos.  Desde el cual se podrá registrar información básica del profesional: Nombres, apellidos, tipo y numero de documento de identificación, especialidad, correo electrónico, celular. Adicionalmente, se podrá listar, consultar, modificar o eliminar un registro de medico.
Consulta.  Desde el cual se podrá registrar información básica de la consulta: fecha de la consulta, paciente, medico, medicamento, observaciones. Adicionalmente, se podrá listar, consultar, modificar o eliminar un registro de consulta. Estas consultas se deben registrar desde el modulo de médicos.
Procedimiento.  Desde el cual se podrá registrar información básica del procedimiento a realizar: fecha a realizar, paciente, medico.  Adicionalmente, se podrá listar, consultar, modificar o eliminar un registro de procedimiento. Los procedimientos se deben registrar desde el modulo de médicos.
Medicamentos.  Desde el cual se podrá registrar información básica del medicamento a asignar: Nombre del medicamento, cantidad, formula (Descripción de como se debe tomar o aplicar el medicamento), fecha de receta. Adicionalmente, se podrá listar, consultar, modificar o eliminar un registro de medicamentos. Los medicamentos se deben registrar desde el modulo de médicos.
Historial. Desde aquí se podrá consultar las citas, medicamentos y procedimientos realizados a un paciente. Para realizar la consulta se debe ingresar el numero de documento del paciente. Debe distinguirse claramente de manera visual las consultas, medicamentos y procedimientos.
