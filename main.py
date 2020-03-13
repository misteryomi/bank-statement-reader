from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import tabula

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        f = request.files['statement']
        tabula.convert_into(f, "./uploads/statement.csv", pages='all')
        return send_file("./uploads/statement.csv", as_attachment=True)
    else:
        # return 'Success'
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)