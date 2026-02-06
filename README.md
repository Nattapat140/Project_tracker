# 📊 Project Progress Tracker

A beautiful, lightweight web application to track your projects, tasks, and weekly goals.

## Features

- 📁 **Project Management** - Track multiple projects with status, versions, and tasks
- 📅 **Weekly Tasks** - Keep track of this week's priorities
- 🎨 **Beautiful UI** - Warm, professional design with earthy color palette
- 💾 **Data Persistence** - All data stored in JSON file
- 🚀 **Easy Deployment** - Deploy to Streamlit Cloud for free 24/7 access

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`

## Deployment to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and branch
6. Set main file path to `app.py`
7. Click "Deploy"!

Your app will be live at `https://[your-app-name].streamlit.app`

## Updating Data

To update your progress, edit the `progress_data.json` file:

```json
{
  "lastUpdated": "2026-02-06",
  "projects": [
    {
      "name": "Your Project Name",
      "status": "In Progress",
      "versions": ["v1.0"],
      "tasks": ["Task 1", "Task 2"]
    }
  ],
  "weekTasks": [
    "Weekly task 1",
    "Weekly task 2"
  ]
}
```

After editing, commit and push to GitHub. Streamlit Cloud will auto-deploy your changes!

## Color Palette

- 🌾 Cream: `#F7F1DE`
- 🌿 Sage Green: `#8A9D85`
- 🧱 Terracotta: `#B87C4C`
- 🏜️ Tan: `#C4A484`

## License

Free to use and modify!
