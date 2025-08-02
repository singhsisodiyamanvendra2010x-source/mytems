from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# In-memory product list
products = []

# Admin login details
ADMIN_USERNAME = "mytems.in"
ADMIN_PASSWORD = "mydrugsm1000"

@app.route('/')
def home():
    return render_template("home.html", products=products)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html")

@app.route('/orders')
def orders():
    return render_template("orders.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        products.append({
            'name': name,
            'price': price,
            'image': image
        })

    return render_template("admin_dashboard.html", products=products)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)