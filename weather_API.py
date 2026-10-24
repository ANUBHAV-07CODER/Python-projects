
import sys
import requests
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QLineEdit,
                        QPushButton,
                        QVBoxLayout,
                        QGridLayout,
                        QFrame
)

from PyQt5.QtCore import Qt
class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setFixedSize(430, 510)

        self.setStyleSheet("""
            QWidget {
                background-color: #101827;
                color: white;
                font-family: Arial;
            }

            QLabel#title {
                font-size: 27px;
                font-weight: bold;
                color: #7DD3FC;
            }

            QLineEdit {
                background-color: #1F2B40;
                border: 1px solid #3B4B65;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
            }

            QPushButton {
                background-color: #0284C7;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #0369A1;
            }

            QFrame#card {
                background-color: #1F2B40;
                border-radius: 10px;
            }

            QLabel#value {
                font-size: 21px;
                font-weight: bold;
                color: #7DD3FC;
            }

            QLabel#label {
                font-size: 12px;
                color: #CBD5E1;
            }
        """)

        self.title = QLabel("Weather Dashboard")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name...")
        self.city_input.returnPressed.connect(self.check_weather)

        self.search_button = QPushButton("Check Weather")
        self.search_button.clicked.connect(self.check_weather)

        self.city_label = QLabel("Search for a city")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.temperature_label = QLabel("-- °C")
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet(
            "font-size: 46px; font-weight: bold; color: #7DD3FC;"
        )

        self.condition_label = QLabel("Current weather")
        self.condition_label.setAlignment(Qt.AlignCenter)
        self.condition_label.setStyleSheet("font-size: 16px;")

        self.details = QGridLayout()
        self.details.setSpacing(12)

        self.humidity_card, self.humidity_value = (
            self.create_card("Humidity", "-- %")
        )
        self.feels_card, self.feels_value = (
            self.create_card("Feels Like", "-- °C")
        )
        self.wind_card, self.wind_value = (
            self.create_card("Wind Speed", "-- km/h")
        )
        self.time_card, self.time_value = (
            self.create_card("Local Observation", "--")
        )

        self.details.addWidget(self.humidity_card, 0, 0)
        self.details.addWidget(self.feels_card, 0, 1)
        self.details.addWidget(self.wind_card, 1, 0)
        self.details.addWidget(self.time_card, 1, 1)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("color: #FBBF24;")

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 22, 25, 22)
        layout.setSpacing(15)

        layout.addWidget(self.title)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.city_label)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.condition_label)
        layout.addLayout(self.details)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def create_card(self, title, initial_value):
        card = QFrame()
        card.setObjectName("card")

        card_layout = QVBoxLayout()

        heading = QLabel(title)
        heading.setObjectName("label")
        heading.setAlignment(Qt.AlignCenter)

        value = QLabel(initial_value)
        value.setObjectName("value")
        value.setAlignment(Qt.AlignCenter)

        card_layout.addWidget(heading)
        card_layout.addWidget(value)
        card.setLayout(card_layout)

        return card, value

    def check_weather(self):
        city = self.city_input.text().strip()

        if not city:
            self.status_label.setText("Please enter a city name.")
            return

        self.search_button.setEnabled(False)
        self.search_button.setText("Fetching weather...")
        self.status_label.setText("Connecting to weather service...")

        try:
            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search"
            )

            geo_params = {
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            }

            geo_response = requests.get(
                geo_url,
                params=geo_params,
                timeout=10
            )
            geo_response.raise_for_status()

            geo_data = geo_response.json()
            results = geo_data.get("results", [])

            if not results:
                self.status_label.setText(
                    "City not found. Try another spelling."
                )
                return

            place = results[0]
            latitude = place["latitude"]
            longitude = place["longitude"]

            weather_url = (
                "https://api.open-meteo.com/v1/forecast"
            )

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "timezone": "auto"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params,
                timeout=10
            )
            weather_response.raise_for_status()

            weather_data = weather_response.json()
            current = weather_data["current"]
            code = current["weather_code"]

            if code == 0:
                condition = "Clear Sky"
            elif code in (1, 2, 3):
                condition = "Partly Cloudy"
            elif code in (45, 48):
                condition = "Foggy"
            elif code in (51, 53, 55, 56, 57):
                condition = "Drizzle"
            elif code in (61, 63, 65, 66, 67):
                condition = "Rainy"
            elif code in (71, 73, 75, 77):
                condition = "Snowy"
            elif code in (80, 81, 82):
                condition = "Rain Showers"
            elif code in (85, 86):
                condition = "Snow Showers"
            elif code in (95, 96, 99):
                condition = "Thunderstorm"
            else:
                condition = "Weather Conditions Unavailable"

            self.city_label.setText(
                f"{place['name']}, "
                f"{place.get('country', '')}"
            )

            self.temperature_label.setText(
                f"{current['temperature_2m']} °C"
            )

            self.condition_label.setText(condition)

            self.humidity_value.setText(
                f"{current['relative_humidity_2m']} %"
            )

            self.feels_value.setText(
                f"{current['apparent_temperature']} °C"
            )

            self.wind_value.setText(
                f"{current['wind_speed_10m']} km/h"
            )

            self.time_value.setText(
                current.get("time", "--").replace("T", "\n")
            )

            self.status_label.setText("Weather updated successfully!")

        except requests.RequestException:
            self.status_label.setText(
                "Unable to fetch weather. Check your internet "
                "connection and try again."
            )

        except (KeyError, ValueError, TypeError):
            self.status_label.setText(
                "Unexpected weather data. Please try again."
            )

        finally:
            self.search_button.setEnabled(True)
            self.search_button.setText("Check Weather")


app = QApplication(sys.argv)

window = WeatherApp()
window.show()

sys.exit(app.exec_())
