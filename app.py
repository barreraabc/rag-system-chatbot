from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Ruta principal que sirve la interfaz de chat
@app.route('/')
def index():
    return render_template('chat.html')

# Endpoint para procesar los mensajes del chat
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Obtener el mensaje enviado desde el frontend
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Aquí puedes procesar el mensaje del usuario si es necesario
        # Por ahora simplemente devolvemos "Hola mundo"
        response = "Hola mundo"
        
        return jsonify({
            'success': True,
            'response': response,
            'user_message': user_message
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Crear la carpeta templates si no existe
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Ejecutar la aplicación en localhost:3000
    app.run(host='localhost', port=3000, debug=True)