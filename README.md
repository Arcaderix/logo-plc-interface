# PLC Control Client

**PLC Control Client** es una aplicación de escritorio desarrollada en **Python** que permite la conexión y control de un **PLC Siemens LOGO!** a través de una interfaz gráfica intuitiva. Utilizando la biblioteca **Tkinter**, esta herramienta facilita la interacción con el PLC, permitiendo la lectura y escritura de entradas y salidas digitales de manera eficiente.

## **Características Principales:**

- **Conexión al PLC:** Establece una conexión confiable con el PLC Siemens LOGO! mediante la red local, utilizando el protocolo TCP/IP.
- **Interfaz Gráfica Intuitiva:** Diseñada con Tkinter, la interfaz permite una fácil navegación y control de las funciones del PLC.
- **Control de Entradas y Salidas:** Permite leer el estado de las entradas digitales y escribir en las salidas digitales del PLC.
- **Actualización Automática:** La aplicación verifica periódicamente el estado del PLC.
- **Registro de Eventos:** Mantiene un historial de eventos y acciones realizadas.

## **Tecnologías Utilizadas:**

- **Lenguaje:** Python 3.x
- **Bibliotecas:** Tkinter, snap7
- **Protocolo de Comunicación:** TCP/IP

## **Objetivo del Proyecto:**

Es el resultado de más de 2 meses practicando snap7 y python  tiempo parcial, codificación recodificación, depuración, etc. PLC Control Client  está codificado en python , Este proyecto tiene como objetivo proporcionar una herramienta sencilla y efectiva para el control y monitoreo de PLCs Siemens LOGO!, ideal para aplicaciones de automatización y control industrial en entornos educativos y profesionales.

---

## **Release Notes**

### **Versión 1.0 - Control PLC Ciberfísico**

**¡Bienvenidos al primer parche!** 🎉

Con la **versión 1.0**, hemos lanzado las primeras funcionalidades para conectar y controlar tu **PLC Siemens LOGO!**. Aquí están las novedades:

#### **Lo nuevo:**

- **Conexión remota habilitada**: ¡Ahora puedes conectarte a tu PLC a través de **Hamachi**! Esto te permitirá controlar tu PLC de manera remota, ideal para tener todo bajo control desde cualquier lugar. 🔧💻
- **Conexión Ethernet del PLC**: Ahora puedes conectar el PLC de manera más fácil y eficiente. Solo asegúrate de tener la **IP correcta** del PLC para establecer la comunicación. 🌐
- **Dependencia de Hamachi**: Aunque dependemos de **Hamachi** para la conexión remota, en futuras actualizaciones eliminaremos esta dependencia y ofreceremos una solución más directa. 🌟

> **Próximos pasos:**
> 
> - Optimizar la **conectividad remota** para hacerla aún más rápida y estable.
> - Eliminar la **dependencia de Hamachi**, buscando una solución más sencilla.
> - Trabajar en la mejora de **seguridad** para garantizar conexiones más robustas y seguras. 🔒

---

### **Versión 2.0 - Control PLC Ciberfísico**

**¡El gran parche 2.0 ya está disponible!** 🚀

Con esta nueva versión, hemos mejorado la estabilidad y la experiencia de usuario, incorporando nuevas características y **mejoras de rendimiento**. Aquí te contamos lo que trae esta versión:

#### **Lo nuevo y mejorado:**

- **Reconexión automática al PLC**: Si tu conexión se pierde, el cliente ahora intentará reconectarse automáticamente al PLC. ¡Nunca más perderás la conexión! 🔄
- **Manejo de errores mejorado**: Se ha implementado un **mecanismo de manejo de errores** más robusto. Ahora se capturan y notifican todos los errores de manera clara. 🛠️
- **Verificación automática cada 10 segundos**: La aplicación revisa automáticamente el estado del PLC cada 10 segundos, manteniendo los indicadores de estado siempre actualizados. ⏱️
- **Interfaz cliente mejorada**: La **interfaz gráfica** ha sido completamente rediseñada para hacerla más **intuitiva** y fácil de usar. Ahora puedes ver claramente el estado del PLC y de las salidas digitales. 🎨
- **Registros en consola mejorados**: Se agregó un **sistema de registros** más detallado en la consola para ayudarte a depurar y monitorear los eventos en tiempo real. 📜

> **Próximos pasos:**
> 
> - Mejorar la **seguridad** de las conexiones, implementando cifrado y otras medidas de protección.
> - Conectar y controlar **múltiples PLCs** desde una sola instancia del cliente. ¡Más control, más poder! 💪
> - Agregar más opciones de **visualización de datos** y gráficos para facilitar el monitoreo del PLC. 📊
> - Explorar la **integración en la nube** para ofrecerte un control remoto aún más potente. 🌥️

---
Versión 2.0.a - Corrección Crítica de Conexión
¡Versión 2.0.a ya está aquí! ✅

Esta actualización corrige un problema crítico que afectaba la estabilidad de las conexiones en la versión anterior. Nos aseguramos de que tu experiencia de control con el PLC sea aún más robusta y sin interrupciones.

🛠️ Cambios incluidos:
[WinError 10056] - Socket ya conectado: Se resolvió el error que impedía reconectar al servidor si el socket ya estaba abierto. Ahora, el cliente gestiona correctamente el estado del socket creando una nueva instancia cuando se reconecta. 🎯

IP dinámica desde interfaz: Ya no es necesario modificar el código fuente para cambiar la dirección IP del SERVIDOR. Ahora puedes ingresar la IP directamente desde la interfaz gráfica. 💡

Mejores prácticas de cliente TCP: Se aplicaron principios de diseño robusto al manejo de sockets, mejorando la estabilidad general de la aplicación. 👨‍💻

> **📌 ¿Qué sigue?**
> 
> - Nos estamos preparando para llevar esta herramienta al siguiente nivel. Algunas funciones planeadas para las próximas versiones:
> - Seguridad con cifrado de datos 🔐
> - Visualización avanzada con gráficas  📈

---

