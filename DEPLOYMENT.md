# 🚀 Deployment Guide

## Quick Deployment to Streamlit Cloud (Free 24/7 Hosting)

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done):
```bash
cd /Users/nattapat/Desktop/Proj_progress_Ball
git init
git add .
git commit -m "Initial commit: Progress Tracker"
```

2. **Create GitHub Repository**:
   - Go to [github.com](https://github.com) and create a new repository
   - Name it something like `progress-tracker`
   - Don't initialize with README (we already have one)

3. **Push to GitHub**:
```bash
git remote add origin https://github.com/YOUR_USERNAME/progress-tracker.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "Sign in with GitHub"

2. **Deploy Your App**:
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/progress-tracker`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"!

3. **Wait for Deployment** (usually 1-2 minutes)
   - Your app will be live at: `https://YOUR_USERNAME-progress-tracker.streamlit.app`

### Step 3: Share with Your Team Leader

Once deployed, share the URL with your team leader. The app will be:
- ✅ **Available 24/7**
- ✅ **Automatically updated** when you push changes to GitHub
- ✅ **Free to host** on Streamlit Cloud

---

## Updating Your Progress

### Method 1: Edit JSON File Directly

1. Edit `progress_data.json` on your computer
2. Commit and push to GitHub:
```bash
git add progress_data.json
git commit -m "Update progress"
git push
```
3. Streamlit Cloud will auto-deploy in ~1 minute

### Method 2: Edit on GitHub (Easiest)

1. Go to your repository on GitHub
2. Click on `progress_data.json`
3. Click the pencil icon (Edit)
4. Make your changes
5. Click "Commit changes"
6. Streamlit Cloud will auto-deploy!

### Method 3: Ask Me to Update

Just tell me what you want to update and I'll modify the `progress_data.json` file for you!

---

## Example: Updating Your Data

Edit `progress_data.json`:

```json
{
  "lastUpdated": "2026-02-07",
  "projects": [
    {
      "name": "New Project Name",
      "status": "In Progress",
      "versions": ["v1.0", "v1.1"],
      "tasks": [
        "Task 1",
        "Task 2",
        "Task 3"
      ]
    }
  ],
  "weekTasks": [
    "This week's task 1",
    "This week's task 2"
  ]
}
```

---

## Troubleshooting

**App not updating?**
- Check if your changes were pushed to GitHub
- Go to Streamlit Cloud dashboard and click "Reboot app"

**Want to change the design?**
- Edit `app.py` and push to GitHub
- Changes will auto-deploy

**Need help?**
- Just ask me! I can help you update data or fix any issues.

---

## Your App URLs (After Deployment)

- **Public URL**: `https://YOUR_USERNAME-progress-tracker.streamlit.app`
- **Streamlit Dashboard**: [share.streamlit.io](https://share.streamlit.io)
- **GitHub Repo**: `https://github.com/YOUR_USERNAME/progress-tracker`

Enjoy your 24/7 progress tracker! 🎉
