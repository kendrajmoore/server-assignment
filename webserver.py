from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<h1>Hello!</h1>
<p>I am Kendra. </p>
<br />
</br />
<a href="/bio">Read my Bio</a>
<a href="/socials">Connect with me through social media</a>'''

@app.route('/bio')
def bio():
    return '''
<h1>This is my bio!</h1>
<p>I am a first year student in the MIMS program located in the School of Information.
My interests include blockchain and system administration. My least favorite part of Berkeley
is the lack of reliable public transportation and I am too afraid to ride in bike in traffic.</p>
<br />
</br />
<a href="/socials">Let’s connect?</a>
'''

@app.route('/socials')
def socials():
    return '''
<a href="https://www.linkedin.com/in/kendrajmoore/">LinkedIn</a>
'''