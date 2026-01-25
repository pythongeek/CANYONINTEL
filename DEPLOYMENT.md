# Deployment Guide: Phase 3 Intelligence Engine

The application is now split into two parts:
1.  **Frontend (Vercel)**: Handles UI and API requests (Already Deployed).
2.  **Worker (Render/VPS)**: Handles background scraping and analysis (Needs Deployment).

## 1. Prerequisites
- A GitHub repository linked to this project.
- A [Render.com](https://render.com) account (or any VPS provider).
- Your `DATABASE_URL` (Neon) and `GEMINI_API_KEY`.

## 2. Deploy the Worker (Render)
1.  **New Web Service**: Go to Render Dashboard -> New -> Web Service.
2.  **Source**: Connect your GitHub repository.
3.  **Runtime**: Select **Docker**.
4.  **Region**: Choose a region close to your database (e.g. US East).
5.  **Environment Variables**:
    Add the following keys:
    - `DATABASE_URL`: (Your connection string from Neon/Supabase)
    - `GEMINI_API_KEY`: (Your Google AI Studio Key)
    - `PYTHONPATH`: `/app`
6.  **Deploy**: Click "Create Web Service".

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
