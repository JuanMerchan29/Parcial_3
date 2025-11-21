# Diseño   concurrencia

A continuación se presenta una versión ampliada y más completa del diseño para la regresión lineal empleando el paradigma de concurrencia (modelo Maestro–Trabajador). Incluye la explicación paso a paso y los diagramas provistos.

---

## **1. Arquitectura general del sistema concurrente**
<img width="980" height="2048" alt="image" src="https://github.com/user-attachments/assets/18e0c447-11b7-421c-9ea5-d88427f280ca" />


La regresión lineal con gradiente descendente es una operación que puede paralelizarse dividiendo el dataset en fragmentos y enviando cada fragmento a un **Worker** que calcula los gradientes locales. Un **Coordinador** central recibe esos gradientes, los combina y actualiza los parámetros.

### **Componentes principales:**

### **🔹 DataLoader**  
Carga el dataset y lo divide en **K particiones**. Cada partición representa un minibatch que será procesado por un Worker.

### **🔹 Coordinator (Maestro)**
Controla todo el ciclo de entrenamiento:
- Inicializa Workers.
- Envía parámetros actuales (w, b).
- Recibe gradientes de cada Worker.
- Agrega los gradientes.
- Actualiza los parámetros globales.
- Decide cuándo detener el entrenamiento.

### **🔹 Workers (Trabajadores)**
Cada uno:
- Recibe parámetros (w, b).
- Recibe un chunk de datos.
- Calcula predicciones, errores y gradientes locales.
- Envía los gradientes al Aggregator.

### **🔹 Aggregator**
Realiza:
- La suma o promedio de gradientes.
- El cálculo final de los nuevos parámetros.

---

## **2. Flujo detallado del algoritmo concurrente**
<img width="2048" height="843" alt="image" src="https://github.com/user-attachments/assets/df737c70-41e1-4eab-8457-5e47363e4f86" />


### **Fase 1 — Inicialización**
1. DataLoader divide el dataset en K trozos.  
2. Coordinator crea los Workers.  
3. Coordinator prepara los parámetros iniciales w y b.

### **Fase 2 — Inicio de cada época**
4. Coordinator envía los parámetros **(w, b)** a cada Worker.
5. Coordinator envía el chunk correspondiente a cada Worker.

### **Fase 3 — Cálculo paralelo**
Cada Worker ejecuta en paralelo:
- `y_pred = w * X_local + b`
- `error  = y_pred - y_local`
- `dw_local = 2/m_local * sum(error * X_local)`
- `db_local = 2/m_local * sum(error)`

### **Fase 4 — Envío de gradientes**
Cada Worker devuelve:
- `dw_local`
- `db_local`

### **Fase 5 — Agregación**
El Aggregator ejecuta:
- `dw = sum(dw_local)` o su promedio.
- `db = sum(db_local)` o su promedio.
- `w = w - lr * dw`
- `b = b - lr * db`

### **Fase 6 — Repetición o terminación**
Si no se alcanzan las épocas:
- Coordinator envía los nuevos parámetros a cada Worker.

Si se terminó:
- Coordinator envía STOP a todos los Workers.








