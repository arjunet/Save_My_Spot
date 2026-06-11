# Imports:
from plyer import gps
from kivy_garden.mapview import MapView
from carbonkivy.uix.screen import CScreen
from kivy.utils import platform
from carbonkivy.app import CarbonApp
# ----------------------------------------------------------------
class MapScreen(CScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creates the mapview
        self.mapview = MapView(zoom=15, lat=0, lon=0)
        self.add_widget(self.mapview)

        # Starts GPS
        if platform == "android":
            gps.configure(on_location=self.update_map_pos)
            gps.start()

        else:
            # Windows fallback
            self.current_lat = 0
            self.current_lon = 0

    def update_map_pos(self, **kwargs):
        # Update the pos on the map (if location changes)

        # Get the current coordinates
        self.current_lat = kwargs.get('lat')
        self.current_lon = kwargs.get('lon')
        
        if self.current_lat and self.current_lon:
            self.mapview.lat = self.current_lat
            self.mapview.lon = self.current_lon
            self.mapview.center_on(self.current_lat, self.current_lon)

class MainApp(CarbonApp):
    def build(self):
        # This tells Kivy to actually render your screen inside a window
        return MapScreen()

if __name__ == '__main__':
    MainApp().run()
