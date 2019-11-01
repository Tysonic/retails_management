import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from Cices_enterprise import App

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


App.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(App.config['UPLOAD_FOLDER'], filename))