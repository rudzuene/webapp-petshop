from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/shop')
def shop_front_view(): 
    products = [
        {
            "name": "Dog shampo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
        {
            "name": "Dog shampo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
        {
            "name": "Dog shampo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
        {
            "name": "Dog shampo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15,
            "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.zalora.com.ph%2Fpedigree-pedigree-adult-beef-vegetables-dry-dog-food-500g-n-a-1611655.html&psig=AOvVaw1JRcSbDODWjQwbZRqxCVtf&ust=1596671064323000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNjzgLDdgusCFQAAAAAdAAAAABAS"
        },
    ]

    return render_template("shopfront.html", products=products)


@app.route('/<nomber>')
def geeting(nomber):
    return render_template("shopfront.html", nomber=nomber)