from sqlalchemy.orm import Session
import models

def create_translation_task(db: Session, text: str, languages: list):
    task = models.TranslationTask(text=text, languages=languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_translation_task(db: Session, task_id: str):
    return db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()


def update_translation_task(db: Session, task_id: str, translations: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    task.translations = translations
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task
