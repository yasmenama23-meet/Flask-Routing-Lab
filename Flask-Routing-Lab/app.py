from flask import Flask, redirect, request, render_template, url_for


app = Flask(  __name__,
    template_folder='templates',  
    static_folder='static'  
)
@app.route('/')
def HELLO():
    return render_template("home.html")
@app.route('/c')
def clothes():
    return render_template("product.html")
    @app.route('/')
def HELLO():
    return render_template("cart.html")

if __name__ == "__main__": 
    app.run(debug=True)
