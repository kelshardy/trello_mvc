from init import db, ma 
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date created
    status = db.Column(db.String)
    priority = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', back_populates='cards')
    
    # { id: 1, "Card 1", "description": "Card 1 desc", user: { id: 3, nsame: "User 1" } }
    
class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    
    class Meta:
        fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user')
        ordered = True
        
card_schema = CardSchema()
cards_schema = CardSchema(many=True)