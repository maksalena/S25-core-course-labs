import os
import asyncio
from datetime import datetime

import pytz
from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define global variables
counter_lock = asyncio.Lock()
visits_file_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "../data/visits.txt"
)

# Ensure the visits file exists
if not os.path.exists(visits_file_path):
    with open(visits_file_path, "w") as f:
        f.write("0")


# Define a route for the root URL ("/")
@app.route("/")
async def moscow_time():
    """
    Handles requests to the root URL. Retrieves and displays the
    current time in the Moscow timezone.
    """
    await add_visit()

    # Set the timezone to Moscow
    moscow_tz = pytz.timezone("Europe/Moscow")

    # Get the current date and time in the Moscow timezone
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

    # Return the current time as an HTML response
    return f"<h1>Current Moscow Time: {current_time}</h1>"


@app.route("/visits")
async def get_visits():
    try:
        with open(visits_file_path, "r") as f:
            visits = f.readline().strip()
            if not visits:
                visits = 0
            else:
                visits = int(visits)
    except IOError:
        visits = 0

    return jsonify(visits=visits)


async def add_visit():
    async with counter_lock:
        try:
            with open(visits_file_path, "r") as f:
                visits = f.readline().strip()
                if not visits:
                    visits = 1
                else:
                    visits = int(visits) + 1
        except IOError:
            visits = 1

        with open(visits_file_path, "w") as f:
            f.write(str(visits))


# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
