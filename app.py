from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from settings import Settings

import asyncio
import os
app = Flask(__name__)
socketio = SocketIO(app)
settings = Settings(socketio)
#settings.socketio = socketio
settings.generators = [
    #WeatherDataSource(settings.weather_api_key),

]
#print(WeatherDataSource(settings.weather_api_key))
@app.route('/settings', methods=['GET'])
def get_settings():
    return jsonify(settings.to_dict())
@app.route('/settings', methods=['POST'])
def update_settings():
    settings.update(request.form)
    if 'logo' in request.files:
        logo = request.files['logo']
        logo_path = os.path.join('uploads', 'logo.png')
        logo.save(logo_path)
        settings.logo_path = logo_path
    if 'images' in request.files:
        settings.images = []
        for image in request.files.getlist('images'):
            image_path = os.path.join('uploads', image.filename)
            image.save(image_path)
            settings.images.append(image_path)
    socketio.emit('settingsUpdate', settings.to_dict())
    return '', 200
@app.route('/start', methods=['GET'])
def start_info_board():
    settings.info_board_running = True
    socketio.emit('settingsUpdate', settings.to_dict())
    return jsonify({"status": "started"})
@app.route('/stop', methods=['GET'])
def stop_info_board():
    settings.info_board_running = False
    socketio.emit('settingsUpdate', settings.to_dict())
    return jsonify({"status": "stopped"})
@socketio.on('connect')
def handle_connect():
    emit('settingsUpdate', settings.to_dict())
async def send_data():
    while True:
        if settings.info_board_running:
            data = {
                "weather": settings.generators[0].get_data(),
                #"news": settings.generators[1].get_data()
            }
            socketio.emit('dataUpdate', data)
        await asyncio.sleep(settings.update_interval)
async def update_content(self):
    while True:
        html = await self.generators[self.current_index].generate_html()
        socketio.emit('htmlUpdate', {'html': html})
        self.current_index = (self.current_index + 1) % len(self.generators)
        await asyncio.sleep(self.interval / 1000)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_data())
    loop.create_task(settings.update_content())
    socketio.run(app, port=3000)