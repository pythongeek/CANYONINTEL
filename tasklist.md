**In an HTMX-centric world, the traditional "Frontend vs. Backend" divide is blurred because your server is actually your UI engine—it returns HTML fragments, not just JSON. To get this live on Vercel while staying within their serverless execution limits, we’ll start with the Engine (Backend & Data) first. Without the data and the scraper, the UI has nothing to "swap" in.**

**Here is your production-ready, segment-wise task list to take this from localhost to the finish line.**

---

## **Segment 1: The Engine (Foundation, DB & Scraping)**

***Before we paint the walls, we need to lay the pipes.***

| Task ID | Component | Task Description |
| :---- | :---- | :---- |
| **1.1** | **Infrastructure** | **Initialize Flask/Python project with Vercel configuration (vercel.json) and environment variables.** |
| **1.2** | **Data Layer** | **Set up Supabase (PostgreSQL) and run the initial schema migrations from agent.md.** |
| **1.3** | **Scraper Core** | **Build the CodeCanyonScraper service using BeautifulSoup and Requests. *Note: We'll avoid Playwright for the Vercel Free Tier if possible due to binary size/execution limits.*** |
| **1.4** | **The Algorithm** | **Implement the ProfitabilityAnalyzer logic in Python to calculate the weighted scores.** |
| **1.5** | **Auth System** | **Implement Flask-Login or Supabase Auth for user sessions.** |

---

## **Segment 2: The Shell (HTMX Interface & Dashboard)**

***This is where the app starts "feeling" real using partial HTML updates.***

* **2.1 Base Template & Tailwind: Create the master base.html with Tailwind CSS, HTMX, and Alpine.js (for minor client-side toggles) as specified in ui.md.**  
* **2.2 HTMX Partial Routing: Set up Flask routes that detect HX-Request headers to return only the necessary HTML fragments instead of full pages.**  
* **2.3 Search & Discovery: \* Build the advanced search sidebar with HTMX filters.**  
  * **Implement Live Search using hx-trigger="keyup delay:500ms".**  
* **2.4 The Scraping Dashboard: \* Create the URL input UI.**  
  * **Implement Polling (hx-trigger="every 2s") so users can watch the scraping progress in real-time.**  
* **2.5 Analysis Panels: Integrate Chart.js within HTMX fragments to render the radar charts for profitability breakdown.**

---

## **Segment 3: The Brain (AI Integration & Planning)**

***Adding the "Intelligence" that makes this platform high-value.***

* **3.1 Claude API Bridge: Connect the AIRecommendationService to the Anthropic API.**  
* **3.2 Streamed Insights: Use Server-Sent Events (SSE) or progressive HTMX swaps to "stream" the AI recommendations so the user isn't staring at a blank screen while Claude thinks.**  
* **3.3 Project Planner Wizard: \* Build the 6-step multi-part form for the Project Planner using HTMX to swap steps without page reloads.**  
  * **Implement the "Save to Dashboard" logic for user-created projects.**  
* **3.4 Market Research: Integrate the Google Custom Search API to provide "grounding" data for the AI analysis.**

---

## **Segment 4: The Finish Line (Optimization & Deployment)**

***Polishing for a 2026 production standard.***

**Important Note on Vercel Free Tier: We must ensure our background tasks (like heavy scraping) don't hit the 10-second execution timeout. We will use Upstash Redis for lightweight rate limiting and caching.**

* **4.1 Global Caching: Implement Redis caching for search results and profitability scores to save on API costs and database hits.**  
* **4.2 Rate Limiting: Add the @rate\_limit\_check decorator to protect your Claude API credits from abuse.**  
* **4.3 UI Polish: Add skeleton loaders (shimmer effect) and toast notifications for a premium feel.**  
* **4.4 SEO & Metadata: Generate dynamic meta tags for product pages to make them shareable on social media.**  
* **4.5 Vercel Launch: Deploy, configure custom domains, and set up Vercel Cron Jobs for daily market trend updates.**

