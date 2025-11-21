# Diseño detallado de la solución usando concurrencia

A continuación se presenta una versión ampliada y más completa del diseño para la regresión lineal empleando el paradigma de concurrencia (modelo Maestro–Trabajador). Incluye la explicación paso a paso y los diagramas provistos.

---

## **1. Arquitectura general del sistema concurrente**

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

---

## **3. Diagramas del diseño concurrente**

### **📌 Diagrama 1 — Diagrama general de arquitectura concurrente**

![Diagrama Arquitectura](/mnt/data/deepseek_mermaid_20251121_e9c127.png)

---

### **📌 Diagrama 2 — Diagrama de secuencia detallado**

![Diagrama Secuencia](/mnt/data/b8906c20-93e2-4980-8daf-33fe19ba3a43.png)

---

Si quieres, también puedo generar la explicación para el punto de **Aspectos**, o integrar todos los puntos en un único documento en tu lienzo.

