from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status
from repositories.jobs import JobsRepository
from schemas.jobs import Job, JobIn
from schemas.user import User
from .depends import get_job_repository, get_current_user


router = APIRouter()


@router.get("/", response_model=List[Job])
async def read_jobs(
    limit: int = 100,
    skip: int = 0,
    jobs: JobsRepository = Depends(get_job_repository)):
    return await jobs.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Job)
async def create_job(
    j: JobIn, 
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    return await jobs.create(user_id=current_user.id, j=j)

@router.put("/", response_model=Job)
async def update_job(
    id: int,
    j: JobIn, 
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    job = await jobs.get_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return await jobs.update(id=id, user_id=current_user.id, j=j)

@router.delete("/")
async def delete_job(id: int,
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    job = await jobs.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if job is None or job.user_id != current_user.id:
        raise not_found_exception
    result = await jobs.delete(id=id)
    return {"status": True}