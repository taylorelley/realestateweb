from flask import Flask, render_template

class WebInterface:
    def __init__(self):
        self.app = Flask(__name__)

    def display_results(self, results):
        # Display the results on the web interface
        @self.app.route('/')
        def home():
            return render_template('index.html', results=results)

        self.app.run(debug=True)
