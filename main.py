from replit import web
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "FUUUUUUUUUUUCCCCCKKK RAAAAAHHHHHH"

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

# if the file is being executed directly and not as a module...
if __name__ == "__main__":
    web.run(app)