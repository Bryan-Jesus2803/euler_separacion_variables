# Solución de una ecuación diferencial separable

## **Descripción del problema**

En este proyecto se resuelve la siguiente ecuación diferencial: 
$$
\frac{𝑑𝑦}{𝑑t}=−2𝑦
$$

con la condición inicial: y(0)=1

Primero se obtiene la solución exacta utilizando el método de separación de variables. 
Después se utiliza el método de Euler para aproximar la solución en el intervalo 
𝑡∈[0,1], utilizando un paso de:

**h = 0.2**

## **Solución analítica**

Partimos de:

$$
\frac{𝑑𝑦}{𝑑t}=−2𝑦
$$

Separamos las variables:

$$
\frac{1}{𝑦}𝑑𝑦=−2𝑑𝑡
$$

Integramos ambos lados:

$$
\int\frac{1}{y}dy=\int-2dt
$$

Obtenemos:
$$
\ln|y|=-2t+C
$$

Despejando $y$:

$$
y=Ce^{-2t}
$$

Ahora utilizamos la condición inicial $y(0)=1$:

$$
1=Ce^0
$$

Por lo tanto:

$$
C=1
$$

La solución exacta es:

$$
\boxed{y(t)=e^{-2t}}
$$

## Instalación y ejecución

### Requisitos

Para ejecutar el programa se necesita tener instalado Python.

Las dependencias utilizadas por el proyecto se encuentran en el archivo `requirements.txt`.

### Clonar el repositorio

1. Ejecutar en tu carpeta local el comando
```bash
git clone https://github.com/Bryan-Jesus2803/euler_separacion_variables.git
```

Después entra a la carpeta del proyecto:
```bash
cd euler-separacion-variables
```

2. Crear el entorno virtual
Se puede crear un entorno virtual con:
```bash
python -m venv venv
```

3. Activar el entorno virtual
En Windows PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```
En Windows CMD o Linux:
```bash
venv\Scripts\activate
```

4. Instalar las dependencias
**Con el entorno virtual activado**:
```bash
pip install -r requirements.txt
```

El archivo requirements.txt contiene las librerías necesarias: NumPy y Matplotlib

### Ejecutar el programa
Para ejecutar el código:
```bash
python metodo_euler.py
```