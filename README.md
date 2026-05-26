# 🪄 Magical News Fact-Checker

An enterprise-grade, multilingual AI-powered fact-checking application leveraging an **Agentic RAG** pipeline built atop the advanced **AvalAI Responses API**. This tool autonomously performs live web verification, evaluates incoming text claims, delivers structural JSON reasoning reports, and displays them via an elegant, single-page dashboard.
<img width="1849" height="838" alt="image" src="https://github.com/user-attachments/assets/d8cb218a-a1af-47a0-942b-ad0f8c1e9ecf" />

---

## 🚀 Key Features

- **Agentic RAG Engine:** Instead of building loose, decoupled web-scraping heuristics, this platform harnesses native autonomous tooling (`web_search`) exposed via AvalAI's advanced `/v1/responses` endpoint.
- **Symmetric, Scroll-Free UX:** Built utilizing Streamlit with completely custom-engineered DOM constraints. The system offers a locked-viewport grid layout (Inputs on the Left, Context and Evidence Box on the Right) completely eliminating global page scrolling.
- **Dynamic Multilingual Fluidity:** Instantaneous local shifting between Persian (featuring responsive RTL alignment and custom `Lalezar` / `Baloo Bhaijaan 2` typography) and English (styled with premium `Fredoka` font structures).
- **Enforced JSON Output Structure:** Leverages deterministic data schema serialization to guarantee responses parse reliably into semantic attributes (`status`, `confidence_score`, `explanation`, `sources`).
- **Production-Level Structural Logging:** Powered by a clean dual-handler system mapping standard tracking routines to the stdout console and structural files simultaneously (`logs/app.log`).
- **Session-Based State Audit History:** Utilizes dynamic browser state synchronization primitives to maintain a running historical audit ledger of previously vetted assertions within the current user lifecycle.

---

## 📂 Project Architecture & Directory Layout

```text
news_validator/
├── .env                  # Confidential local API configuration values
├── requirements.txt      # Pinned dependency manifests 
├── main.py               # Central execution runtime bootstrap script
├── config/
│   └── settings.py       # Decoupled environment validation and parsing engine
├── core/
│   ├── __init__.py       # Package definition index mapping 
│   ├── llm_client.py     # Network layer interfacing directly with the AvalAI Responses endpoint
│   └── pipeline.py       # Orchestration layer stitching core components together
├── prompts/
│   └── templates.json    # Isolated system prompts mapped by localization keys
├── utils/
│   └── logger.py         # Advanced logging stream multiplexer configuration
└── ui/
    └── app.py            # Streamlit responsive frontend view container
```

---

## 🛠️ Installation & Workspace Bootstrapping

Follow these programmatic setup steps to establish the environment and run the application locally:

### 1. Clone the Workspace Repository
```bash
git clone [https://github.com/Shahab-Esfandiar/Turing-Session04-Project.git](https://github.com/Shahab-Esfandiar/Turing-Session04-Project.git)
cd magical-news-factchecker
```

### 2. Prepare the Python Virtual Environment
```bash
python -m venv venv
# On Windows platforms:
venv\Scripts\activate
# On Unix or macOS systems:
source venv/bin/activate
```

### 3. Install Required Core System Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Local Environment Variables
Instantiate your localized `.env` variables container from the included example template:
```bash
cp .env.example .env
```
Open the freshly instantiated `.env` file and assign your explicit credentials:
```env
AVALAI_API_KEY=your_secured_avalai_api_key_here
AVALAI_BASE_URL=[https://api.avalai.ir/v1](https://api.avalai.ir/v1)
AVALAI_MODEL=gpt-5.5
```

### 5. Launch the Enterprise Control Panel
Initialize the dashboard lifecycle by executing the root utility script:
```bash
python main.py
```

---

## 🧩 Architectural Implementation Details

### Core Network Layer Data Contract (`core/llm_client.py`)
The system overrides standard text completion frameworks to interface directly with the advanced unified response abstractions. It specifies exact schema definitions to streamline pipeline processing:

```python
payload = {
    "model": AVALAI_MODEL,
    "instructions": system_prompt,
    "input": f"Claim/ادعا: {user_claim}",
    "tools": [{"type": "web_search"}], # Activates the autonomous web search agent
    "text": {
        "format": "json_object"        # Guarantees a parseable JSON output string
    }
}
```

### Structured Output Payload Schema
The application's internal prompt orchestrators enforce absolute formatting discipline. The downstream LLM runtime returns data exclusively bounded to the following JSON blueprint:

```json
{
  "status": "TRUE | FALSE | MISLEADING",
  "confidence_score": 95,
  "explanation": "Detailed textual context explaining the objective reality discovered during autonomous search.",
  "sources": [
    "[https://example-verified-news-source.com/article-slug](https://example-verified-news-source.com/article-slug)"
  ]
}
```

---

## 🛠️ Tech Stack
* **UI Framework:** Streamlit
* **AI Engine & Orchestration:** OpenAI SDK (configured for AvalAI Responses API)
* **Data Serialization:** JSON
* **State Management:** Streamlit Session State
* **Logging:** Python Standard Logging Library

