# 🌌 Simulación del Problema de los Tres Cuerpos

Este repositorio contiene una simulación numérica y visualización animada del **problema de los tres cuerpos**, un problema clásico de la mecánica celeste que describe el movimiento de tres masas bajo la influencia de la **gravitación universal**.

---

## 📖 Introducción

El **problema de los tres cuerpos** busca describir cómo interactúan tres cuerpos en el espacio debido a la gravedad.  
A diferencia del problema de dos cuerpos (que tiene solución exacta gracias a las leyes de Kepler y Newton), el de tres cuerpos **no posee una solución analítica general**.  
Por ello, se estudia mediante **simulación numérica** con métodos de integración.

En esta implementación se utilizan:
- **Ecuaciones de Newton** para la fuerza gravitacional.
- **Integración numérica** para aproximar trayectorias.
- **Visualización animada** con `matplotlib`.

## ⚙️ Condiciones iniciales

Para esta simulación se eligieron valores **hipotéticos y simplificados** de masas, posiciones y velocidades (no corresponden a un sistema real de Sol-Tierra-Luna, sino que buscan mostrar el caos del sistema):

- **Cuerpo 1**  
  - Masa: `5.0`  
  - Posición inicial: `(−1, 0)`  
  - Velocidad inicial: `(0, −0.5)`  

- **Cuerpo 2**  
  - Masa: `3.0`  
  - Posición inicial: `(1, 0)`  
  - Velocidad inicial: `(0, 0.5)`  

- **Cuerpo 3**  
  - Masa: `4.0`  
  - Posición inicial: `(0, 1)`  
  - Velocidad inicial: `(−0.5, 0)`  

Estas condiciones iniciales generan trayectorias complejas y muestran cómo pequeñas diferencias en valores pueden producir comportamientos muy distintos.

##Análisis
La simulación muestra que, aunque las leyes que rigen el movimiento de los tres cuerpos son deterministas, el sistema exhibe un comportamiento caótico y difícil de predecir a largo plazo. Las trayectorias no son periódicas y pequeñas variaciones en las condiciones iniciales generan resultados muy distintos, lo que confirma la sensibilidad al estado inicial.

En conclusión, el problema de los tres cuerpos ilustra la complejidad de la mecánica celeste y cómo fenómenos aparentemente simples pueden dar lugar a dinámicas impredecibles. Esta simulación, aunque simplificada, refleja la belleza matemática y el carácter caótico de los sistemas gravitacionales.

## ⚙️ Requisitos e Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/tres-cuerpos.git
   cd tres-cuerpos
