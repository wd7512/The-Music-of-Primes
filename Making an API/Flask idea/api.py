from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/test')
def api_all():

    return render_template('test.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
