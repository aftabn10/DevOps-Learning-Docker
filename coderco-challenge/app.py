import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def welcome():
    return """
    <html>
    <head>
    <style>
            body {
                background-color: #0049B7;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                color: white;
            }
            h1 {
                font-weight: bold;
                margin-bottom: 20px;
            }
             p {
                font-size: 14px;
                margin-bottom: 40px;
                font-weight:400;
                color: #f4f3f1;
            }
            .button-container {
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            a.button {
                display: inline-block;
                padding: 15px 30px;
                font-size: 16px;
                color: white;
                background-color: #003B94;
                border: 2px solid #f4f3f1;
                border-radius: 8px;
                text-decoration: none;
                text-transform: capitalize;
                transition: all 0.2s ease-in-out;
            }
            a.button:hover {
                font-weight:bold;
            }
            a.button:active {
                background-color: #003B94;
            }
        </style>
    </head>
    <body>
    <div class="container">
            <h1>MediaDezines: EazyTracker</h1>
            <p>Track how many times this page has been visited and learn more about the challenge below.</p>
            <div class="button-container">
                <a class="button" href="/count">View Count</a>
                <a class="button" href="/about">About</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/count")
def count():
    visits = r.incr('visits')
    return f"""
    <html>
    <head>
    <style>
        body {{
                background-color: #0049B7;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                color: white;
            }}
            h1 {{
                font-weight: bold;
                margin-bottom: 20px;
            }}
             p {{
                font-size: 14px;
                margin-bottom: 40px;
                font-weight:400;
                color: #f4f3f1;
            }}
            .button-container {{
                display: flex;
                justify-content: center;
                gap: 20px;
            }}
            a.button {{
                display: inline-block;
                padding: 15px 30px;
                font-size: 16px;
                color: white;
                background-color: #003B94;
                border: 2px solid #f4f3f1;
                border-radius: 8px;
                text-decoration: none;
                text-transform: capitalize;
                transition: all 0.2s ease-in-out;
            }}
            a.button:hover {{
                font-weight:bold;
            }}
            a.button:active {{
                background-color: #68756D;
            }}
    </style>
    <div class="container">
        <h1>This page has been visited {visits} times.</h1>
            <div class="button-container">
                <a class="button" href="/count">Reload</a>
                <a class="button" href="/">Home</a>
            </div>
        </div>
    </body>
    </head>
    </html>
    """

@app.route("/about")
def about():
    return """
    <html>
    <head>
    <style>
            body {
                background-color: #0049B7;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                color: white;
            }
            h1 {
                font-weight: bold;
                margin-bottom: 20px;
            }
             p {
                font-size: 14px;
                margin-bottom: 40px;
                font-weight:400;
                color: #f4f3f1;
            }
            </style>
    </head>
    <body>
    <div class="container">
    <h1>About Us Page</h1>
    <p>Brief explanation about us...</p>
    </div>
    </body>
    </html>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)