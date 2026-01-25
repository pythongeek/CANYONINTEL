# **CodeCanyon Intelligence Platform \- Complete UI/UX Design Documentation**

## **🎨 Design System & Visual Identity**

---

## **📋 Document Purpose**

This comprehensive design document provides detailed instructions for creating a production-ready, advanced-level interactive interface for the CodeCanyon Intelligence Platform. This document is intended for AI design assistants, UI/UX designers, and frontend developers to create a cohesive, modern, and highly functional user interface.

---

## **🎯 Design Philosophy & Principles**

### **Core Design Values**

**1\. Data-Driven Clarity**

* Information should be immediately scannable  
* Complex data presented through clear visualizations  
* Progressive disclosure: show summaries first, details on demand  
* Visual hierarchy guides users to important insights

**2\. Professional & Trustworthy**

* Clean, modern aesthetic that conveys expertise  
* Subtle animations that feel premium, not gimmicky  
* Consistent spacing and alignment throughout  
* Professional color palette that inspires confidence

**3\. Interactive Intelligence**

* Real-time feedback for all user actions  
* Micro-interactions that make the interface feel alive  
* Smart defaults that anticipate user needs  
* Contextual help and guidance where needed

**4\. Performance-Oriented**

* Fast-loading interfaces with skeleton states  
* Optimistic UI updates  
* Smooth transitions and animations  
* Progressive enhancement approach

---

## **🎨 Visual Design System**

### **Color Palette**

**Primary Colors**

* **Primary Blue**: `#2563EB` (Brand color, CTAs, links)  
  * Light variant: `#60A5FA`  
  * Dark variant: `#1E40AF`  
  * Use for: Primary buttons, active states, key metrics  
* **Secondary Purple**: `#7C3AED` (Accent, AI features)  
  * Light variant: `#A78BFA`  
  * Dark variant: `#5B21B6`  
  * Use for: AI recommendation badges, premium features

**Semantic Colors**

* **Success Green**: `#10B981`  
  * Use for: Positive metrics, success states, growth indicators  
* **Warning Amber**: `#F59E0B`  
  * Use for: Caution states, medium priority alerts  
* **Danger Red**: `#EF4444`  
  * Use for: Error states, negative metrics, critical alerts  
* **Info Cyan**: `#06B6D4`  
  * Use for: Information tooltips, neutral notifications

**Neutral Palette**

* **Background**: `#F9FAFB` (Light gray for main background)  
* **Surface**: `#FFFFFF` (Card backgrounds)  
* **Border**: `#E5E7EB` (Subtle dividers)  
* **Text Primary**: `#111827` (Main content)  
* **Text Secondary**: `#6B7280` (Supporting text)  
* **Text Tertiary**: `#9CA3AF` (Placeholder text)

**Gradient Accents**

* **Hero Gradient**: Linear gradient from `#2563EB` to `#7C3AED` at 135deg  
* **Success Gradient**: Linear gradient from `#10B981` to `#059669`  
* **Card Hover**: Subtle gradient overlay with 3% opacity

### **Typography System**

**Font Families**

* **Primary**: "Inter" (Headings, UI elements, body text)  
  * Weights: 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold)  
  * Excellent readability for data-heavy interfaces  
* **Monospace**: "JetBrains Mono" (Code snippets, technical data)  
  * Use for: Technology tags, API responses, code examples

**Type Scale**

* **Display**: 48px / 3rem (Hero sections, major headings)  
  * Line height: 1.1  
  * Font weight: 700  
* **H1**: 36px / 2.25rem (Page titles)  
  * Line height: 1.2  
  * Font weight: 700  
* **H2**: 30px / 1.875rem (Section headers)  
  * Line height: 1.3  
  * Font weight: 600  
* **H3**: 24px / 1.5rem (Card titles, subsections)  
  * Line height: 1.4  
  * Font weight: 600  
* **H4**: 20px / 1.25rem (Component headers)  
  * Line height: 1.4  
  * Font weight: 600  
* **Body Large**: 18px / 1.125rem (Feature descriptions)  
  * Line height: 1.6  
  * Font weight: 400  
* **Body**: 16px / 1rem (Standard content)  
  * Line height: 1.5  
  * Font weight: 400  
* **Body Small**: 14px / 0.875rem (Secondary info, labels)  
  * Line height: 1.5  
  * Font weight: 400  
* **Caption**: 12px / 0.75rem (Metadata, timestamps)  
  * Line height: 1.4  
  * Font weight: 400

### **Spacing System**

**Base Unit**: 4px

**Spacing Scale**

* **XS**: 4px (Tight spacing within components)  
* **SM**: 8px (Related elements)  
* **MD**: 16px (Component padding, card spacing)  
* **LG**: 24px (Section spacing)  
* **XL**: 32px (Major section breaks)  
* **2XL**: 48px (Page-level spacing)  
* **3XL**: 64px (Hero sections)

**Container Widths**

* **Full Width**: 100% (Dashboard sections)  
* **Wide**: 1400px (Main content area)  
* **Standard**: 1200px (Centered content)  
* **Narrow**: 800px (Forms, articles)  
* **Reading**: 600px (Long-form text)

### **Border Radius System**

* **None**: 0px (Tables, data grids)  
* **Small**: 4px (Tags, badges, small buttons)  
* **Medium**: 8px (Cards, inputs, standard buttons)  
* **Large**: 12px (Modals, large cards)  
* **XL**: 16px (Hero cards, feature sections)  
* **Full**: 9999px (Pills, circular avatars)

### **Shadow System**

**Elevation Levels**

* **Shadow SM**:

 0 1px 2px 0 rgba(0, 0, 0, 0.05)

Use for: Subtle card elevation, input focus states

* **Shadow MD**:

 0 4px 6px \-1px rgba(0, 0, 0, 0.1),

  0 2px 4px \-1px rgba(0, 0, 0, 0.06)

Use for: Default card state, dropdowns

* **Shadow LG**:

 0 10px 15px \-3px rgba(0, 0, 0, 0.1),

  0 4px 6px \-2px rgba(0, 0, 0, 0.05)

Use for: Modals, popovers, hover states

* **Shadow XL**:

 0 20px 25px \-5px rgba(0, 0, 0, 0.1),

  0 10px 10px \-5px rgba(0, 0, 0, 0.04)

Use for: Large modals, floating action buttons

* **Shadow 2XL**:

 0 25px 50px \-12px rgba(0, 0, 0, 0.25)

Use for: Hero sections, important notifications

**Colored Shadows**

* **Primary Glow**: Same as Shadow MD but with `rgba(37, 99, 235, 0.2)` for primary actions  
* **Success Glow**: Same as Shadow MD but with `rgba(16, 185, 129, 0.2)` for success states

### **Animation & Transition Standards**

**Timing Functions**

* **Default**: `cubic-bezier(0.4, 0, 0.2, 1)` \- Smooth, natural feeling  
* **Sharp**: `cubic-bezier(0.4, 0, 0.6, 1)` \- Quick entries  
* **Deceleration**: `cubic-bezier(0.0, 0, 0.2, 1)` \- Elements entering screen  
* **Acceleration**: `cubic-bezier(0.4, 0, 1, 1)` \- Elements leaving screen

**Duration Scale**

* **Instant**: 100ms (Color changes, simple state toggles)  
* **Fast**: 200ms (Button hovers, dropdown reveals)  
* **Normal**: 300ms (Card animations, page transitions)  
* **Slow**: 500ms (Complex multi-step animations)  
* **Slower**: 700ms (Page-level transitions)

**Common Animations**

* **Fade In**: Opacity 0 → 1, 300ms  
* **Slide Up**: Transform translateY(20px) → 0, 300ms  
* **Scale In**: Transform scale(0.95) → 1, 200ms  
* **Bounce**: Scale 1 → 1.05 → 1, 400ms (for success actions)

---

## **🏗️ Layout Structure**

### **Overall Application Layout**

**Three-Panel Dashboard Layout**

┌─────────────────────────────────────────────────────────────────┐  
│                       TOP NAVIGATION BAR                        │  
│                         (Height: 64px)                          │  
├─────────┬───────────────────────────────────────────────────────┤  
│         │                                                       │  
│         │                                                       │  
│  SIDE   │                                                       │  
│  BAR    │            MAIN CONTENT AREA                          │  
│         │                                                       │  
│ (280px) │                                                       │  
│         │                                                       │  
│  Fixed  │               Scrollable                              │  
│         │                                                       │  
│         │                                                       │  
│         │                                                       │

└─────────┴───────────────────────────────────────────────────────┘

**Responsive Breakpoints**

* **Mobile**: \< 640px (Collapsed sidebar, stacked layout)  
* **Tablet**: 640px \- 1024px (Collapsible sidebar, 2-column grids)  
* **Desktop**: 1024px \- 1440px (Full sidebar, 3-column grids)  
* **Large Desktop**: \> 1440px (Wider containers, 4-column grids)

---

## **📱 Top Navigation Bar Design**

### **Navigation Bar Structure**

**Left Section** (Logo & Quick Actions)

* **Logo Area**:  
  * Brand logo (40px height)  
  * Platform name "CodeCanyon Intelligence" in 18px semibold  
  * Gradient text effect on hover  
  * Click returns to dashboard  
* **Quick Search** (On desktop):  
  * Universal search input (300px width)  
  * Placeholder: "Search products, categories, features..."  
  * Icon: Magnifying glass (left-aligned)  
  * Keyboard shortcut badge: "⌘K" or "Ctrl+K"  
  * Rounded border, subtle shadow  
  * Expands to 400px on focus  
  * Shows search suggestions dropdown on typing

**Center Section** (Main Navigation)

* Navigation tabs with icons:  
  * **Dashboard** \- Home icon  
  * **Discover** \- Compass icon  
  * **Analytics** \- Chart icon  
  * **Projects** \- Folder icon  
  * **Research** \- Telescope icon  
* Tab styling:  
  * Inactive: Gray text, no background  
  * Hover: Light blue background (5% opacity)  
  * Active: Primary blue text, blue bottom border (3px)  
  * Smooth transition: 200ms

**Right Section** (User & System Controls)

* **Notification Bell**:  
  * Bell icon (20px)  
  * Red dot badge for unread (animated pulse)  
  * Dropdown shows recent notifications  
  * Click marks all as read  
* **API Usage Indicator**:  
  * Circular progress ring  
  * Shows percentage of daily quota used  
  * Color changes: Green → Amber → Red  
  * Tooltip shows exact numbers  
* **User Menu**:  
  * User avatar (36px, circular)  
  * Initials if no photo  
  * Dropdown on click:  
    * Profile  
    * Settings  
    * Billing (with tier badge)  
    * Documentation  
    * Divider  
    * Logout

**Styling Details**

* Background: White with subtle bottom border  
* Box shadow: SM elevation  
* Sticky positioning (stays visible on scroll)  
* Backdrop blur on semi-transparent overlay (when modals open)  
* Z-index: 1000 (always on top)

---

## **🗂️ Sidebar Navigation Design**

### **Sidebar Structure & Sections**

**Header Section** (Top of sidebar)

* **Profile Summary Card**:  
  * Avatar (48px, circular, gradient border)  
  * Username (16px, semibold)  
  * Subscription tier badge ("Free", "Pro", "Enterprise")  
  * Badge colors match tier (gray, blue, purple)  
  * Hover: Subtle scale effect, shows "View Profile"

**Primary Navigation** (Main menu items)

**Section 1: Discovery**

* **Dashboard**  
  * Icon: Grid of 4 squares  
  * Badge: New insights count (if any)  
* **Product Search**  
  * Icon: Magnifying glass  
  * Sub-items (expandable):  
    * Browse All  
    * Trending  
    * Top Rated  
    * Recent Launches  
* **URL Scraper**  
  * Icon: Link chain  
  * Badge: Shows pending scrapes

**Section 2: Analysis**

* **Analyze Product**  
  * Icon: Chart with magnifying glass  
  * Quick action button  
* **Comparison Tool**  
  * Icon: Side-by-side rectangles  
  * Badge: Number of items in comparison (max 4\)  
* **Market Trends**  
  * Icon: Trending up arrow  
  * Sub-items:  
    * By Category  
    * By Technology  
    * Emerging Niches

**Section 3: AI Features**

* **AI Recommendations**  
  * Icon: Sparkles/star with glow effect  
  * Purple accent color  
  * "AI" badge on icon  
* **Smart Research**  
  * Icon: Brain or robot  
  * Purple accent  
  * Shows "Beta" tag

**Section 4: Projects**

* **My Projects**  
  * Icon: Folder  
  * Badge: Active projects count  
* **Create New Project**  
  * Icon: Plus in circle  
  * Prominent blue color  
  * Slightly larger than other items

**Section 5: Resources**

* **Documentation**  
  * Icon: Book  
* **API Access**  
  * Icon: Code brackets  
  * Shows "Pro" lock if free tier  
* **Help & Support**  
  * Icon: Question mark in circle

**Footer Section** (Bottom of sidebar)

* **Upgrade CTA** (for free/pro users):  
  * Gradient background card  
  * "Unlock Full Potential" headline  
  * Feature bullets  
  * "Upgrade Now" button  
  * Dismissable  
* **Quick Stats Summary**:  
  * Analyses Used: X/10 (progress bar)  
  * Scrapes Remaining: X/5  
  * Mini chart icon linking to detailed usage

**Styling Details**

* Background: Dark blue gradient (`#1E293B` to `#0F172A`)  
* Text: White with varying opacity  
* Width: 280px (fixed)  
* Padding: 24px  
* Item spacing: 8px between items, 24px between sections  
* Hover state: Light blue background (10% white opacity)  
* Active state: Brighter blue background, left border accent (3px)  
* Icons: 20px, consistent positioning  
* Expandable sections: Smooth accordion animation (300ms)  
* Scrollable: If content exceeds viewport height  
* Collapse button: Hamburger icon at top (mobile/tablet)

**Mobile Behavior**

* Overlay sidebar (slides in from left)  
* Dark overlay on main content (50% black opacity)  
* Click outside to close  
* Swipe left to close  
* Animation: Slide \+ fade, 300ms

---

## **🎯 Dashboard Main Content Design**

### **Dashboard Header Section**

**Welcome Banner**

* **Layout**: Full-width gradient card  
* **Background**: Hero gradient (blue to purple)  
* **Content**:  
  * Greeting text: "Welcome back, \[User Name\]" (32px, white, semibold)  
  * Subtitle: Dynamic message based on time/activity  
    * Morning: "Let's discover your next profitable product"  
    * Afternoon: "X new products analyzed today"  
    * Evening: "Review today's insights"  
  * Date/time display (subtle, top-right)  
* **Quick Actions Row**:  
  * 3-4 large action buttons (horizontal layout)  
  * Button 1: "Scrape New Product" (primary blue)  
  * Button 2: "Browse Trending" (secondary)  
  * Button 3: "Generate Report" (outline)  
  * Icon \+ text layout  
  * Hover: Lift effect (translateY \-2px, larger shadow)

**Key Metrics Row** (4 stat cards)

**Stat Card Structure** (each):

* White background card  
* Shadow: MD elevation  
* Padding: 24px  
* Border radius: 12px  
* Hover: Lift effect \+ shadow increase

**Metric 1: Total Products Analyzed**

* Large number display (48px, bold, primary blue)  
* Label below (14px, gray)  
* Small trend indicator: "+12% vs last week"  
* Icon: Magnifying glass chart (top-right, subtle, large, 10% opacity)  
* Sparkline graph (bottom): Last 7 days trend

**Metric 2: Average Profitability Score**

* Large number (48px, bold, success green or amber based on value)  
* Out of 100 indicator  
* Circular progress ring background (subtle)  
* Icon: Target bullseye

**Metric 3: Total Revenue Potential**

* Dollar amount (48px, bold, success green)  
* Formatted with commas  
* Icon: Money stack  
* Small calculator icon link: "How we calculate"

**Metric 4: Active Projects**

* Number of projects (48px, bold, purple)  
* Icon: Folder with star  
* Quick link: "View All Projects"

**Card Animations**

* Stagger appearance: Each card fades in sequentially (100ms delay between)  
* Initial state: Opacity 0, translateY 20px  
* Final state: Opacity 1, translateY 0  
* Duration: 400ms

### **Dashboard Main Grid Layout**

**2-Column Responsive Grid**

* Desktop: 2 columns (60% / 40% split)  
* Tablet: Stacks to single column  
* Gap: 24px between cards

---

## **📊 Left Column Components**

### **Component 1: Recent Product Analysis**

**Card Structure**

* **Header**:  
  * Title: "Recent Analyses" (20px, semibold)  
  * Filter dropdown: "Last 7 Days" (right-aligned)  
  * View all link: "See All" (blue, right)

**Product List** (5 most recent items)

**Each Product Row**:

* **Left Section**:  
  * Product thumbnail (64px × 64px, rounded-lg, shadow-sm)  
  * Fallback: Gradient background with category icon  
* **Middle Section**:  
  * Product title (16px, semibold, 2-line clamp)  
  * Category badge (small, gray background)  
  * Metadata row:  
    * Price tag: "$X"  
    * Sales count: "X sales"  
    * Rating: Stars (filled/half/empty)  
    * Separator dots between items  
* **Right Section**:  
  * Large profitability score circle:  
    * Number (24px, bold)  
    * Colored by score (red \< 50, amber 50-70, green \> 70\)  
    * Background: Colored circle (10% opacity)  
  * "View Analysis" link (appears on hover)

**Row Styling**:

* Padding: 16px  
* Border bottom: 1px, light gray  
* Hover: Light blue background, cursor pointer  
* Transition: 200ms  
* Click: Opens product detail view

**Empty State** (if no analyses):

* Illustration: Magnifying glass with document  
* Message: "No products analyzed yet"  
* CTA button: "Analyze Your First Product"

### **Component 2: Trending Categories Chart**

**Card Structure**

* **Header**:  
  * Title: "Trending Categories" (20px, semibold)  
  * Time period selector: Tabs (7D, 30D, 90D, 1Y)

**Chart Visualization**

* **Type**: Horizontal bar chart  
* **Data**: Top 10 categories by profitability score change  
* **Bars**:  
  * Height: 32px each  
  * Gradient fill (subtle)  
  * Rounded ends  
  * Animated fill (left to right, 500ms, staggered)  
* **Labels**:  
  * Left: Category name (14px, semibold)  
  * Right: Score value (16px, bold, colored)  
  * Percentage change badge: "↑ 12%" (green) or "↓ 5%" (red)  
* **Interactive**:  
  * Hover: Bar highlights, tooltip shows details  
  * Click: Filters product search by category

**Styling**:

* Padding: 24px  
* Background: White  
* Chart area: 400px height  
* Responsive: Reduces to 6 categories on mobile

### **Component 3: Technology Trends**

**Card Structure**

* **Header**:  
  * Title: "Hot Technologies" (20px, semibold)  
  * Subtitle: "Most mentioned in top products"

**Tag Cloud Visualization**

* **Layout**: Flexible wrap grid  
* **Each Tag**:  
  * Technology name (e.g., "React", "Vue.js", "Laravel")  
  * Size varies by popularity:  
    * Small: 12px (emerging)  
    * Medium: 16px (popular)  
    * Large: 24px (dominant)  
  * Color: Gradient from blue to purple based on trend  
  * Background: Subtle colored background (10% opacity)  
  * Padding: 8px 16px  
  * Border radius: Full (pill shape)  
  * Shadow: SM on hover  
* **Interactive**:  
  * Hover: Scale 1.05, shadow increase  
  * Click: Shows products using this technology  
* **Animation**:  
  * Tags fade in randomly (cloud formation effect)  
  * Duration: 600ms  
  * Stagger: 50ms between tags

**Stats Tooltip** (on hover):

* Number of products using tech  
* Average profitability score  
* Growth percentage

---

## **📈 Right Column Components**

### **Component 1: AI Insights Panel**

**Card Structure**

* **Header**:  
  * Icon: Sparkles (animated subtle glow)  
  * Title: "AI-Powered Insights" (20px, semibold)  
  * "AI" badge (purple gradient)

**Insight Cards** (3-4 rotating insights)

**Each Insight**:

* **Icon Area**:  
  * Colored background circle (48px)  
  * Relevant icon (lightbulb, chart up, target, etc.)  
* **Content Area**:  
  * Insight title (16px, semibold)  
  * Description (14px, 3-line max)  
  * Confidence indicator: Progress bar (green)  
  * Action link: "Explore" or "Learn More"

**Insight Types**:

1. **Market Opportunity**: "WordPress plugins show 45% YoY growth"  
2. **Feature Gap**: "Mobile responsiveness missing in 30% of top products"  
3. **Pricing Sweet Spot**: "Products priced $49-$69 have highest ROI"  
4. **Emerging Niche**: "AI-powered form builders gaining traction"

**Styling**:

* Gradient border (subtle, purple)  
* Inner padding: 20px  
* Space between insights: 16px  
* Smooth slide transition when rotating (if animated)

### **Component 2: Quick Actions Card**

**Card Structure**

* **Title**: "Quick Actions" (18px, semibold)

**Action Buttons** (Large, stacked vertically)

**Button 1: Scrape Product**

* Icon: Link chain  
* Primary blue background  
* Full width  
* Large padding (16px)  
* Text: "Scrape CodeCanyon URL"  
* Hover: Darker blue, lift effect

**Button 2: Compare Products**

* Icon: Side-by-side boxes  
* Secondary (outline) style  
* Text: "Compare 2-4 Products"  
* Badge: Shows items in comparison (e.g., "2 selected")

**Button 3: Generate Report**

* Icon: Document with download  
* Secondary style  
* Text: "Export Analysis Report"  
* Dropdown arrow (format options on click)

**Button 4: Start New Project**

* Icon: Plus circle  
* Purple gradient background  
* Slightly larger than others (emphasis)  
* Text: "Plan New Product"

**Styling**:

* Buttons: 16px vertical spacing  
* Icon size: 24px  
* Text: 16px, semibold  
* Border radius: 8px  
* Transition: All 200ms

### **Component 3: Activity Feed**

**Card Structure**

* **Header**:  
  * Title: "Recent Activity" (18px, semibold)  
  * Filter: "All Activity" dropdown

**Timeline List**

**Activity Item Structure**:

* **Timeline Line**: Vertical line connecting items (left side)  
* **Timeline Dot**: Colored circle (12px) on line  
  * Color varies by activity type  
  * Animated pulse on newest item  
* **Activity Card**:  
  * **Icon**: Type-specific icon in colored circle (32px)  
  * **Content**:  
    * Action description (14px): "Analyzed Slider Revolution"  
    * Timestamp (12px, gray): "2 hours ago"  
    * Optional metadata: Score, category, etc.  
  * **Action Link**: "View" (appears on hover)

**Activity Types**:

1. **Product Analyzed** (Blue)  
2. **Recommendation Generated** (Purple)  
3. **Product Compared** (Green)  
4. **Project Created** (Orange)  
5. **Export Generated** (Gray)

**Styling**:

* Max height: 400px  
* Scrollable (custom scrollbar)  
* Item padding: 12px  
* Hover: Light background  
* Last item: No bottom border

**Empty State**:

* Illustration: Clock with checkmark  
* Message: "No recent activity"  
* Subtle, centered

### **Component 4: Usage Quota Widget**

**Card Structure**

* **Title**: "Your Usage" (18px, semibold)  
* **Tier Badge**: Current subscription (prominent)

**Quota Meters** (3 items)

**Each Meter**:

* **Label**: Feature name (14px, semibold)  
  * "Product Analyses"  
  * "URL Scrapes"  
  * "AI Recommendations"  
* **Progress Bar**:  
  * Background: Light gray  
  * Fill: Gradient based on usage  
    * \< 50%: Green  
    * 50-80%: Amber  
    * 80%: Red

  * Height: 8px  
  * Rounded ends  
  * Smooth animated fill  
* **Stats Row**:  
  * Used count (left): "7 used"  
  * Remaining (right): "3 remaining"  
  * 12px, gray text

**Upgrade CTA** (if near limit or free tier):

* Gradient background  
* Icon: Rocket  
* Text: "Upgrade for unlimited access"  
* Button: "See Plans"  
* Compact, bottom of card

**Styling**:

* Border: 2px gradient (subtle pulse if near limit)  
* Padding: 20px  
* Meter spacing: 20px vertical

---

## **🔍 Advanced Product Search Interface**

### **Search Page Layout**

**Three-Section Layout**:

┌──────────────────────────────────────────────────────┐  
│              SEARCH HEADER & FILTERS                 │  
├──────────┬───────────────────────────────────────────┤  
│          │                                           │  
│ FILTERS  │         PRODUCT GRID                      │  
│ SIDEBAR  │         (Results)                         │  
│          │                                           │  
│ (320px)  │                                           │  
│          │                                           │

└──────────┴───────────────────────────────────────────┘

### **Search Header Section**

**Search Bar Component**

* **Layout**: Centered, prominent position  
* **Width**: 800px max, 90% on mobile  
* **Height**: 56px  
* **Styling**:  
  * Large input field  
  * Left icon: Magnifying glass (20px)  
  * Placeholder: "Search by product name, category, or technology..."  
  * Right side: Clear button (X) when text present  
  * Border: 2px, primary blue on focus  
  * Shadow: MD elevation, increases on focus  
  * Border radius: 12px

**Search Suggestions Dropdown**

* **Trigger**: After 2 characters typed  
* **Layout**: Below search bar, full width  
* **Sections**:  
  1. **Recent Searches** (top):  
     * Clock icon  
     * Last 5 searches  
     * Delete individual items  
  2. **Suggested Products**:  
     * Mini product cards  
     * Image thumbnail (40px)  
     * Title \+ category  
     * Score badge  
  3. **Popular Searches**:  
     * Trending icon  
     * Clickable search terms

**Active Filters Display**

* **Position**: Below search bar  
* **Layout**: Horizontal scrollable chip row  
* **Each Filter Chip**:  
  * Category/filter name \+ value  
  * X close button  
  * Blue background  
  * White text  
  * Pill shape  
  * Hover: Darker background  
  * Animation: Scale in when added, fade out when removed

**Results Count & Sort**

* **Left**: "Showing X results" (14px, gray)  
* **Right**: Sort dropdown  
  * Options: Relevance, Score (High/Low), Sales (High/Low), Price (Low/High), Newest  
  * Current selection shown  
  * Dropdown icon

### **Filters Sidebar Design**

**Sidebar Header**

* **Title**: "Filters" (20px, semibold)  
* **Clear All Button**: (14px, blue, right-aligned)  
* **Divider**: Below header

**Filter Sections** (Collapsible accordions)

**Section 1: Category Filter**

* **Header**: "Category" \+ expand/collapse icon  
* **Content**:  
  * Search within categories input (small)  
  * Hierarchical checkbox tree:  
    * Parent category (bold)  
      * Subcategories (indented, lighter)  
    * Product count next to each (gray, in parentheses)  
  * "Show more" link if \> 5 categories

**Section 2: Price Range**

* **Header**: "Price Range"  
* **Content**:  
  * Dual-range slider:  
    * Track: Gray  
    * Active range: Blue gradient  
    * Thumb handles: Circular, white, shadow  
    * Smooth drag interaction  
  * Min/Max input fields:  
    * Dollar sign prefix  
    * Number input  
    * Linked to slider  
  * Quick presets:  
    * Under $20  
    * $20 \- $50  
    * $50 \- $100  
    * $100+  
    * Clickable chips

**Section 3: Profitability Score**

* **Header**: "Profitability Score"  
* **Content**:  
  * Single range slider (minimum score)  
  * Visual indicator: Color changes with score  
  * Quick presets:  
    * Excellent (80+)  
    * Good (60-79)  
    * Average (40-59)  
    * All

**Section 4: Sales Volume**

* **Header**: "Total Sales"  
* **Content**:  
  * Range slider  
  * Logarithmic scale visualization  
  * Presets:  
    * 0-100 (New)  
    * 100-500 (Growing)  
    * 500-2000 (Popular)  
    * 2000+ (Best Seller)

**Section 5: Rating**

* **Header**: "Minimum Rating"  
* **Content**:  
  * Star rating selector (clickable stars)  
  * Display: 5 stars, fill based on selection  
  * Minimum reviews input (optional)  
  * Label: "At least X reviews"

**Section 6: Launch Date**

* **Header**: "Launch Date"  
* **Content**:  
  * Date range picker (calendar dropdown)  
  * Presets:  
    * Last 30 days  
    * Last 6 months

Continue

5:54 PM  
\- Last year  
\- Last 2 years

\- All time

* Custom range option

**Section 7: Last Updated**

* **Header**: "Last Updated"  
* **Content**: Same as launch date

**Section 8: Technologies**

* **Header**: "Technologies Used"  
* **Content**:  
  * Search tech input  
  * Popular tech tags (multi-select):  
    * React, Vue.js, Laravel, WordPress, etc.  
    * Checkbox style  
    * Icon for each tech  
  * "Show more" for full list  
  * Selected count badge on header

**Section 9: Features**

* **Header**: "Key Features"  
* **Content**:  
  * Checkbox list:  
    * Responsive Design  
    * Admin Panel  
    * Documentation  
    * Updates Included  
    * etc.  
  * Search features input

**Sidebar Styling**:

* Background: Light gray (`#F9FAFB`)  
* Padding: 24px  
* Section spacing: 20px  
* Smooth accordion animations  
* Sticky scroll (filters stay visible)  
* Mobile: Overlay drawer (slide from left)

### **Product Grid Results**

**Grid Layout**

* **Desktop**: 3 columns  
* **Tablet**: 2 columns  
* **Mobile**: 1 column  
* **Gap**: 24px between cards

**Product Card Design** (Comprehensive)

**Card Structure**:

* **Container**:  
  * Background: White  
  * Border radius: 12px  
  * Shadow: MD elevation  
  * Hover: Shadow LG \+ translateY(-4px)  
  * Transition: All 300ms  
  * Cursor: Pointer

**Card Sections**:

**1\. Image Section** (Top)

* **Height**: 200px  
* **Image**:  
  * Product screenshot/thumbnail  
  * Object-fit: Cover  
  * Lazy loading  
* **Overlay** (appears on hover):  
  * Dark gradient overlay (bottom to top)  
  * Quick action buttons:  
    * "Quick View" (eye icon)  
    * "Add to Compare" (checkbox icon)  
    * "Bookmark" (heart icon)  
  * Smooth fade in (200ms)  
* **Badges** (Top-left corner):  
  * "New" badge (green) if \< 30 days  
  * "Trending" badge (orange) if trending  
  * "Featured" badge (purple) if featured  
  * Positioned absolutely, stacked

**2\. Content Section**

* **Padding**: 20px

**Title Row**:

* Product title (18px, semibold, primary color)  
* 2-line clamp (truncate with...)  
* Hover: Underline

**Category Row**:

* Category icon (16px)  
* Category name (14px, gray)  
* Breadcrumb style (Category › Subcategory)

**Author Row**:

* Small avatar (24px, circular)  
* Author name (14px, gray)  
* Verified badge (if applicable)

**Stats Row** (Icon \+ number pairs):

* **Sales**: Cart icon \+ "X sales" (14px)  
* **Rating**: Star icon \+ "X.X" \+ "(X reviews)"  
* Horizontal layout, space between

**Technology Tags Row**:

* Horizontal scrollable row  
* Small tech chips:  
  * Icon \+ name  
  * 12px text  
  * Subtle background  
  * Border radius: Full  
  * Max 3 visible, "+X more" badge

**3\. Metrics Section**

* **Divider**: Subtle line

**Profitability Score** (Prominent):

* **Large Circle**:  
  * Score number (32px, bold)  
  * Circular progress ring background  
  * Color: Score-based (red/amber/green)  
  * Size: 80px diameter  
  * Centered  
* **Score Label**: "Profitability Score" (12px, gray, centered)

**Quick Metrics Grid** (2x2 grid):

* **Revenue Potential**: "$X/month" (green)  
* **Sales Velocity**: "X/day" (blue)  
* **Market Saturation**: "Low/Med/High" (colored)  
* **Update Frequency**: "Active/Moderate/Slow" (colored)  
* Each: Icon \+ label \+ value  
* 12px text  
* Compact layout

**4\. Action Section** (Bottom)

* **Divider**: Subtle line  
* **Price Display**:  
  * Large price (24px, bold, success green)  
  * Left aligned  
* **Action Buttons** (Right aligned):  
  * "Analyze" button (primary, blue)  
  * Dropdown arrow (more options):  
    * View Details  
    * Add to Comparison  
    * Generate AI Insights  
    * Export Data

**Loading State**:

* Skeleton cards with animated shimmer  
* Same layout as real cards  
* Gray placeholder blocks  
* Pulse animation

**Empty State**:

* Centered illustration (search with sad magnifying glass)  
* Message: "No products found"  
* Suggestions:  
  * "Try adjusting your filters"  
  * "Browse trending products instead"  
* CTA button: "Clear Filters"

### **Pagination Component**

**Layout**: Bottom of page, centered

**Elements**:

* **Previous Button**: Left arrow icon \+ "Previous"  
* **Page Numbers**:  
  * Current page: Highlighted (blue background, white text)  
  * Other pages: Gray text, hover blue  
  * Ellipsis (...) for skipped ranges  
  * Example: 1 ... 5 \[6\] 7 ... 20  
* **Next Button**: "Next" \+ right arrow icon  
* **Items per Page**: Dropdown (20, 40, 60, 100\)  
* **Go to Page**: Small input \+ "Go" button

**Styling**:

* Buttons: 40px height, rounded  
* Spacing: 8px between elements  
* Shadow: SM on buttons  
* Hover: Background color change  
* Active page: Primary blue gradient

**Infinite Scroll Option**:

* Toggle in settings  
* Loading spinner at bottom when loading more  
* "Load More" button alternative

---

## **📦 Product Detail Page Design**

### **Page Layout**

**Hero Section** (Full-width)

* **Background**: Subtle gradient (very light blue to white)  
* **Content**: Constrained to 1200px

**Breadcrumb Navigation**

* Home › Search › Category › Product Name  
* 14px, gray, with separators  
* Clickable links (blue on hover)  
* Top-left of hero section

**Product Hero** (2-column layout)

**Left Column \- Image Gallery** (50%)

* **Main Image**:  
  * Large display (600px height)  
  * Product screenshot/demo  
  * Border radius: 8px  
  * Shadow: LG  
  * Lightbox on click (fullscreen view)  
* **Thumbnail Strip**:  
  * Below main image  
  * Horizontal scrollable row  
  * 4-6 thumbnails visible  
  * Each: 100px × 75px  
  * Active thumbnail: Blue border (3px)  
  * Click to change main image  
  * Smooth transition  
* **Action Buttons Row**:  
  * "View Live Demo" (primary button, blue)  
  * "Download Sample" (secondary, outline)  
  * Icons in buttons

**Right Column \- Product Info** (50%)

* **Product Title**: 36px, bold, primary color  
* **Rating & Sales Row**:  
  * Star rating (large, 24px stars)  
  * Rating number: "4.8" (18px, bold)  
  * Review count: "(234 reviews)" (14px, gray, link)  
  * Separator  
  * Sales badge: "2,341 sales" (14px, with icon)  
* **Author Card**:  
  * Avatar (48px, circular)  
  * Author name (16px, semibold, link)  
  * "Elite Author" badge (if applicable)  
  * Follow button  
  * Background: Light gray, padding, rounded  
* **Price Section**:  
  * Large price: "$49" (48px, bold, success green)  
  * License type: "Regular License" (14px, gray)  
  * Info icon (tooltip: license details)  
* **Key Features List** (Bullet points):  
  * Check icons (green)  
  * Top 5-6 features  
  * 14px text  
  * Compact spacing  
* **Technology Tags**:  
  * Horizontal wrap layout  
  * Each tag: Icon \+ name  
  * Colored backgrounds (tech-specific)  
  * Clickable (filters by tech)  
* **Meta Information Grid**:  
  * 2-column grid  
  * Launch Date: "XX"  
  * Last Update: "XX"  
  * Version: "XX"  
  * Compatible With: "XX"  
  * 12px labels, 14px values  
* **Action Buttons** (Large, stacked):  
  * "Analyze This Product" (primary, full-width)  
    * Icon: Chart magnifying glass  
    * Blue gradient background  
    * Large (56px height)  
  * "Add to Comparison" (secondary, outline)  
  * "Generate AI Insights" (purple gradient)  
  * "Export Details" (outline)

### **Tabs Section**

**Tab Navigation** (Sticky on scroll)

* Horizontal tab bar  
* Tabs:  
  * Overview  
  * Profitability Analysis  
  * AI Recommendations  
  * Similar Products  
  * Reviews  
  * Changelog  
* **Styling**:  
  * Active tab: Blue bottom border (3px), bold text  
  * Inactive: Gray text  
  * Hover: Light blue background  
  * Smooth slide indicator  
  * Background: White  
  * Shadow: SM when sticky

**Tab Content Areas**

**Tab 1: Overview**

* **Description Section**:  
  * Rich text content  
  * Formatted HTML  
  * Expandable (show more/less)  
  * Max height: 400px before expansion  
* **Features Grid**:  
  * 3-column grid  
  * Each feature: Icon \+ name \+ description  
  * Card style  
  * Hover: Subtle lift  
* **Screenshots Gallery**:  
  * Masonry grid layout  
  * Lightbox on click  
  * Captions below each  
* **Documentation Links**:  
  * If available  
  * External link icons

**Tab 2: Profitability Analysis**

**Score Dashboard**

* **Large Score Display** (Centered):  
  * Circular gauge (200px diameter)  
  * Animated fill  
  * Score number (64px, bold)  
  * Color gradient based on score  
  * Label below  
* **Score Breakdown Cards** (Grid):  
  * 5 metric cards (from analysis)  
  * Each card:  
    * Icon (colored)  
    * Metric name  
    * Score value (large number)  
    * Out of 100 indicator  
    * Small chart/progress bar  
    * Explanation tooltip

**Detailed Metrics Section**

* **Revenue Potential Chart**:  
  * Line chart (time series)  
  * Projected vs actual (if data available)  
  * Chart.js implementation  
  * Hover: Tooltip with exact values  
* **Market Position Chart**:  
  * Radar/spider chart  
  * Compare to category average  
  * Multiple dimensions  
* **Competitive Landscape**:  
  * Scatter plot  
  * X-axis: Price  
  * Y-axis: Sales  
  * Bubble size: Profitability score  
  * This product highlighted  
  * Competitors as bubbles  
* **Feature Comparison Matrix**:  
  * Table layout  
  * Rows: Features  
  * Columns: This Product | Top Competitor 1 | Top Competitor 2  
  * Checkmarks and X marks  
  * Green for competitive advantage

**Trend Analysis Section**

* **Sales Trend Graph**:  
  * Line chart (estimated monthly sales)  
  * Time range selector (6M, 1Y, 2Y, All)  
* **Review Trend**:  
  * Bar chart (reviews over time)  
  * Sentiment color coding

**Recommendations Summary**

* Quick bullets  
* Action items based on analysis  
* Link to AI tab for details

**Tab 3: AI Recommendations**

**Loading State** (if not generated):

* "Generate AI Insights" button (prominent)  
* Icon: Sparkles  
* Purple gradient  
* Subtitle: "Get personalized recommendations from AI"

**Generated State**:

**Recommendations Grid** (2-column)

**Column 1: Opportunities**

* **Feature Gaps Card**:  
  * Title: "Missing Features"  
  * List of 5 features competitors have  
  * Each feature:  
    * Feature name (bold)  
    * Brief description  
    * Impact indicator (High/Medium/Low)  
    * Number of competitors using it  
* **Technology Modernization Card**:  
  * Suggested tech stack improvements  
  * Current vs Recommended (side-by-side)  
  * Benefits list  
  * Learning resources links  
* **Pricing Strategy Card**:  
  * Optimal price suggestion (large)  
  * Reasoning explanation  
  * Price tier suggestions:  
    * Basic  
    * Standard  
    * Premium  
  * Revenue projection table

**Column 2: Strategy**

* **Unique Selling Propositions Card**:  
  * 3-5 USP suggestions  
  * Each USP:  
    * Headline  
    * Explanation (2-3 sentences)  
    * Target audience  
    * Differentiation score  
* **Development Effort Card**:  
  * Complexity indicator:  
    * Visual: Low/Medium/High badge  
    * Color-coded  
  * Timeline estimate:  
    * MVP: X weeks  
    * Full Version: Y months  
  * Resource requirements  
  * Key challenges list  
* **Market Positioning Card**:  
  * Target niche description  
  * Competitive advantages  
  * Go-to-market strategy bullets  
  * Marketing angles

**Export Button** (Bottom):

* "Export Full AI Report" (PDF)  
* Icon: Download  
* Secondary styling

**Tab 4: Similar Products**

**Comparison Table**

* **Layout**: Horizontal scroll table  
* **Columns**:  
  * Feature/Metric name (fixed left)  
  * This Product (highlighted column)  
  * Competitor 1  
  * Competitor 2  
  * Competitor 3  
  * Competitor 4  
* **Rows**:  
  * Thumbnail image  
  * Price  
  * Total Sales  
  * Rating  
  * Profitability Score  
  * Launch Date  
  * Last Update  
  * Key Features (expandable)  
  * Technologies  
* **Styling**:  
  * Header row: Sticky  
  * Current product column: Light blue background  
  * Alternating row colors  
  * Better/worse indicators (arrows, colors)  
  * Click column header to visit product

**Product Cards View** (Alternative toggle)

* Grid of similar product cards  
* Same card design as search results  
* "Add to Comparison" quick action

**Tab 5: Reviews**

**Reviews Summary** (Top)

* **Overall Rating**:  
  * Large number (4.8/5)  
  * Star visualization  
  * Total reviews count  
* **Rating Distribution**:  
  * Horizontal bar chart  
  * 5 bars (5-star to 1-star)  
  * Each bar:  
    * Star count label  
    * Progress bar (fill \= percentage)  
    * Count/percentage  
  * Click bar to filter reviews  
* **Sentiment Breakdown**:  
  * Positive / Neutral / Negative percentages  
  * Pie chart or segments

**Review Filters**

* Sort dropdown: Most Recent, Most Helpful, Highest/Lowest Rating  
* Filter by rating (star buttons)  
* Search within reviews

**Review List**

**Each Review Card**:

* **Header**:  
  * Reviewer avatar (40px)  
  * Reviewer name  
  * "Verified Purchase" badge (if applicable)  
  * Star rating (filled stars)  
  * Date posted (gray, right)  
* **Content**:  
  * Review title (if available, bold)  
  * Review text (expandable if long)  
  * "Read more" link if truncated  
* **Footer**:  
  * Helpful? Yes (count) / No (count) buttons  
  * Report link (subtle)  
* **Styling**:  
  * White background card  
  * Border: 1px light gray  
  * Padding: 20px  
  * Margin bottom: 16px  
  * Hover: Subtle shadow increase

**Pagination**: Bottom of reviews

**Tab 6: Changelog**

**Timeline Layout**

**Each Version Entry**:

* **Timeline Dot**: Left side, colored circle  
* **Version Card**:  
  * **Header**:  
    * Version number (large, bold): "v2.5.0"  
    * Release date (gray)  
    * Badge: "Latest" (green) if current  
  * **Content**:  
    * Changes organized by type:  
      * 🎉 New Features (green)  
      * 🔧 Improvements (blue)  
      * 🐛 Bug Fixes (red)  
      * 📚 Documentation (gray)  
    * Each change: Bullet point list  
  * **Footer**:  
    * Download this version link (if available)

**Styling**:

* Vertical timeline line (left)  
* Cards: White, shadow SM  
* Spacing: 24px between versions  
* Collapse older versions (show first 5\)  
* "Show More" button

---

## **🎯 URL Scraper Interface**

### **Page Layout**

**Hero Section**

* **Title**: "Scrape CodeCanyon Product" (36px, bold)  
* **Subtitle**: "Enter any CodeCanyon product URL to analyze" (18px, gray)

**Main Scraper Card** (Centered, 800px max width)

**Card Design**:

* Large white card  
* Shadow: XL  
* Padding: 48px  
* Border radius: 16px

**Input Section**:

* **URL Input Field**:  
  * Large input (56px height)  
  * Placeholder: "[https://codecanyon.net/item/](https://codecanyon.net/item/)..."  
  * Left icon: Link chain  
  * Right button: Paste from clipboard  
  * Border: 2px, blue on focus  
  * Border radius: 12px  
  * Error state: Red border \+ shake animation  
* **Validation**:  
  * Real-time URL format check  
  * Error message below (red): "Invalid CodeCanyon URL"  
  * Success indicator (green checkmark) when valid  
* **Recent URLs** (Below input):  
  * "Recently scraped:" label (14px, gray)  
  * Horizontal scrollable chip row  
  * Each chip: Product name (truncated)  
  * Click to use that URL  
  * Max 5 shown

**Action Buttons**:

* **Scrape Button** (Large, prominent):  
  * Full width  
  * Height: 56px  
  * Blue gradient background  
  * White text (18px, semibold)  
  * Icon: Magnifying glass or download  
  * Disabled state if invalid URL  
  * Loading state: Spinner \+ "Scraping..."  
  * Success state: Checkmark \+ "Complete\!"  
* **Advanced Options** (Collapsible):  
  * Toggle link: "Advanced options"  
  * Checkbox: "Force re-scrape (ignore cache)"  
  * Checkbox: "Include review data"  
  * Checkbox: "Generate AI insights immediately"

**Progress Indicator** (Appears during scraping)

**Multi-Step Progress**:

* **Visual**: Horizontal step indicator  
* **Steps**:  
  * Validating URL  
  * Fetching page  
  * Extracting data  
  * Analyzing metrics  
  * Complete  
* **Each Step**:  
  * Circle indicator  
  * Line connecting to next  
  * Checkmark when complete (green)  
  * Spinner when active (blue, animated)  
  * Gray when pending  
  * Step label below  
* **Progress Bar**:  
  * Below step indicators  
  * Smooth animated fill (left to right)  
  * Blue gradient  
  * Height: 4px

**Real-time Status Messages**:

* Below progress bar  
* Updates as scraping progresses:  
  * "Connecting to CodeCanyon..."  
  * "Fetching product data..."  
  * "Extracting features..."  
  * "Calculating profitability..."  
  * "Almost done..."

**Result Display** (After completion)

**Success State**:

* **Product Preview Card** (Slides in from bottom):  
  * Thumbnail (left)  
  * Product name (large)  
  * Category badge  
  * Profitability score (right, prominent)  
* **Action Buttons**:  
  * "View Full Analysis" (primary, blue)  
  * "Add to Dashboard" (secondary)  
  * "Scrape Another" (outline)

**Error State**:

* **Error Card**:  
  * Red error icon (large)  
  * Error message headline: "Scraping Failed"  
  * Specific error description  
  * Possible causes (bulleted list)  
  * Suggested actions:  
    * "Try again"  
    * "Check URL format"  
    * "Contact support"  
  * Retry button

**Previously Scraped Products Section**

**Below main card**:

* **Title**: "Your Scraped Products" (24px, semibold)  
* **Grid**: 3 columns, product cards  
* **Each Card** (Mini version):  
  * Thumbnail  
  * Product name  
  * Date scraped (gray, small)  
  * Profitability score badge  
  * "View" link  
* **Pagination**: If \> 9 products

**Help Section** (Right sidebar or below)

* **Icon**: Question mark circle  
* **Content**:  
  * "How to find CodeCanyon URLs"  
  * Example URL format shown  
  * Tips for best results  
  * FAQ accordion

---

## **🚀 Project Planner Interface**

### **Wizard-Style Multi-Step Form**

**Overall Layout**:

* Full-width container  
* Left sidebar: Progress tracker (sticky)  
* Right content area: Current step form

**Progress Sidebar** (Left, 300px)

**Sidebar Content**:

* **Project Overview** (Top card):  
  * Project name (editable inline)  
  * Inspired by product (link)  
  * Progress circle: X/6 steps complete  
* **Steps List**:  
  * Concept Validation ✓ (green checkmark if complete)  
  * Feature Specification (current: blue dot)  
  * Technology Stack (pending: gray)  
  * Development Roadmap  
  * CodeCanyon Compliance  
  * Marketing Strategy  
* **Each Step Item**:  
  * Number badge (circular)  
  * Step name  
  * Status indicator  
  * Click to navigate (if already visited)  
  * Active step: Highlighted background  
* **Save Progress** (Bottom):  
  * Auto-save indicator: "Saved 2 minutes ago"  
  * Manual save button  
  * Exit wizard link

**Step Content Area** (Right)

**Step Header** (Each step):

* Step number: "Step 1 of 6"  
* Step title (32px, bold)  
* Step description (16px, gray)  
* Progress bar (thin, top of content)

**Step 1: Concept Validation**

**Form Fields**:

* **Project Name**:  
  * Large input (48px height)  
  * Placeholder: "e.g., AI-Powered Form Builder"  
  * Character counter (50 max)  
  * Real-time URL slug preview below  
* **Inspiration Product** (if coming from product page):  
  * Product card (read-only)  
  * Remove button  
  * Or "Browse products" button if none selected  
* **Target Category**:  
  * Dropdown with search  
  * Categories from database  
  * Icon for each category  
  * Popular categories at top  
* **Project Description**:  
  * Textarea (large, auto-expanding)  
  * Placeholder: "Describe your product idea..."  
  * Rich text editor (basic formatting)  
  * Character counter (500 max)  
* **Market Opportunity** (AI-generated suggestion):  
  * Read-only section  
  * Shows AI analysis of market potential  
  * Score indicator  
  * Expandable details

**Navigation**:

* "Next: Feature Specification" button (bottom-right)  
* Large, primary blue  
* Arrow icon

**Step 2: Feature Specification**

**Layout**: 2-column

**Left Column: AI Suggestions**

* **Title**: "Suggested Features" (20px)  
* **Subtitle**: "Based on market analysis" (14px, gray)  
* **Feature Cards** (Vertical list):  
  * **Each Card**:  
    * Feature name (16px, semibold)  
    * Description (14px, 2 lines)  
    * Impact badge: High/Medium/Low  
    * Add button (+) \- adds to right column  
    * Already added: Checkmark \+ "Added"  
* **Categories** (Filter tabs):  
  * All  
  * Must-Have  
  * Nice-to-Have  
  * Competitive Edge

**Right Column: Your Features**

* **Title**: "Selected Features" (20px)  
* **Count**: "X features selected" (gray)  
* **Feature List** (Sortable, drag-and-drop):  
  * **Each Item**:  
    * Drag handle (6 dots icon, left)  
    * Feature name (editable inline)  
    * Priority dropdown: Must-Have / Should-Have / Could-Have  
    * Complexity estimate: Low/Medium/High (colored badge)  
    * Delete button (trash icon)  
* **Add Custom Feature**:  
  * Input row (always at bottom)  
  * Plus icon button  
  * Placeholder: "Add custom feature..."

**Navigation**:

* "Back" button (left, secondary)  
* "Next: Technology Stack" (right, primary)  
* "Save & Exit" (link, top-right)

**Step 3: Technology Stack Selection**

**Recommended Stack Card** (Top)

* **AI Badge**: "AI Recommended"  
* **Icon**: Tech stack icon  
* **Stack Display**:  
  * Frontend: React / Vue / Angular  
  * Backend: Node.js / Laravel / Django  
  * Database: PostgreSQL / MySQL / MongoDB  
  * Additional: Redis, etc.  
* **Reasoning**: Bulleted explanation  
* **Use This Stack** button

**Custom Stack Builder** (Below)

**Categories** (Tabs):

* Frontend  
* Backend  
* Database  
* Infrastructure  
* Other

**Each Category Panel**:

* **Popular Options** (Grid of cards):  
  * Each technology card:  
    * Logo icon (large, 64px)  
    * Tech name  
    * Brief description  
    * Popularity indicator (stars or %)  
    * Select checkbox  
    * "Learn More" link (external)  
* **Search Technologies**:  
  * Input with autocomplete  
  * Can add custom tech not in list

**Selected Stack Summary** (Right sidebar):

* **Title**: "Your Stack"  
* **List by Category**:  
  * Each selected tech:  
    * Icon \+ name  
    * Remove button (X)  
* **Compatibility Check**:  
  * Auto-validates compatibility  
  * Shows warnings if issues  
  * Green checkmark if compatible  
* **Learning Resources**:  
  * Auto-generates links to:  
    * Documentation  
    * Tutorials  
    * Starter templates

**Navigation**:

* Standard Back / Next buttons

**Step 4: Development Roadmap**

**MVP Scope Definition**

**Section 1: Core Features** (Top)

* **Instructions**: "Select features for MVP"  
* **Feature List** (from Step 2):  
  * Each feature: Checkbox  
  * Pre-selected: High priority features  
  * Visual indicator: MVP badge on selected

**Section 2: Timeline Builder**

**Visual Timeline Creator**:

* **Drag-and-drop Gantt chart style**:  
  * Rows: Milestones/features  
  * Columns: Weeks/months  
  * Draggable blocks to schedule  
* **Milestones** (Default suggestions):  
  * Project Setup  
  * Core Features Development  
  * Testing & QA  
  * Documentation  
  * CodeCanyon Submission  
  * Launch  
* **Each Milestone Card**:  
  * Milestone name (editable)  
  * Duration input (weeks)  
  * Features included (list)  
  * Dependencies (if any)

**Auto-calculated Totals**:

* Total estimated time (large display)  
* Full-time vs part-time toggle  
* Resource requirements (1-2-3+ developers)

**Section 3: Risk Assessment**

* **AI-generated risks**:  
  * Technical challenges  
  * Time constraints  
  * Resource needs  
* **Each Risk**:  
  * Risk description  
  * Severity: Low/Medium/High  
  * Mitigation suggestion

**Navigation**: Back / Next

**Step 5: CodeCanyon Compliance**

**Checklist Generator**

**Section 1: File Structure**

* **Auto-generated folder tree**:  
  * Based on selected stack  
  * Expandable/collapsible tree view  
  * Each item: Checkbox when ready  
  * CodeCanyon requirements highlighted

**Section 2: Documentation Requirements**

* **Checklist**:  
  * README.md  
  * Installation guide  
  * Configuration instructions  
  * API documentation (if applicable)  
  * Changelog  
  * License information  
* **Templates Available**:  
  * "Download Template" buttons for each  
  * Auto-fills with project info

**Section 3: Code Quality**

* **Best Practices Checklist**:  
  * Commented code  
  * Consistent naming  
  * Error handling  
  * Security measures  
  * Performance optimization

**Section 4: Testing Requirements**

* **Checklist**:  
  * Unit tests  
  * Integration tests  
  * Browser compatibility  
  * Mobile responsiveness  
  * Load testing

**Section 5: Submission Checklist**

* **Final Steps**:  
  * Preview images (6 required)  
  * Demo site/video  
  * Item description (SEO)  
  * Tags and keywords  
  * Pricing decision  
  * Support plan

**Progress Indicator**:

* X/Y items complete  
* Progress bar  
* "You're ready\!" message when all checked

**Navigation**: Back / Next

**Step 6: Marketing Strategy**

**Section 1: Pricing Calculator**

**Input Fields**:

* Development hours estimate  
* Hourly rate  
* Competitor prices (auto-filled from analysis)

**Output Display**:

* **Recommended Price** (Large, centered):  
  * Price amount ($X)  
  * Reasoning bullets  
* **Price Tiers Table**:  
  * Regular License: $X  
  * Extended License: $Y  
  * Expected monthly revenue (estimate)

**Section 2: Competitive Analysis**

**Comparison Table**:

* Your Product vs Top 3 Competitors  
* Columns: Price, Features, Score  
* Visual indicators: Better/worse/same

**Section 3: Unique Selling Propositions**

**USP Cards** (AI-generated):

* **Each USP**:  
  * Headline (large, bold)  
  * Explanation (2-3 sentences)  
  * Target audience  
  * Edit button (customize)

**Section 4: Launch Checklist**

**Pre-Launch**:

* Demo site live  
* Documentation complete  
* Preview images ready  
* Video demo created  
* Item description written

**Launch Week**:

* Submit to CodeCanyon  
* Social media posts scheduled  
* Email newsletter  
* Forum announcements

**Post-Launch**:

* Monitor reviews  
* Support setup  
* Update schedule  
* Marketing analytics

**Section 5: Marketing Channels**

**Suggested Channels** (Checkboxes):

* CodeCanyon search optimization  
* Social media (list platforms)  
* Blog/content marketing  
* YouTube tutorials  
* Email marketing  
* Paid advertising

**Final Actions**:

* **Export Full Plan** (PDF button):  
  * Comprehensive PDF with all wizard data  
  * Professional formatting  
  * Charts and visuals included  
* **Save to Dashboard** (Primary button):  
  * Creates project in dashboard  
  * Navigate to project page  
* **Start Development** (Call-to-action):  
  * Links to resources  
  * Integration with project management tools

---

## **📊 Dashboard Analytics Page**

### **Page Structure**

**Time Range Selector** (Top-right)

* Dropdown: Last 7 Days / 30 Days / 90 Days / Year / All Time  
* Custom date range picker

**Key Metrics Row** (4 Cards)

**Each Metric Card**:

* **Layout**: Horizontal split  
* **Left**:  
  * Icon (large, 48px, colored background circle)  
  * Metric name (14px, gray)  
* **Right**:  
  * Large number (36px, bold)  
  * Trend indicator: Arrow \+ percentage  
  * Colored by direction (green up, red down)

**Metrics**:

1. Total Products Analyzed  
2. Total Revenue Potential (sum)  
3. Average Profitability Score  
4. Active Projects

**Charts Section** (Grid layout)

**Chart 1: Analysis Activity Timeline**

* **Type**: Area chart  
* **Data**: Products analyzed over time  
* **X-axis**: Dates  
* **Y-axis**: Count  
* **Fill**: Blue gradient  
* **Interactive**: Hover shows exact date and count  
* **Height**: 300px

**Chart 2: Category Distribution**

* **Type**: Donut chart  
* **Data**: Analyzed products by category  
* **Colors**:

Continue

5:57 PM

Distinct colors per category

* **Center**: Total count  
* **Legend**: Right side  
* **Interactive**: Click segment to filter  
* **Height**: 300px

**Chart 3: Profitability Score Distribution**

* **Type**: Histogram  
* **Data**: Number of products in each score range  
* **Ranges**: 0-20, 20-40, 40-60, 60-80, 80-100  
* **Colors**: Red to green gradient  
* **Height**: 300px

**Chart 4: Revenue Potential Trend**

* **Type**: Line chart with area fill  
* **Data**: Total revenue potential over time  
* **Y-axis**: Dollar amounts  
* **Cumulative**: Shows growth  
* **Color**: Success green  
* **Height**: 300px

**Insights Panel** (Below charts)

**AI-Generated Insights**:

* **Card Layout**: Grid, 3 columns  
* **Each Insight**:  
  * Icon (lightbulb, chart, star)  
  * Insight title (bold)  
  * Description (2-3 lines)  
  * Action button  
  * Colored border (left, insight type)

**Example Insights**:

* "WordPress is your most profitable category"  
* "Products with React tend to score higher"  
* "Your analysis activity increased 25% this month"

**Export Section** (Bottom)

* **Title**: "Export Data"  
* **Options**:  
  * Export all analyzed products (CSV)  
  * Export profitability reports (PDF)  
  * Export project plans (ZIP)  
* **Buttons**: Download icons

---

## **🔬 AI Recommendations Generator Page**

### **Page Layout**

**Header Section**

* **Title**: "AI-Powered Insights Generator" (36px)  
* **Subtitle**: "Get intelligent recommendations for any product"  
* **Sparkle icon animation** (subtle pulse)

**Input Section** (Centered card)

**Product Selection**:

* **Option 1**: Select from analyzed products  
  * Dropdown with search  
  * Shows product thumbnails  
* **Option 2**: Enter new URL  
  * URL input field  
  * Auto-scrape on submit  
* **Advanced Options** (Collapsible):  
  * Focus areas (checkboxes):  
    * Feature gaps  
    * Technology modernization  
    * Pricing strategy  
    * Market positioning  
  * Competitor depth: Shallow / Deep

**Generate Button**:

* Large (full-width)  
* Purple gradient (AI branding)  
* Icon: Sparkles  
* "Generate AI Insights" text

**Generation Process** (Animated)

**AI Thinking Animation**:

* **Visual**: Animated brain icon or pulsing dots  
* **Progress Steps**:  
  * Analyzing product...  
  * Researching competitors...  
  * Evaluating market...  
  * Generating recommendations...  
  * Finalizing insights...  
* **Progress Bar**: Smooth animated fill

**Streaming Results** (Real-time display)

**Results Appear Progressively**:

* Each section fades in as AI generates it  
* Typewriter effect for text (subtle)  
* Smooth scroll to new content

**Results Layout** (Comprehensive from earlier, enhanced)

**Section Navigation** (Sticky sidebar)

* Quick jump links to each section  
* Progress indicators (completed sections)

**Export Options** (Top-right):

* PDF Export (formatted report)  
* Copy to clipboard  
* Share link  
* Save to project

**Feedback Section** (Bottom)

* "Was this helpful?" (thumbs up/down)  
* "Request regeneration" button  
* "Refine recommendations" (opens options)

---

## **🎨 Component Library \- Reusable Elements**

### **Buttons**

**Primary Button**:

* Background: Primary blue (`#2563EB`)  
* Text: White, 16px, semibold  
* Padding: 12px 24px  
* Border radius: 8px  
* Shadow: MD  
* Hover: Darker blue, shadow LG, translateY(-1px)  
* Active: Even darker, shadow SM  
* Disabled: Gray, opacity 50%, cursor not-allowed  
* Icon support: Left or right, 20px

**Secondary Button**:

* Background: Transparent  
* Border: 2px primary blue  
* Text: Primary blue  
* Same sizing as primary  
* Hover: Blue background (10% opacity)

**Tertiary/Ghost Button**:

* Background: Transparent  
* No border  
* Text: Primary blue  
* Hover: Blue background (5% opacity)

**Danger Button**:

* Background: Danger red  
* Same structure as primary  
* Use for delete, destructive actions

**Button Sizes**:

* Small: 32px height, 12px 16px padding  
* Medium: 40px height, 12px 24px padding (default)  
* Large: 48px height, 16px 32px padding  
* XL: 56px height, 20px 40px padding

### **Form Inputs**

**Text Input**:

* Height: 44px  
* Padding: 12px 16px  
* Border: 1px light gray  
* Border radius: 8px  
* Font: 16px  
* Focus: Blue border (2px), box shadow (blue glow)  
* Error: Red border, shake animation  
* Success: Green border, checkmark icon (right)  
* Disabled: Gray background, cursor not-allowed

**Input with Icon**:

* Icon position: Left or right, 20px size  
* Padding adjusted for icon (add 36px)  
* Icon color: Gray, blue on focus

**Textarea**:

* Same styling as input  
* Min height: 120px  
* Resize: Vertical only  
* Auto-expand option

**Select Dropdown**:

* Same base styling as input  
* Chevron icon (right)  
* Dropdown panel:  
  * White background  
  * Shadow: LG  
  * Max height: 300px (scrollable)  
  * Options: Hover blue background (5%)  
  * Selected: Blue background, checkmark icon

**Checkbox**:

* Size: 20px × 20px  
* Border: 2px gray  
* Border radius: 4px  
* Checked: Blue background, white checkmark  
* Label: 14px, clickable  
* Focus: Blue outline (keyboard navigation)

**Radio Button**:

* Size: 20px diameter  
* Border: 2px gray  
* Checked: Blue background, white dot (8px)  
* Label: 14px, clickable

**Toggle Switch**:

* Width: 44px  
* Height: 24px  
* Pill shape  
* Off: Gray background  
* On: Blue background  
* Knob: White circle, 20px, animated slide  
* Transition: 200ms

### **Cards**

**Standard Card**:

* Background: White  
* Border radius: 12px  
* Shadow: MD  
* Padding: 24px  
* Hover: Shadow LG, translateY(-2px)  
* Transition: 300ms

**Card Header**:

* Border bottom: 1px light gray  
* Padding bottom: 16px  
* Margin bottom: 20px  
* Title: 20px, semibold  
* Action button/link: Right-aligned

**Card Footer**:

* Border top: 1px light gray  
* Padding top: 16px  
* Margin top: 20px  
* Typically contains actions

**Gradient Card**:

* Background: Gradient (blue to purple)  
* Text: White  
* Used for CTAs, premium features

**Stat Card** (Special):

* Icon: Large, subtle, positioned top-right  
* Number: 48px, bold  
* Label: 14px, gray  
* Trend: Small chart or percentage

### **Badges**

**Status Badge**:

* Padding: 4px 12px  
* Border radius: Full (pill)  
* Font: 12px, semibold  
* Uppercase

**Colors/Variants**:

* Success: Green background, dark green text  
* Warning: Amber background, dark amber text  
* Danger: Red background, dark red text  
* Info: Blue background, dark blue text  
* Neutral: Gray background, dark gray text

**Notification Badge**:

* Circular: 20px diameter  
* Background: Red  
* Text: White, 12px  
* Position: Absolute (top-right of icon)  
* Shadow: SM

### **Modals**

**Modal Overlay**:

* Background: Black, 50% opacity  
* Backdrop blur: 4px  
* Z-index: 2000  
* Click to close (outside modal)

**Modal Container**:

* Background: White  
* Border radius: 16px  
* Shadow: 2XL  
* Max width: 600px (default)  
* Margin: Auto, centered vertically and horizontally  
* Padding: 32px  
* Animation: Scale in from 0.9, fade in, 300ms

**Modal Header**:

* Close button: Top-right, X icon  
* Title: 24px, bold  
* Optional icon/illustration

**Modal Body**:

* Content area  
* Max height: 60vh (scrollable if exceeds)  
* Custom scrollbar

**Modal Footer**:

* Border top: 1px light gray  
* Padding top: 24px  
* Action buttons: Right-aligned  
* Cancel button: Secondary, left  
* Confirm button: Primary, right

**Modal Sizes**:

* Small: 400px  
* Medium: 600px (default)  
* Large: 800px  
* Full: 90vw

### **Tooltips**

**Tooltip Container**:

* Background: Dark gray (`#1F2937`)  
* Text: White, 14px  
* Padding: 8px 12px  
* Border radius: 6px  
* Shadow: MD  
* Max width: 200px  
* Arrow pointing to target (8px)

**Trigger**: Hover or focus **Position**: Auto (smart positioning) **Animation**: Fade in \+ slide, 200ms

### **Dropdowns**

**Dropdown Toggle**:

* Button with chevron icon  
* Same as button styling

**Dropdown Menu**:

* Background: White  
* Shadow: LG  
* Border radius: 8px  
* Padding: 8px 0  
* Min width: 200px  
* Position: Absolute (below toggle)  
* Z-index: 1000

**Dropdown Item**:

* Padding: 10px 16px  
* Text: 14px  
* Hover: Blue background (5%)  
* Icon support (left, 20px)  
* Divider: 1px gray line between groups

**Dropdown Animation**: Fade \+ scale from top, 200ms

### **Loading Indicators**

**Spinner** (Primary):

* Circular, rotating animation  
* Border: 3px, blue gradient  
* Sizes: 16px, 24px, 32px, 48px  
* Smooth 360deg rotation, infinite

**Skeleton Loader**:

* Background: Light gray  
* Animated shimmer effect (light sweep)  
* Shape matches content (rectangles for text, circles for avatars)  
* Pulse animation

**Progress Bar**:

* Track: Light gray, 4px height  
* Fill: Blue gradient  
* Border radius: Full  
* Animated fill (smooth transition)  
* Optional percentage label

**Dots Loader**:

* 3 dots, animated bounce  
* Staggered animation (sequential bounce)  
* Use for text-based loading ("Loading...")

### **Alerts/Notifications**

**Alert Box**:

* Border left: 4px colored (semantic color)  
* Background: Semantic color, 10% opacity  
* Padding: 16px  
* Border radius: 8px  
* Icon: Left-aligned, 24px  
* Close button: Right-aligned (optional)

**Toast Notification**:

* Position: Fixed, top-right (or bottom-right)  
* Background: White  
* Shadow: XL  
* Padding: 16px 20px  
* Border radius: 12px  
* Icon: Left, colored  
* Message: 14px  
* Close button: Right  
* Auto-dismiss: 5 seconds (with progress bar)  
* Slide-in animation from right  
* Stack multiple toasts (8px gap)

### **Tables**

**Table Container**:

* Border: 1px light gray  
* Border radius: 12px  
* Overflow: Auto (horizontal scroll on mobile)

**Table Header**:

* Background: Light gray (`#F9FAFB`)  
* Text: 14px, semibold, uppercase  
* Padding: 12px 16px  
* Border bottom: 2px gray  
* Sortable headers: Cursor pointer, sort icons

**Table Row**:

* Border bottom: 1px light gray  
* Padding: 16px  
* Hover: Blue background (3%)  
* Clickable rows: Cursor pointer

**Table Cell**:

* Text: 14px  
* Padding: 16px  
* Vertical align: Middle  
* Truncate long text (ellipsis)

**Table Footer** (Pagination):

* Border top: 1px gray  
* Padding: 16px  
* Centered or right-aligned controls

### **Tabs**

**Tab Container**:

* Border bottom: 1px light gray

**Tab Button**:

* Padding: 12px 20px  
* Text: 16px, semibold  
* Border: None  
* Background: Transparent  
* Inactive: Gray text  
* Active: Primary blue text, bottom border (3px)  
* Hover: Blue background (5%)  
* Transition: 200ms  
* Indicator: Animated underline (slides to active tab)

**Tab Panel**:

* Padding: 24px 0  
* Fade in animation when switching (300ms)

### **Accordions**

**Accordion Item**:

* Border: 1px light gray  
* Border radius: 8px  
* Margin bottom: 8px

**Accordion Header**:

* Padding: 16px 20px  
* Background: White  
* Cursor: Pointer  
* Hover: Blue background (3%)  
* Title: 16px, semibold  
* Icon: Chevron (right), rotates when open  
* Transition: 200ms

**Accordion Body**:

* Padding: 0 20px 16px  
* Animation: Slide down, 300ms  
* Hidden when collapsed

### **Pagination**

**Pagination Container**:

* Display: Flex, centered  
* Gap: 8px  
* Padding: 24px 0

**Page Button**:

* Width: 40px  
* Height: 40px  
* Border radius: 8px  
* Text: 14px, semibold  
* Border: 1px light gray  
* Background: White  
* Hover: Blue background (10%)  
* Active page: Blue background, white text  
* Disabled: Gray, opacity 50%

**Previous/Next Buttons**:

* Same size  
* Icon: Arrow  
* Can include text on desktop

**Ellipsis**:

* Display: ... (when pages skipped)  
* Same size, not clickable

---

## **🎭 Animations & Micro-interactions**

### **Page Transitions**

**Page Load**:

* Stagger animation for main content  
* Each section fades in \+ slides up  
* Delay: 100ms between sections  
* Total duration: 800ms

**Navigation**:

* Fade out current content (200ms)  
* Fade in new content (300ms)  
* Optional: Slide left/right for sequential pages

### **Interactive Elements**

**Button Click**:

* Scale down to 0.95 on active  
* Ripple effect from click point  
* Bounce back on release  
* Duration: 150ms

**Card Hover**:

* Lift: translateY(-4px)  
* Shadow increase: MD → LG  
* Smooth transition: 300ms

**Input Focus**:

* Border color change: Gray → Blue  
* Border width: 1px → 2px  
* Blue glow (box-shadow)  
* Duration: 200ms

**Checkbox Check**:

* Scale animation: 0 → 1.2 → 1  
* Checkmark draws in (stroke animation)  
* Duration: 300ms

**Toggle Switch**:

* Background color transition: 300ms  
* Knob slide: 200ms  
* Spring effect on knob (slight overshoot)

### **Data Visualizations**

**Chart Entrance**:

* Bars/lines draw from 0 to value  
* Stagger animation for multiple elements  
* Easing: Deceleration curve  
* Duration: 800ms

**Number Count-Up**:

* Large numbers animate from 0  
* Smooth counting animation  
* Duration based on magnitude  
* Easing: Ease-out

### **Loading States**

**Skeleton Shimmer**:

* Gradient sweep from left to right  
* Animation: Continuous, 1.5s duration  
* Light gray to lighter gray

**Spinner Rotation**:

* Smooth 360deg rotation  
* Infinite animation  
* 1s duration, linear

**Progress Bar Fill**:

* Smooth width increase  
* Gradient animation  
* Transition: 500ms

### **Success/Error States**

**Success Checkmark**:

* Scale in: 0 → 1.2 → 1  
* Draw checkmark (stroke animation)  
* Green color  
* Optional: Confetti burst  
* Duration: 500ms

**Error Shake**:

* Horizontal shake (translateX)  
* 3-4 shakes  
* Red flash  
* Duration: 400ms

### **Scroll Animations**

**Scroll Reveal**:

* Elements fade in \+ slide up as they enter viewport  
* Stagger for lists  
* Trigger: 10% in viewport  
* Once only (no repeat)

**Parallax** (Subtle):

* Background elements move slower than foreground  
* Depth effect  
* Use sparingly

### **Drag and Drop**

**Drag Start**:

* Element lifts (shadow increase)  
* Slightly transparent  
* Cursor changes

**Drag Over**:

* Drop zone highlights  
* Dashed border animation  
* Blue background (10% opacity)

**Drop**:

* Element snaps to position  
* Brief scale pulse  
* Confirmation animation

---

## **📱 Responsive Design Guidelines**

### **Breakpoint Strategy**

**Mobile First Approach**:

* Design for mobile (320px+)  
* Enhance for larger screens

**Breakpoints**:

* XS: \< 640px (Mobile)  
* SM: 640px (Large mobile / Small tablet)  
* MD: 768px (Tablet)  
* LG: 1024px (Desktop)  
* XL: 1280px (Large desktop)  
* 2XL: 1536px (Extra large)

### **Mobile Adaptations (\< 640px)**

**Navigation**:

* Hamburger menu (sidebar overlay)  
* Bottom tab bar for main sections  
* Collapse all sub-menus

**Dashboard**:

* Single column layout  
* Metric cards: Stack vertically  
* Charts: Full width, reduced height  
* Hide non-essential elements

**Product Cards**:

* Full width (1 column grid)  
* Larger touch targets (44px min)  
* Simplified information

**Forms**:

* Full width inputs  
* Stack all fields vertically  
* Larger buttons (56px height)  
* Native select dropdowns (better UX on mobile)

**Tables**:

* Horizontal scroll  
* Or convert to card layout  
* Important columns first

**Modals**:

* Full screen on mobile  
* Slide up from bottom  
* Close button: Top-left or bottom

### **Tablet Adaptations (640px \- 1024px)**

**Navigation**:

* Collapsible sidebar (icon only or hidden)  
* More horizontal space utilized

**Dashboard**:

* 2-column layout  
* Charts: 2 per row

**Product Grid**:

* 2 columns

**Forms**:

* 2-column layouts for related fields

### **Touch Targets**

**Minimum Size**: 44px × 44px **Spacing**: 8px between touch targets **Visual Feedback**: Immediate on tap (not just hover)

### **Performance Optimization**

**Images**:

* Lazy loading (below fold)  
* Responsive images (srcset)  
* WebP format with fallbacks  
* Placeholders: Blurred preview or solid color

**Fonts**:

* Font display: Swap (avoid invisible text)  
* Preload critical fonts  
* Subset fonts (remove unused characters)

**Critical CSS**:

* Inline above-the-fold CSS  
* Defer non-critical CSS

**JavaScript**:

* Defer non-critical JS  
* Code splitting (load on demand)  
* Minimize main thread work

---

## **♿ Accessibility (A11y) Requirements**

### **Keyboard Navigation**

**Requirements**:

* All interactive elements keyboard-accessible  
* Visible focus indicators (2px blue outline)  
* Logical tab order  
* Skip navigation links  
* Keyboard shortcuts documented

**Focus Management**:

* Focus trapped in modals  
* Focus returns after modal close  
* Focus moves to new content after HTMX swap

### **Screen Reader Support**

**ARIA Labels**:

* All icons have aria-labels  
* Form inputs have labels (visible or aria-label)  
* Dynamic content: aria-live regions  
* Loading states announced

**Semantic HTML**:

* Proper heading hierarchy (H1 → H2 → H3)  
* Semantic elements (nav, main, section, article)  
* Lists for lists (ul, ol)  
* Buttons for actions, links for navigation

**Alt Text**:

* All images have descriptive alt text  
* Decorative images: alt=""  
* Complex images: Long descriptions

### **Color Contrast**

**WCAG AA Compliance**:

* Normal text: 4.5:1 contrast ratio  
* Large text (18px+): 3:1 contrast ratio  
* UI components: 3:1 contrast ratio

**Color Independence**:

* Information not conveyed by color alone  
* Use icons, text labels, patterns in addition to color

### **Form Accessibility**

**Labels**:

* Every input has a label  
* Label associated with input (for attribute)

**Error Messages**:

* Inline error messages  
* Announced to screen readers (aria-live)  
* Errors listed at form top (also)

**Required Fields**:

* Marked visually (asterisk)  
* Marked semantically (required attribute, aria-required)

### **Motion & Animation**

**Respect Preferences**:

* Detect prefers-reduced-motion  
* Reduce/remove animations if set  
* Essential animations only

---

## **🎨 Dark Mode Design (Optional Future Enhancement)**

**Color Palette (Dark)**:

* Background: `#0F172A` (very dark blue)  
* Surface: `#1E293B` (dark blue)  
* Text Primary: `#F1F5F9` (very light gray)  
* Text Secondary: `#94A3B8` (light gray)  
* Borders: `#334155` (medium gray)

**Toggle**:

* User preference setting  
* Persists in local storage  
* Smooth transition (300ms) when switching

**Adjustments**:

* Reduce white colors (use off-white)  
* Lower contrast for comfort  
* Adjust shadows (lighter, more subtle)

---

## **📐 Design Handoff Specifications**

### **For Developers**

**Design Files**:

* Figma/Sketch files with all screens  
* Component library (reusable)  
* Style guide (this document)  
* Asset exports (icons, logos, images)

**Specifications**:

* Exact spacing values (use 4px grid)  
* Color hex codes  
* Font sizes and weights  
* Border radius values  
* Shadow specifications  
* Animation timing and easing

**States**:

* Default, hover, active, disabled for all interactive elements  
* Loading, error, success states  
* Empty states  
* Mobile/tablet/desktop variants

### **For Content**

**Placeholder Content**:

* All text is placeholder (Lorem ipsum acceptable)  
* Use realistic data lengths  
* Consider edge cases (very long titles, zero results)

**Tone**:

* Professional but friendly  
* Clear and concise  
* Action-oriented CTAs  
* Helpful error messages

---

## **🎯 Implementation Priority**

**Phase 1: Core Pages** (Week 1-2)

1. Navigation structure  
2. Dashboard homepage  
3. Product search interface  
4. Product detail page  
5. Basic components

**Phase 2: Advanced Features** (Week 3-4) 6\. URL scraper interface 7\. Analysis visualizations 8\. AI recommendations UI 9\. Advanced components

**Phase 3: Project Features** (Week 5-6) 10\. Project planner wizard 11\. Dashboard analytics 12\. User settings 13\. Responsive refinements

**Phase 4: Polish** (Week 7-8) 14\. Animations and transitions 15\. Loading states 16\. Error handling UIs 17\. Accessibility audit 18\. Performance optimization 19\. Cross-browser testing

---

## **✅ Final Checklist**

**Visual Design**:

* Consistent spacing throughout  
* Color palette applied correctly  
* Typography hierarchy clear  
* Icons consistent style  
* Shadows appropriate for elevation  
* Brand identity evident

**Interactive Design**:

* All hover states defined  
* Loading states designed  
* Error states handled  
* Success feedback provided  
* Animations smooth and purposeful  
* Touch targets adequate size

**Responsive Design**:

* Mobile layouts complete  
* Tablet layouts defined  
* Desktop optimized  
* Breakpoints tested  
* Touch-friendly on mobile  
* Performance optimized

**Accessibility**:

* Keyboard navigation works  
* Screen reader compatible  
* Color contrast meets standards  
* Focus indicators visible  
* ARIA labels present  
* Semantic HTML used

**Content**:

* All copy written/placeholder  
* Imagery sourced  
* Empty states designed  
* Error messages helpful  
* Loading messages clear

---

## **🎨 Conclusion**

This comprehensive design documentation provides a complete blueprint for creating a production-ready, advanced-level UI for the CodeCanyon Intelligence Platform. The design emphasizes:

✅ **Professional aesthetics** \- Modern, clean, trustworthy visual identity  
 ✅ **Data clarity** \- Complex information made scannable and actionable  
 ✅ **Interactive intelligence** \- Smooth micro-interactions and real-time feedback  
 ✅ **Responsive excellence** \- Optimized for all screen sizes  
 ✅ **Accessibility first** \- Inclusive design for all users  
 ✅ **Performance focus** \- Fast loading and smooth animations

Implement these designs systematically using the priority phases, and you'll create a premium SaaS experience that rivals the best B2B data platforms. Every pixel, every animation, and every interaction has been thoughtfully specified to create a cohesive, delightful user experience.

**Now, use this documentation to guide your AI-assisted design creation or hand it to your development team for pixel-perfect implementation\!** 🚀

