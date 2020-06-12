from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/test/')
def test():
    return render_template("test.html")

@app.route('/rotation/')
def rotation():
    return render_template("rotation_download.html")

@app.route('/dombyra/')
def dombyra():
    return render_template("dombyra.html")
    
if __name__=="__main__":
    app.run(debug=True)