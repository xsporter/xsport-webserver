from flask import Flask, render_template, request

app = Flask(__name__)

# Sample product data (you can replace it with your own data)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 7.99},
    # Add more products...
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('search_query')

    # Perform search logic here (e.g., filtering products based on the query)
    search_results = []
    for product in products:
        if query.lower() in product['name'].lower():
            search_results.append(product)

    return render_template('search_results.html', query=query, results=search_results)

if __name__ == '__main__':
    app.run()
