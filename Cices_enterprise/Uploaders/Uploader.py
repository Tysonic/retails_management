import os
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask import Blueprint
from wtforms import FileField, SubmitField

from Cices_enterprise import upload, basedir


uploader_blueprint = Blueprint("Uploader",__name__, template_folder="templates/uploaders")


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
class AddImage(FlaskForm):
    image = FileField("Select File to Upload")
    submit = SubmitField("Upload")


@uploader_blueprint.route('/upload', methods = ['POST','GET'])
def upload_image():
    image = AddImage()
    if request.method == 'POST':
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        file = request.files['imagefile']
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file:
        filenames = secure_filename(file.filename)
        file.save(os.path.join(upload, filenames))
        return  redirect(url_for("Items.list_of_items"))
    return render_template("image_uploader.html", image=image)