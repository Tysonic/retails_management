from Cices_enterprise import App,db
from flask import Blueprint,render_template,request
from werkzeug.utils import secure_filename
from Cices_enterprise import upload
import os


image_blueprint = Blueprint("ItemImage",__name__, template_folder="templates/images")
class Images(db.Model):
    Id = db.Column(db.Integer, primary_key =True)
    item_id = db.Column(db.Integer)
    image = db.Column(db.String)

    def __init__(self, item_id, image):
        self.image = image
        self.item_id = item_id

    def __repr__(self):
        return f"{self.item_id,self.image}"

@image_blueprint.route('/image upload', methods=["POST","GET"])
def uploader():
    if request.method=='POST':
        image_file = request.files['imagefile']
        file_name = secure_filename(image_file.filename)
        new_item = Images(item_id=1,image=file_name)
        db.session.add(new_item)
        image_file.save(os.path.join(upload, file_name))
        db.session.commit()
    return render_template('image_uploader.html')


@image_blueprint.route('/images image gallery')
def list_0f_images():
    images=Images.query.all()
