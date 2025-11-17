# **📊 Proyecto de Automatización E-commerce**

**📋 Descripción**  
Sistema de automatización para procesos de e-commerce que gestiona órdenes, transformación de archivos y ejecución de macros. Actualmente en desarrollo con funcionalidades básicas operativas. Procesa datos de tiendas como Ripley y Falabella mediante scripts Python especializados.

## **🚀 Estado del Proyecto**  
⚠️ **PROYECTO INCOMPLETO - EN DESARROLLO**

El sistema actual funciona con scripts independientes que automatizan procesos básicos. Falta integración entre módulos, manejo robusto de errores y características avanzadas. La arquitectura actual es funcional pero requiere refactorización para escalabilidad.

<p align="center">
  <img width="329" height="517" alt="Diagrama_de_Flujo_del_Proceso" src="https://github.com/user-attachments/assets/2af9f5da-ca13-4d56-904b-afe772caa462" />
</p>

**Diagrama de secuencia** que muestra el flujo actual de ejecución.  
Comienza con el menú principal, selección de tienda **Ripley**, y ejecución secuencial de scripts para **crear ambiente**, **transformar archivos**, **ejecutar macros** y **generar packing**.

## **📁 Estructura de Archivos**

<p align="center">
  <img width="455" height="163" alt="Estructura_de_Archivos" src="https://github.com/user-attachments/assets/71a1da67-aed9-41c9-9d76-69bbd37fc87f" />
</p>

Cada script maneja una **función específica**, desde la **creación del entorno de trabajo** hasta la **ejecución de macros Excel**.  
La estructura actual **funciona**, pero **carece de integración elegante**.

## **🔄 Flujo de Procesamiento**

<p align="center">
  <img width="346" height="429" alt="Diagrama_de_Estados_del_Sistema" src="https://github.com/user-attachments/assets/3d7be886-8ccd-4611-97ea-f1e42e0b7042" />
</p>

Diagrama de estados que ilustra las **transiciones entre cada fase del proceso**.  
Cada estado representa un **script ejecutándose secuencialmente**, mostrando el **ciclo completo desde inicio hasta finalización**.


## **🛠️ Instalación y Uso**
<p align="center">
   <img width="243" height="168" alt="Instalacion" src="https://github.com/user-attachments/assets/d5160a63-78e5-4943-bf41-af0245006ee0" />
</p>
Seleccione la tienda y espere la ejecución automática. El sistema crea directorios por fecha, transforma archivos y ejecuta macros. Verifique los logs en consola para monitoreo.

---

## **📈 Proyecciones y Mejoras Futuras**

<p align="center">
  <img width="456" height="590" alt="Arquitectura_Target_Planeada" src="https://github.com/user-attachments/assets/d7a595bd-85a7-4d4d-a1f7-0e44bb3d4ebd" />
</p>

Arquitectura objetivo que incluye API REST, orquestador central, microservicios por tienda, base de datos unificada y dashboard web. Representa la evolución desde scripts monolíticos hacia sistema distribuido.

## **🎯 Roadmap de Desarrollo**

**Fase 1 - Estabilización (1-2 meses)**
✅ Scripts básicos funcionales  
🔄 Sistema de logging centralizado  
🔄 Manejo robusto de errores  
🔄 Configuración externalizada  

**Fase 2 - Escalabilidad (2-3 meses)**
🔲 Patrón modular con herencia  
🔲 Procesamiento paralelo  
🔲 Caché inteligente  
🔲 Sistema de alertas  

**Fase 3 - Enterprise (3-6 meses)**
🔲 API REST + Dashboard  
🔲 CI/CD Pipeline  
🔲 Integración en la nube  
🔲 Analítica avanzada  
