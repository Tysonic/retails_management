import os
from flask import Blueprint, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename, redirect
from Cices_enterprise import db, upload
from Cices_enterprise.Modules.Uploads import Images
from Cices_enterprise.Uploads.Forms import AddImage

allowed_fie_type = ['JPG','PNG','JPEG','GIF']

image_blueprint = Blueprint("ItemImage",__name__, template_folder="templates/uploaders")
@image_blueprint.route('/image upload', methods=["POST","GET"])
def uploader():
    form = AddImage()
    if request.method=='POST':
        file = request.files['imagefile']
        filenames = secure_filename(file.filename)
        file.save(os.path.join(upload, filenames))
        new_item = Images(item_id=1,image=filenames, description= form.description.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("ItemImage.image_gallery"))
    return render_template('image_uploader.html', form=form)




@image_blueprint.route('/image gallery', methods=['POST','GET'])
def image_gallery():
    images=Images.query.all()
    return render_template("image_gallery.html",images=images)

@image_blueprint.route("/image list <filename> ")
def send_file(filename):
    return send_from_directory(".\Static\images", filename)
