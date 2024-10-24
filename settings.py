import asyncio
class Settings:
    def __init__(self,socketio):
        self.socketio = socketio
        self.update_interval = 50000
        self.interval = 5000
        self.mode = 'sequential'
        self.logo = 'path/to/logo.png'
        self.rss_feed = 'https://www.braunschweiger-zeitung.de/rss'
        self.weather_api_key = ''
        self.images = []
        self.info_board_running = False
        self.current_index = 0
        self.generators = []
    def to_dict(self):
        return {
            'update_interval': self.update_interval,
            'interval': self.interval,
            'mode': self.mode,
            'logo': self.logo,
            'rssFeed': self.rss_feed,
            'images': self.images,
            'info_board_running': self.info_board_running
            #'weatherApiKey': self.weather_api_key
        }
    def update(self, new_settings):
        self.__dict__.update(new_settings)
        if 'update_interval' in new_settings:
            self.update_interval = int(new_settings['update_interval'])
        if 'logo' in new_settings:
            self.logo_path = new_settings['logo']
        if 'images' in new_settings:
            self.images = new_settings['images']
        if 'info_board_running' in new_settings:
            self.info_board_running = new_settings['info_board_running']
    async def update_content(self):
            while True:
                html = await self.generators[self.current_index].generate_html()
                self.socketio.emit('htmlUpdate', {'html': html})
                self.current_index = (self.current_index + 1) % len(self.generators)
                await asyncio.sleep(self.interval / 1000)