import json
from datetime import datetime

# Import the centralized db instance from extensions.py
from src.extensions import db

class AdminUser(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Respondent(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.String(10), nullable=True)
    education = db.Column(db.String(100), nullable=True)
    occupation = db.Column(db.String(100), nullable=True)
    marital_status = db.Column(db.String(50), nullable=True)
    referral_source = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    test_started_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    test_completed_at = db.Column(db.DateTime, nullable=True)
    
    answers = db.relationship("src.models.models.Answer", foreign_keys="Answer.respondent_id", lazy=True)
    raw_scores = db.relationship("src.models.models.RawScore", foreign_keys="RawScore.respondent_id", lazy=True)
    t_scores = db.relationship("src.models.models.TScore", foreign_keys="TScore.respondent_id", lazy=True)
    
    report_html = db.Column(db.Text, nullable=True)
    report_pdf_path = db.Column(db.String(255), nullable=True)
    report_text_path = db.Column(db.String(255), nullable=True)
    t_scores_json_path = db.Column(db.String(255), nullable=True)

class Question(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

class Answer(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey("respondent.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    response = db.Column(db.String(10))

class Scale(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    
    true_items_json = db.Column(db.Text, nullable=True)
    false_items_json = db.Column(db.Text, nullable=True)
    
    k_factor_numeric = db.Column(db.Float, nullable=True)
    k_factor_string = db.Column(db.String(10), nullable=True)
                                                
    t_scores_male_json = db.Column(db.Text, nullable=True)
    t_scores_female_json = db.Column(db.Text, nullable=True)

    raw_scores = db.relationship("src.models.models.RawScore", foreign_keys="RawScore.scale_id", lazy=True)
    t_scores = db.relationship("src.models.models.TScore", foreign_keys="TScore.scale_id", lazy=True)

    def get_true_items(self):
        return json.loads(self.true_items_json) if self.true_items_json else []

    def get_false_items(self):
        return json.loads(self.false_items_json) if self.false_items_json else []

    def get_t_scores_male(self):
        return json.loads(self.t_scores_male_json) if self.t_scores_male_json else {}
    
    def get_t_scores_female(self):
        return json.loads(self.t_scores_female_json) if self.t_scores_female_json else {}

class RawScore(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey("respondent.id"), nullable=False)
    scale_id = db.Column(db.Integer, db.ForeignKey("scale.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    k_corrected_score = db.Column(db.Float, nullable=True)
    items_answered = db.Column(db.Integer, nullable=True) # Added items_answered field

class TScore(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey("respondent.id"), nullable=False)
    scale_id = db.Column(db.Integer, db.ForeignKey("scale.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)

