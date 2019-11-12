import os
from flask import Blueprint, request, render_template, url_for
from werkzeug.utils import secure_filename, redirect
from Cices_enterprise import db, upload
from Cices_enterprise.Modules.Uploads import Images
from Cices_enterprise.Uploads.Forms import AddImage

image_blueprint = Blueprint("ItemImage",__name__, template_folder="templates/uploaders")
@image_blueprint.route('/image upload', methods=["POST","GET"])
def uploader():
    form = AddImage()
    if request.method=='POST':
        file = request.files['imagefile']
        filenames = secure_filename(file.filename)
        file.save(os.path.join(upload, filenames))
        return redirect(url_for("ItemImage.list_of_images"))
    return render_template('image_uploader.html', form=form)

@image_blueprint.route('/images image gallery')
def list_of_images():
    # images=Images.query.all()
    return "Image saved successfully"
