from flask import Flask, render_template, request
from seo import analyze_seo

app = Flask(__name__)

@app.route('/seo', methods=['GET', 'POST'])
def seo():
    if request.method == 'POST':
        url = request.form['url']
        result = analyze_seo(url)
        return render_template('seo.html', result=result)
    return render_template('seo.html')
