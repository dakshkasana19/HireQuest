# HireQuest: ATS & SWOT Evaluator

**HireQuest** is an AI-powered applicant tracking system (ATS) screener and SWOT candidate evaluation tool built as a lightweight, high-performance web application. Designed for technical recruiters and candidates preparing for technical interviews, HireQuest extracts plain text from resumes, analyzes alignment against target job descriptions, computes quantifiable match ratings, identifies under-indexed skills, and generates an actionable Strengths, Weaknesses, Opportunities, and Threats (SWOT) candidate dossier.

---

## Academic Context & Problem Pool

- **Institution**: Bennett University
- **Course**: Prompt Engineering Mini-Project
- **Problem Pool**: C9 (Resume Feedback Against a Job Description)

---

## Developer Team

| Member Name | Student ID |
|---|---|
| **Daksh Kasana** | `s24cseu2714` |
| **Rohit Gangwar** | `s24cseu2533` |
| **Vabhravi Vashishth** | `s24cseu2534` |
| **Abhigyan Manit Jha** | `s24cseu0622` |
| **Saivats** | `s24cseu1436` |
| **Vishesh Agarwal** | `s24cseu2521` |

---

## Architectural Overview

```
HireQuest/
├── index.html              # Main web application (Tailwind CSS, PDF.js, UI runtime)
├── pixel_bg.jpg            # 16-bit retro pixel landscape backdrop asset
├── config.example.js       # Template for configuring Gemini API credentials
├── .gitignore              # Ignores sensitive configuration and environment variables
├── backend/
│   └── ats_helper.py       # Python text normalization & keyword scoring utilities
└── core/
    └── string_matcher.cpp  # High-performance C++ string search & indexing algorithm
```

---

## Key Features & Evaluation Engines

### 1. Client-Side PDF Parsing (PDF.js CDN)
- Parses PDF documents directly within the browser using Mozilla's PDF.js library.
- Eliminates server file transfer overhead, ensures data privacy, and enables instant resume analysis on low-bandwidth networks.
- Provides optional plain-text pasting fallback.

### 2. Live LLM Inference (`gemini-2.5-flash`)
- Interfaces directly with Google's `gemini-2.5-flash` model via REST API.
- Implements strict JSON schema definitions (`responseSchema` with type validation) ensuring predictable, parseable output structures.
- Generates numeric match ratings (0–100), executive summaries, missing keyword tags, and targeted SWOT breakdowns.

### 3. SWOT Evaluation Framework
- **Strengths [S]**: Highlights candidate's verified core proficiencies and clear alignment with JD requirements.
- **Weaknesses [W]**: Identifies explicit skill deficits, missing frameworks, or unmentioned credentials.
- **Opportunities [O]**: Recommends strategic interview talking points, architectural trade-offs, and resume enhancements.
- **Threats [T]**: Flags competitive market risks and areas where other applicants may present stronger tenure.

### 4. Built-in Offline Simulation Engine
- Operates automatically when an API key is omitted, exhausted, or when offline.
- Executes client-side heuristic keyword extraction and corpus cross-matching so the interface remains operational under all environments.

### 5. Retro 8-Bit Pixel Aesthetic
- Avoids generic AI templates in favor of a retro 8-bit / 16-bit gaming UI.
- Custom typography using Google Fonts (`Press Start 2P` headers, `VT323` body text).
- Translucent frosted glass card overlay (`rgba(255, 255, 255, 0.88)` with `backdrop-filter: blur(8px)`).
- Tactile pixelated action buttons with pressed states and segmented health-bar-style score meters.

---

## Local Development & Deployment

### Direct Browser Execution
No build tools or server setup required:
1. Clone the repository.
2. (Optional) Copy `config.example.js` to `config.js` and paste your Gemini API key.
3. Open `index.html` in any modern web browser.

### Static Web Server
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .
```

### Static Cloud Hosting
Deploy directly to GitHub Pages, Vercel, or Netlify by pointing the root directory to `index.html`.
