from flask import Flask, render_template, request
import os  # For compatibility with deployment environments

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/products')
def products():
    return render_template('products.html', title='Our Products')

@app.route('/services')
def services():
    return render_template('services.html', title='Our Services')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission (save data or send an email)
        return "Message Sent!"
    return render_template('contact.html')

if __name__ == '__main__':
    # Use environment variables for host and port compatibility with deployment
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
