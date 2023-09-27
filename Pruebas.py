from ClaseUnivariable import Single_variable

objeto_prueba = Single_variable("archivo_limpiado.csv")
objeto_prueba.incializa_lista_variables()
print(objeto_prueba.dict_columnas_valores['fecha_creacion'])