## **Phase 1: The Bedrock (Deep Detail)**

This phase focuses on establishing a "Thin Vertical Slice" of the application: a working server, a connected database, and a successful deployment to Vercel.

### **1\. Project Initialization & Structure**

The AI must initialize a **FastAPI** (Python) project. FastAPI is chosen over Flask for its native `async` support, which is critical for handling AI streaming and scraping tasks within Vercel's 10s execution limits.

**Directory Structure to Implement:**

Plaintext  
/  
├── api/                \# Vercel entry point  
│   └── index.py        \# Main FastAPI entry  
├── core/               \# Business logic  
│   ├── scraper.py  
│   ├── analyzer.py  
│   └── ai\_engine.py  
├── database/           \# DB Models & Migrations  
│   ├── models.py  
│   └── session.py  
├── static/             \# Assets (CSS/JS)  
├── templates/          \# Jinja2 HTML Fragments  
│   ├── components/     \# HTMX partials  
│   └── layouts/        \# Base wrappers  
├── .env.example        \# Template for secrets  
├── requirements.txt    \# Dependencies  
└── vercel.json         \# Vercel config

### **2\. Database Schema (Industry Standard)**

We will use **PostgreSQL** (via Supabase or Neon.tech for the free tier). The AI must implement the `Users` and `Products` tables using **SQLAlchemy** with `alembic` for migrations.

**Core Requirements:**

* Use UUIDs for Primary Keys.  
* Implement `created_at` and `updated_at` timestamps on every table.  
* Ensure the `Products` table has a `JSONB` column for `metadata` to handle the varying data structures returned from scraping.

### **3\. Environment Variable Guardrails**

To prevent runtime errors, the AI must create a `config.py` that validates the existence of these keys at startup:

* `DATABASE_URL` (Postgres)  
* `GEMINI_API_KEY` (Google AI)  
* `UPSTASH_REDIS_URL` (For rate limiting/caching)  
* `SECRET_KEY` (For session signing)

### **4\. The "Base" UI (HTMX \+ Tailwind \+ DaisyUI)**

The AI will build the `base.html` using a CDN-first approach for rapid prototyping.

* **HTMX Config:** Set `hx-boost="true"` on the body to handle standard links as AJAX requests automatically.  
* **Loading States:** Implement a global `#loading-bar` that triggers on `htmx:beforeRequest` and hides on `htmx:afterRequest`.

### **5\. Implementation Steps for AI Coding Assistant**

\[\!IMPORTANT\] **Instructions for the Coding AI:**

1. **Initialize FastAPI:** Create a basic app in `api/index.py` that renders a "Hello World" template.  
2. **Database Connection:** Set up an asynchronous SQLAlchemy engine. Create a `/test-db` route that verifies the connection and returns a success/fail fragment via HTMX.  
3. **Template Engine:** Configure Jinja2 to look in the `/templates` directory. Create a base layout and an index page.  
4. **Vercel Config:** Create a `vercel.json` that routes all traffic to the FastAPI app.

**Vercel Configuration (`vercel.json`):**

JSON  
{  
  "rewrite": \[{ "source": "/(.\*)", "destination": "/api/index.py" }\]  
}

---

## **🚀 Deployment Instructions (Milestone 1\)**

After the AI completes the code for Phase 1, follow these steps to deploy:

1. **Install Vercel CLI:** `npm i -g vercel`  
2. **Login:** `vercel login`  
3. **Link Project:** `vercel link`  
4. **Add Secrets:** \* `vercel env add DATABASE_URL`  
   * `vercel env add GEMINI_API_KEY`  
5. **Deploy:** `vercel --prod`

---

### **🛠️ Technical Algorithm: The "Vercel Timeout" Pattern**

Since Vercel Free Tier limits functions to **10 seconds**, the AI must implement the **Polling Pattern** for all scraping and AI tasks.

* **Step A:** User submits URL.  
* **Step B:** Server triggers a background task (or creates a 'pending' DB record) and immediately returns an HTMX component.  
* **Step C:** The component contains `hx-get="/api/status/{id}" hx-trigger="every 2s"` to poll until the data is ready.

