from store import app
from flask import render_template


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/products")
def products():
    return render_template("product.html")

@app.route("/shopping-cart")
def shopping_cart():
    return render_template("shoping-cart.html")
