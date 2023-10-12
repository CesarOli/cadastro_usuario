from app import app, db
import models.address_model

with app.app_context():

    db.create_all()
