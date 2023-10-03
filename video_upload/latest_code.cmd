@echo off
setlocal enabledelayedexpansion

rem Check if logged into Docker Hub
docker info | findstr /C:"ravi0000"

if errorlevel 1 (
    echo Not logged in to Docker Hub
    rem Log in to Docker Hub
    docker login -u ravi0000 -p Ravi#9780
    if errorlevel 1 (
        echo Failed to log in to Docker Hub
        exit /b 1
    ) else (
        echo Successfully logged in to Docker Hub
    )
) else (
    echo Logged in to Docker Hub as your_username
)

rem Set the branch name
set "branch_name=main"

rem Get the latest commit hash
for /f "tokens=*" %%a in ('git rev-parse !branch_name!') do (
    set "latest_commit_hash=%%a"
)

echo Latest commit hash of branch '%branch_name%': !latest_commit_hash!

docker-compose build
docker-compose up -d
docker tag video_upload-web:latest  ravi0000/video_upload-web:!latest_commit_hash!
docker push  ravi0000video_upload-web:!latest_commit_hash!
