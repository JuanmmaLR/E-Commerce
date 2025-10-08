# **📊 Proyecto de Automatización E-commerce**

**📋 Descripción**  
Sistema de automatización para procesos de e-commerce que gestiona órdenes, transformación de archivos y ejecución de macros. Actualmente en desarrollo con funcionalidades básicas operativas. Procesa datos de tiendas como Ripley y Falabella mediante scripts Python especializados.

## **🚀 Estado del Proyecto**  
⚠️ **PROYECTO INCOMPLETO - EN DESARROLLO**

El sistema actual funciona con scripts independientes que automatizan procesos básicos. Falta integración entre módulos, manejo robusto de errores y características avanzadas. La arquitectura actual es funcional pero requiere refactorización para escalabilidad.

<p align="center">
  <img width="122" height="516" alt="Diagrama_de_Flujo_del_Proceso" src="https://github.com/user-attachments/assets/9984e120-3dd7-4d8c-bd08-310f1f8e76b6" />
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
  <img width="103" height="431" alt="Diagrama_de_Estados_del_Sistema" src="https://github.com/user-attachments/assets/ff37a26e-f78a-41a1-81fe-09976241c96b" />
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
   <img width="1742" height="1479" alt="Arquitectura_Target_Planeada" src="https://github.com/user-attachments/assets/b8343393-0177-415c-a2c9-3b4887e28d9d" />
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

## **🤝 Contribución**

Este proyecto **acepta contribuciones** para completar las funcionalidades faltantes.  
Priorizamos *issues* relacionados con **estabilidad**, **documentación** y **pruebas**.  
Siga los **estándares de código existentes** al realizar *pull requests*.

## **📄 Licencia**

Proyecto bajo licencia **MIT**.  
Libre uso y modificación con atribución.  
Se invita a compartir mejoras con la comunidad para fortalecer el ecosistema de automatización.

⚠️ **NOTA:**  
Este proyecto está en **desarrollo activo**.  
Las funcionalidades pueden cambiar y algunas características planeadas **aún no están implementadas**.  
Considere esta documentación como una **guía del estado actual y visión futura**.
