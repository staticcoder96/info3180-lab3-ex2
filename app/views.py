"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
import smtplib
from flask import render_template, request, redirect, url_for,flash
app.secret_key = 'secret_key'


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render the website's contact page"""
    """Send an email when a post request is made"""
    
    if request.method == 'POST':
        send_mail(request.form['name'],request.form['mail'], request.form['subject'], request.form['message'])
        flash('Message Sent')
        return redirect(url_for('home'))
        
    else:
        flash("Message not sent")
        
    return render_template('contact.html')
    


def send_mail(name,mail,sub,msg):
    
    from_addr = 'stephanieramsay6@gmail.com'
    
    name = request.form['name']
    mail = request.form['mail']
    sub = request.form['subject']
    msg = request.form['message']
    
    
    
    server = smtplib.SMTP('smtp.gmail.com',587) #error fixed
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_addr, password)
    
    BODY = '\r\n'.join(['To: %s' %mail,
        'From: %s' %from_addr,
        'Subject: %s' %sub,
        '',
        msg
        ])
        
    try:
            server.sendmail(from_addr, [mail], BODY)
            print 'EMAIL SENT'
    except:
            print 'ERROR Sending Email'
            
    server.quit()
        
    
    


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")