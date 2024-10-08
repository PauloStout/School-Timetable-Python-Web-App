from flask import render_template_string
from app import app
import main

# Define the HTML as a string
html_template = """
<!doctype html>
<html>
    <head>
    <style>
        /* Move content higher on the page */
        body {
            margin: 7px;
            padding: 0;
        }
        
        /* Center the container and adjust its position */
        .container {
            margin: 0 auto;
            padding-top: 5px; /* Move the container closer to the top */
            width: 100%;
            text-align: center; /* Center the content horizontally */
        }
        
        /* Reduce the gap between h2 and h3 */
        h1, h2 {
            margin: 0; /* Removes default margin */
            padding: 0px 0; /* Adds slight padding if needed */
            font-size: 33px;
            font-family: 'Inter UI', sans-serif;
        }
        
        /* You can further adjust the gap here if needed */
        h1 {
            margin-bottom: 0px; /* Adjust this value as needed */
        }
        
        h2 {
            margin-top: 0px; /* Adjust this value as needed */
        }
    </style>

        <title>{{ title }}</title>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <div class="info-container">
            <h1>{{ current_info }}</h1>
            <h2>{{ next_info }}</h2>
        </div>
    </body>
</html>
"""

@app.route('/')  # Route for the root URL
@app.route('/home')  # Route for the /home URL
def index():
    current_info, next_info, TOD = main.get_schedule_info()
    return render_template_string(html_template, title='YC-Timetable', current_info=current_info, next_info=next_info)

def run_app():
    app.run(host='127.0.0.1', port=5000)  # Run Flask app

if __name__ == '__main__':
    run_app()  # Ensure this is only called once
