Este proyecto consiste en la construcción de un sistema RAG - chatbot.
Se empleará una arquitectura estándar de sistema RAG.
La respuesta del chatbot se formará mediante un agente principal, que recibirá la query del usuario, decidirá qué herramientas usar (RAG) para responder y construirá la respuesta final.
Para las respuestas finales obtenidas usando la herramienta de RAG, se determinará si es necesaria la introducción de un LLM que evalúe si la query del usuario está correctamente respondida en base a la información extraída con el RAG.
Se pretende analizar la precisión del sistema RAG para acotar la información que puede dar respuesta a la query del usuario.
En la parte del chatbot, se evaluará la importancia del esquema del prompt: En los artículos o cursos de creación de sistemas RAG - chatbot, no se explica en detalle dónde hay que situar la información extraida con el RAG dentro de la llamada al LLM, si en el system message o el user message.
