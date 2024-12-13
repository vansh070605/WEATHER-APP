# India Weather App

This is a simple web application that allows users to get real-time weather updates for various cities in India. It provides weather details like temperature, weather conditions, and weather icons fetched from the OpenWeather API.

## Features

- Select a state and city from dropdown menus.
- Fetches real-time weather data for the selected city.
- Displays weather details like temperature, weather description, and an icon representing the weather condition.
- Responsive design, optimized for different screen sizes.

## Technologies Used

- **HTML**: For the structure of the web pages.
- **CSS**: For styling the application, including Bootstrap for responsive design.
- **JavaScript**: For handling dynamic changes in the UI (city selection, API calls).
- **Flask** (Assumed as backend): Python web framework for handling routes and rendering data.
- **OpenWeather API**: Used for fetching real-time weather data.

## Prerequisites

- Python 3.x
- Flask
- Access to the OpenWeather API for weather data.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/india-weather-app.git
2. Navigate into the project directory:
   cd india-weather-app
3. Install the required dependencies using pip:
   pip install -r requirements.txt
4. Create an account on OpenWeather and get your API key from OpenWeather.
5. In the app.py (or your Flask app file), replace YOUR_API_KEY with your OpenWeather API key:
   api_key = 'YOUR_API_KEY'
6. Run the Flask app:
   python app.py
7. Open your browser and visit http://127.0.0.1:5000 to access the app.

## Directory Structure

india-weather-app/
│
├── app.py                # Flask backend application
├── templates/
│   └── index.html        # Main HTML page
├── static/
│   └── style.css         # Custom CSS (if any)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## How It Works
1. The user selects a state and city from the dropdown menus.
2. Upon submitting the form, the Flask app sends a request to the OpenWeather API with the selected city.
3. The API responds with the current weather data, which is then displayed on the page (city name, weather, temperature, and weather icon).
4. The weather icon is dynamically loaded based on the data from the API.

## Contributing
Contributions are welcome! If you find any bugs or would like to add features, feel free to open an issue or submit a pull request.

## License
This project is open-source and available under the MIT License.

### Key sections:

- **Introduction**: Describes the project and its functionality.
- **Features**: Lists key features of the weather app.
- **Technologies Used**: Highlights the technologies and frameworks used in the project.
- **Prerequisites**: Information on what is required to run the project.
- **Setup Instructions**: Steps to set up the app locally, including installation and configuration.
- **Directory Structure**: Explains the layout of files in the project.
- **How It Works**: Explains the flow of how the app functions.
- **Contributing**: Encourages contributions and explains how others can help improve the project.
- **License**: Information about the project's licensing.
