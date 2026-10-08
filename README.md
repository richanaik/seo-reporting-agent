# 🤖 AI-Powered SEO Reporting Agent
### Autonomous Analytics Pipeline | LangGraph + Groq + GA4 + GSC

An autonomous multi-agent system that pulls live data from Google Analytics 4 and Google Search Console, detects performance anomalies, and generates formatted client-ready reports in `.docx` format — eliminating 6+ hours of manual reporting per week.

---

## 🏗️ Architecture

```
[Data Collector Agent]
        ↓
[Anomaly Detector Agent]
        ↓
[Report Writer Agent]
        ↓
[.docx Report Output]
```

**3-agent LangGraph pipeline:**
- **Data Collector** — Pulls GA4, GSC, and Google Ads data via APIs
- **Anomaly Detector** — Compares periods, flags metric changes >20%, tags severity
- **Report Writer** — Uses Groq LLaMA to write natural language client reports

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Agent Framework | LangGraph |
| LLM | Groq (openai/gpt-oss-20b) — Free tier |
| Data Sources | GA4 API, GSC API, Google Ads API |
| Report Output | python-docx (.docx) |
| Auth | OAuth 2.0 via Google Cloud |

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/seo-reporting-agent.git
cd seo-reporting-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up credentials
- Create a Google Cloud project
- Enable: Google Analytics Data API, Search Console API, Google Ads API
- Download OAuth credentials as `credentials.json` and place in root folder
- Get a free Groq API key at console.groq.com

### 5. Configure `.env`
```
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Run the agent
```bash
python main.py
```

A browser window will open for Google OAuth on first run. After that, tokens are cached automatically.

---

## 📄 Sample Output

The agent generates a fully formatted `.docx` report including:

- **Executive Summary** — Plain English overview of the period
- **Traffic & Engagement** — GA4 analysis with anomaly explanations
- **Search Performance** — GSC clicks, impressions, CTR, top queries
- **Paid Advertising** — Google Ads summary (demo or live)
- **Recommendations** — 3 actionable bullet points
- **Next Steps** — What to monitor the following week

Reports are saved to the `output/` folder as:
```
SEO_Report_ClientName_YYYYMMDD.docx
```

---

## 🚧 Planned Features

### 1. ⏰ Automated Scheduling (Windows Task Scheduler)
Run the agent automatically every Monday morning without manual intervention.
- Use Windows Task Scheduler to trigger `python main.py` on a schedule
- Set trigger: Weekly → Monday → 8:00 AM
- Point it to the `venv` Python executable for correct environment
- Reports will be generated and saved to `output/` automatically

### 2. 📧 Email Delivery (Gmail API)
Automatically send the generated `.docx` as an email attachment to the client.
- Add Gmail API scope and credentials to Google Cloud project
- Use `google-api-python-client` to compose and send email with attachment
- Trigger email send at end of `report_writer_agent` after `.docx` is saved
- Client receives a polished report in their inbox every Monday

### 3. 👥 Multi-Client Support
Generate reports for multiple clients in a single run.
- Define a `clients.json` file with a list of client configs (name, GA4 ID, GSC URL)
- Loop through clients in `main.py` and invoke the pipeline for each
- Each client gets their own dated `.docx` saved to `output/`
- Combine with email delivery to fully automate multi-client reporting

### 4. 🎨 Branded .docx Formatting
Add logo, brand colors, cover page, and styled sections to the Word report.
- Use `python-docx` styles to set custom fonts, heading colors, and spacing
- Add a cover page with logo image, client name, report date, and agency branding
- Apply consistent table styles for metrics sections
- Output a report that looks agency-grade out of the box

---

## 📁 Project Structure

```
seo-reporting-agent/
├── agents/
│   ├── data_collector.py      # Agent 1: Pulls GA4, GSC, Ads data
│   ├── anomaly_detector.py    # Agent 2: Detects metric anomalies
│   └── report_writer.py       # Agent 3: LLM report generation + .docx
├── tools/
│   ├── ga4_tool.py            # Google Analytics Data API
│   ├── gsc_tool.py            # Google Search Console API
│   └── google_ads_tool.py     # Google Ads (demo data)
├── output/                    # Generated reports land here
├── graph.py                   # LangGraph pipeline wiring
├── main.py                    # Entry point
├── requirements.txt
├── .env                       # API keys (not committed)
├── .gitignore
└── README.md
```

---

## 👩‍💻 Built By

**Richa Naik** — SEO Team Lead & AI Agent Builder  
[LinkedIn](https://www.linkedin.com/in/richanaik777/) | [Portfolio](https://richa-portfolio-ochre.vercel.app/)

---

*Part of an agentic AI portfolio showcasing autonomous marketing automation systems.*
