from . import lhubdb

class Posts(lhubdb.Model):
    id = lhubdb.Column(lhubdb.Integer, primary_key=True)
    fileLocation = lhubdb.Column(lhubdb.String(256))
    date = lhubdb.DateTime(lhubdb.String(256))
    uploadedById = lhubdb.Column(lhubdb.String(256))