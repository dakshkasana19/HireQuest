# HireQuest: ATS & SWOT Evaluator

**HireQuest** is an AI-powered applicant tracking system (ATS) screener and SWOT candidate evaluation platform built as a lightweight single-page web application. It evaluates candidate resumes against targeted job descriptions, calculates quantifiable match scores, highlights missing technical keywords, and synthesizes a structured Strengths-Weaknesses-Opportunities-Threats (SWOT) candidate analysis.

---

## Academic Context & Problem Pool

- **Institution**: Bennett University
- **Coursework**: Prompt Engineering Mini-Project
- **Problem Pool**: C9 (Resume Feedback Against a Job Description)

---

## Developer Team

- **Daksh Kasana** — `s24cseu2714`
- **Rohit Gangwar** — `s24cseu2533`
- **Vabhravi Vashishth** — `s24cseu2534`
- **Abhigyan Manit Jha** — `s24cseu0622`
- **Saivats** — `s24cseu1436`
- **Vishesh Agarwal** — `s24cseu2521`

---

## Core Capabilities

- **Client-Side PDF Text Extraction**: Uses PDF.js CDN to read candidate resumes directly within the browser with 0MB server payload overhead.
- **Direct Gemini 2.5 Flash Inference**: Sends structured prompts with strict JSON schema enforcement to `gemini-2.5-flash`.
- **SWOT Candidate Evaluation Framework**:
  - **[S] Strengths**: Candidate's core technical skills, verified achievements, and alignment with the job description.
  - **[W] Weaknesses**: Skill gaps, missing tools, or experience mismatches against specified criteria.
  - **[O] Opportunities**: Areas for high-impact interview pivoting, narrative positioning, and resume enhancement.
  - **[T] Threats**: Potential risks in candidate profile compared to competitive applicants.
- **Built-in Offline Heuristic Simulation**: Runs automatically if network interruptions or API rate limits occur.
- **8-Bit Retro Pixel UI**: Built with custom retro borders, pixelated progress meters, and translucent overlay cards.

---

## Deployment & Running Locally

### Option 1: Direct Browser Launch (No Build Tools Required)
1. Clone or download this repository.
2. Open `index.html` in any modern web browser (Google Chrome, Firefox, Safari, Microsoft Edge).

### Option 2: Local Static Web Server
```bash
# Using Python
python -m http.server 8000

# Or using npx serve
npx serve .
```
Navigate to `http://localhost:8000`.

### Option 3: Public Static Hosting
`index.html` is located at the root directory alongside `pixel_bg.jpg`. You can deploy this repository directly to:
- **GitHub Pages**: Go to Repository Settings → Pages → Deploy from branch (`main` / root).
- **Vercel**: Import project repository with zero configuration required.
- **Netlify**: Drag-and-drop the directory or connect your Git repository.
