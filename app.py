from flask import Flask, render_template, request
from weather import main as fetch_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("cityName")
        state = request.form.get("stateName")
        
        # Fetch weather data for the given city and state
        weather_data = fetch_weather(city, state)

    return render_template("index.html", data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
