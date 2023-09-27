import csv


class Single_variable():
    file_name = None  # Nombre del csv
    my_list_variables = None  # Lista de variables x1,x2,x3 ... xn
    dict_columnas_valores = {}  # Diccionario de listas para en cada clave x1,x2,x3 ..xn guardar todos los valores de esa columna "Para tener un diccionario de vectores columna"
    my_csv_dict = None  # Diccionario con todas las filas del csv

    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name, 'r', encoding='utf-8') as my_csv:
            my_csv = csv.DictReader(my_csv)
            self.my_list_variables = my_csv.fieldnames
            self.my_csv_dict = list(my_csv)

    def incializa_lista_variables(self):
        for x in self.my_list_variables:
            # Creamos un diccionario de listas para que cada clave "x1,x2,x3..xn" sea el valor de mi lista de encabezados del csv osea las variables y ademas ponga una lista vacia en el value
            self.dict_columnas_valores[x] = []

        # El siguiente for anidado esta diseñado para iterar sobre cada fila en self.my_csv_dict, que es una lista de diccionarios donde cada diccionario representa una fila del archivo CSV. Luego, para cada fila, se itera sobre sus elementos (pares clave-valor) usando row.items(), donde key es el nombre de la columna y value es el valor correspondiente en esa columna.
        for row in self.my_csv_dict:
            for key, value in row.items():
                self.dict_columnas_valores[key].append(value)

    