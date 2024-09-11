#!/bin/bash

# Variables
LOCAL_REPO_PATH="/Users/ranga/Face-Recognition-From-Crowd"
REMOTE_REPO_NAME="Face-Recognition-From-Crowd"
GITHUB_USERNAME="spandaai"

# Step 1: Create a new repository on GitHub
echo "Creating a new GitHub repository..."
gh repo create ${GITHUB_USERNAME}/${REMOTE_REPO_NAME} --public --confirm

# Step 2: Navigate to the local repository
cd ${LOCAL_REPO_PATH}

# Step 3: Initialize git (if not initialized)
if [ ! -d ".git" ]; then
  echo "Initializing Git in local repository..."
  git init
fi

# Step 4: Add remote origin
echo "Adding remote origin..."
git remote add origin https://github.com/${GITHUB_USERNAME}/${REMOTE_REPO_NAME}.git

# Step 5: Add all files to git
echo "Adding files to git..."
git add .

# Step 6: Commit the files
echo "Committing files..."
git commit -m "Initial commit"

# Step 7: Push to the remote repository
echo "Pushing files to GitHub..."
git branch -M main
git push -u origin main

echo "Successfully pushed to https://github.com/${GITHUB_USERNAME}/${REMOTE_REPO_NAME}.git"

