# Deployment Guide: Phase 3 Intelligence Engine

The application is now split into two parts:
1.  **Frontend (Vercel)**: Handles UI and API requests (Already Deployed).
2.  **Worker (Render/VPS)**: Handles background scraping and analysis (Needs Deployment).

## 1. Prerequisites
- A **GitLab** repository: [Create New Project](https://gitlab.com/projects/new) under `ohmyholy99-group` named `canyon-intel`.
- A [Render.com](https://render.com) account.
- Your `DATABASE_URL` (Neon) and `GEMINI_API_KEY`.

## 2. Deploy the Worker (Render)
> **Auto-Deployment Enabled**: This project includes a `render.yaml` Blueprint.

1.  **Render Dashboard**: Go to **Blueprints** -> New Blueprint Instance.
2.  **Source**: Connect your **GitLab** repository (`canyon-intel`).
3.  **Approve**: Render will detect `canyon-worker` from `render.yaml`.
4.  **Environment Variables**:
    Fill in the prompted values:
    - `DATABASE_URL`
    - `GEMINI_API_KEY`
    - `PYTHONPATH`: `/app`
5.  **Deploy**: Click "Apply". Render will build the Docker container automatically.

## 3. Verification
1.  Visit your Vercel App URL: `https://canyon-intel.vercel.app/scraper`
2.  Enter the Optech URL: `https://codecanyon.net/item/optech-it-service-and-business-consulting-laravel-script/57011612`
3.  Click **Analyze**.
4.  **Observe**:
    - The UI will show a "Pending" or "Finding product..." state.
    - Check your **Render Logs**: You should see "Processing Job...", followed by "Scraping...", then "Job Completed".
    - The Vercel UI will automatically update with the result correctly extracted (Price: $19.00).

## Troubleshooting
- **Logs**: Always check the Worker logs in Render dashboard.
- **Database**: Ensure both Vercel and Render are connecting to the same `DATABASE_URL`.
