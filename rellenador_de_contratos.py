from docxtpl import DocxTemplate
from datetime import datetime

fecha_nombre = datetime.now().strftime("%d_%m_%y")

ciudad = input("ciudad del trabajo >> ")
nombre = input("ingresa el nombre completo del trabajador: ")
run = input("RUN del trabajador: ")
fecha = datetime.today().strftime("%d de %b. del %Y")
nacionalidad = input("nacionalidad del trabajador: ")
estado = input("estado civil del trabajador: ")
f_nacimiento = input("fecha de nacimiento del trabajador: ")
direccion_t= input("direccion del trabajador: ")
nombre_empresa = input("nombre de la empresa: ")
rut_empresa = input("rut de la empresa: ")
nombre_empleador =input("nombre del representante legal o empleador: ")
rut_empleador = input("RUT del empleador: ")
direccion_empresa = input("dirección de la empresa: ")
cargo = input("ingresa a que cargo entrara el trabajador: ")
lugar_trabajo = input("dirección de trabajo: ")
cant_horas = input("horas ordinarias por semana: ")
entrada = input("entrada de cada jornada: ")
salida = input("salida de cada jornada: ")
descanso = input("minutos de descanso: ")
entrada_descanso = input("hora de entrada al descanso: ")
salida_descanso = input("hora de salida del descanso: ")
sueldo_m = input("sueldo mensual liquido: ")
beneficio1 = input("primer beneficio: ")
beneficio2 = input("segundo beneficio: ")
beneficio3 = input("tercer beneficio: ")



doc = DocxTemplate("plantilla_contrato.docx")
context = { "ciudad" : ciudad,
           "fecha" : fecha,
           "nombre_completo" : nombre,
           "run" : run,
           "nacionalidad": nacionalidad,
           "estado": estado,
           "f_nacimiento": f_nacimiento,
           "dirección_t" : direccion_t,
           "nombre_empresa": nombre_empresa,
           "rut_empresa": rut_empresa,
           "nombre_empleador": nombre_empleador,
           "rut_empleador": rut_empleador,
           "dirección_empresa": direccion_empresa,
           "cargo": cargo,
           "lugar_trabajo": lugar_trabajo,
           "cant_horas": cant_horas,
           "entrada": entrada,
           "salida": salida,
           "descanso": descanso,
           "entrada_descanso": entrada_descanso,
           "salida_descanso": salida_descanso,
           "sueldo_m": sueldo_m,
           "beneficio1" :beneficio1,
           "beneficio2": beneficio2,
           "beneficio3": beneficio3
 }


doc.render(context)


doc.save(f"contratos/contrato{fecha_nombre}.docx")