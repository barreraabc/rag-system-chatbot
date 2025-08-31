# Resumen
Este proyecto consiste en la construcción de un sistema RAG - chatbot.
Los objetivos puedes cambiar a lo largo del tiempo, pero a grandes rasgos, la idea es construir un sistema lo más semejante posible a uno que se pueda emplear en un ambiente productivo.
Para ello, el sistema tendrá que ser seguro, robusto, eficiente, escalable, de fácil mantenimiento... tomando las características tradicionales de lo que se llamaría un sistema productivo estándar.

En principio, se emplearán las opciones gratuitas de herramientas de pago que se usen en ambientes profesionales, y en su defecto, herramientas de software libre.
Alrededor de este proyecto, también se crearán ramas o repositorios derivados para analizar artículos relacionados con el sistema, técnicas especiales de RAG, prompting, etc.

La realización del proyecto incluye un gestor de tareas, un diario y una memoria. El diario debe recoger todas las acciones importantes relacionadas con el proyecto, así como cualquier información que sea de interés, sin ser demasiado riguroso. La memoria será un documento técnico en el que se recogerán explicaciones referentes al sistema (arquitectura, herramientas...), pero también análisis de artículos, pruebas, test, estadísticas...

# Objetivos (Luego los iré pasando al gestor de tareas)
* Analizar la precisión del sistema RAG para acotar la información que puede dar respuesta a la query del usuario.
* En la parte del chatbot, evaluar la importancia del esquema del prompt: En los artículos o cursos de creación de sistemas RAG - chatbot, no se explica en detalle dónde hay que situar la información extraida con el RAG dentro de la llamada al LLM, si en el system message o el user message.
* Buscar si hay técnicas de evaluación para decidir si la query del usuario está correctamente respondida en base a la información extraída con el RAG.
