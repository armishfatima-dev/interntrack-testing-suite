from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Submission, Intern
from app.schemas import SubmissionCreate, SubmissionResponse
from app.auth import get_current_user
from app.models import User

router = APIRouter(prefix="/submissions", tags=["Submissions"])

@router.post("/", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
def create_submission(
    submission: SubmissionCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    # Find or mock intern profile linked to user
    intern = db.query(Intern).filter(Intern.user_id == current_user.id).first()
    if not intern:
        # Auto-create intern profile for testing convenience if missing
        intern = Intern(name="Test Intern", track="Backend", user_id=current_user.id)
        db.add(intern)
        db.commit()
        db.refresh(intern)

    new_sub = Submission(
        title=submission.title,
        content=submission.content,
        intern_id=intern.id,
        status="pending"
    )
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub

@router.get("/", response_model=List[SubmissionResponse])
def get_submissions(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return db.query(Submission).all()

