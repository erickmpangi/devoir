import pickle    

# cargar el dataset
with open('dataset.p', 'rb') as fp:
    mydata = pickle.load(fp)    
X_train = mydata["x_train"][:]/255 # 209 instancias, cada instancia de tamaño [D x 1]
X_test = mydata["x_test"][:]/255   # 50 instancias de prueba 
Y_train = mydata["y_train"][:] # etiquetas del conjunto de entrenamiento
Y_test = mydata["y_test"][:]   # etiquetas del conjunto de prueba
            
                
''' 1.- Implementar la función sigmoide (aprox. 2 líneas de código).
    Entrada:
        z: la suma ponderada de la neurona (vector)
    Salida:
        sigmoid_z: función sigmoide evaluada en z, debe tener el mismo tamaño que z '''                
def sigmoid():      
    return
    
''' 2.- Implementar una función para calcular la propagación hacia adelante (feedforward)
    y la propagación hacia atrás (backpropagation). (aprox. 5 líneas de código)
    Entradas: 
        X: Matriz de instancias de entrenamiento, de tamaño [D x m]
        w: El vector de pesos, de tamaño [D x 1] 
        b: El bias (escalar)
        y: Vector de etiquetas de entrenamiento
    Salidas:
        cost : Función de costo J = promedio de la función de pérdida (binary cross-entropy).
        dw : Gradiente del costo con respecto a los pesos, dJ/dw
        db : Gradiente del costo con respecto al bias, dJ/db     ''' 
def fw_bw_propagation():
    return
    
''' 3.- Implementar una función para entrenar el modelo con descenso de gradiente
(aprox 10 líneas de código)
    Entradas:    
        w : matriz de pesos
        b : bias (escalar)
        X : matriz de datos de tamaño [X x m]
        y : etiquetas de entrenamiento
        N : número de iteraciones (p.ej. 100)
        eta : tasa de aprendizaje
    Salidas:    
        wo : pesos entrenados
        bo : bias entrenados
        costs : vector de costos para cada iteración (se usará para graficar el entrenamiento) '''
def train_model():
    return
    

''' 4.- Implementar una función para evaluar el modelo YA ENTRENADO (aprox. 10 líneas de código)
    Entradas:
        wo : vector de pesos ya entrenados
        bo : bias entrenado
        X : matriz de datos sobre los que se va a evaluar el modelo, tamaño [D x m]    
    Salida :
        prediction : vector que contiene las predicciones (tienen que ser 1 o 0 (enteros)) para
        cada instancia de entrada en X.     '''
def evaluate():
    return        
    
    
    
# MAIN
# 1. Inicializar w y b con ceros.

# 2. Entrenar el modelo con función train_model

# 3. Evaluar el modelo con función evaluate, sobre conjunto de entrenamiento y sobre el conjunto de prueba

# 4. Imprimir la precisión del modelo (accuracy) en dataset de entrenamiento y en dataset de prueba

# 5. Graficar el costo durante el entrenamiento (lo regresa la función train_model)
