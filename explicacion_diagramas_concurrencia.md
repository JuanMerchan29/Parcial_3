# Explicación de los Diagramas de Concurrencia

## Diagrama 1: Diagrama de Bloques (Flowchart Conceptual)
**Propósito:** Representar el diseño conceptual y la arquitectura del algoritmo concurrente.

Este diagrama es ideal cuando se solicita **el diseño** del algoritmo, ya que muestra:
- Cómo se estructura el sistema a nivel general.
- Qué partes trabajan en paralelo.
- Cómo fluye la información entre el coordinador y los workers.
- La lógica Map–Reduce aplicada al modelo de regresión lineal.

No entra en detalles técnicos como mensajes ni sincronización explícita, lo que lo convierte en una herramienta clara, limpia y entendible para sustentación. Es el diagrama más adecuado para presentar el **diseño del algoritmo**, no su implementación.

---

## Diagrama 2: Diagrama de Secuencia
**Propósito:** Explicar el funcionamiento interno y detallado del algoritmo concurrente.

Este diagrama representa:
- Los mensajes intercambiados entre procesos.
- La ejecución verdaderamente paralela.
- El envío de gradientes desde cada worker.
- La actualización global del modelo.
- El ciclo completo de entrenamiento concurrente.

Es un diagrama mucho más técnico y profundo. Es ideal si se quiere evidenciar **concurrencia real**: comunicación, sincronización, flujo de datos y estructura por procesos.

---

## Comparación y Uso Recomendado
| Diagrama | Nivel | Uso Ideal | Recomendación |
|---------|-------|-----------|----------------|
| **Diagrama 1: Flowchart / Arquitectura** | Conceptual | Diseño general del algoritmo | ✔ Mejor opción cuando se pide "diseño" |
| **Diagrama 2: Secuencia** | Técnico | Explicación detallada de la concurrencia | ✔ Complemento si se quiere mayor profundidad |

### Conclusión
- Si la consigna pide **diseño**, el diagrama que debes usar es el **Diagrama 1**.
- El **Diagrama 2** sirve como ampliación técnica para demostrar cómo fluye realmente la concurrencia dentro del algoritmo.

Así, ambos diagramas cumplen funciones distintas: el primero muestra *qué hace el sistema a nivel estructural*, mientras el segundo muestra *cómo interactúan los procesos paso a paso*. 

