
# ALZ Wizard 🚀

A lightweight Flask + Bootstrap UI that guides teams through the Azure Landing Zones (ALZ) Accelerator bootstrap and related flows.

This repository contains a multi-page wizard with focused pages and client-side helpers that make it easier to prepare VCS repos, configure bootstrap inputs, and fetch example Platform Landing Zone `.tfvars` scenarios.

Key features

- Phase-based guidance for the ALZ Accelerator (VCS, inputs, bootstrap flows)
- Centralized client-side navigation and gating (per-card confirmation checkboxes)
- Prism.js dark-themed code blocks with copy-to-clipboard buttons
- Scenario selector for Platform Landing Zone `.tfvars` examples (download and preview)

Quick start (local development)
A lightweight Flask + Bootstrap web UI that guides you through the Azure Landing Zones (ALZ) Accelerator
bootstrap and deployment flows. The ALZ Wizard is intended as a helper and reference UI — it complements the
ALZ Accelerator documentation and starter repositories; it does not replace them.

This project provides:

- A multi-step, phase-based wizard UI implemented with Flask (Jinja2 templates) and Bootstrap. 🧭
- Centralized client-side behaviors (per-card gating checkboxes, navigation wiring, Prism.js code copy buttons). 🛠️
- Phase 2 helpers: bootstrap flow selection, starter inputs download, and Platform Landing Zone scenario `.tfvars` preview/download. 📁
- A Finish page that summarizes the wizard phases and offers a downloadable phase summary. 📄

⚙️ Quick start (local development)

1. Create and activate a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

If a `requirements.txt` file exists in the repo, install it:

```bash
pip install -r requirements.txt
```

If not, at minimum install Flask for local testing:

```bash
pip install flask
```

3. Run the app locally

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Then open: http://localhost:5000

📁 Project layout (high-level)

- `app.py` — small Flask router that renders the wizard views.
- `templates/` — Jinja2 templates for each page and shared partials (including `base.html` which contains the centralized client JS).
- `static/` — static assets (images, icons) used by the UI.

🧭 Phases (what the wizard covers)

- Phase 0 — Planning: Collect your decisions and scope (subscriptions, naming, governance) before bootstrapping.
- Phase 1 — Prepare & Bootstrap: Configure accounts, roles, and subscriptions; select your VCS and run the ALZ bootstrap to generate starter inputs.
- Phase 2 — Inputs & Bootstrapping Flows: Choose a flow (Azure DevOps + Terraform or GitHub + Terraform), download or edit starter inputs, and select platform `.tfvars` scenarios.
- Phase 3 — Deployment: Trigger your CD pipeline (GitHub Actions or Azure Pipelines) or run local deploy scripts; review plan & apply steps.
- Post-deploy & Cleanup: Validate deployed resources, configure monitoring/policies, and perform cleanup for test environments.

✅ Features & UX notes

- Per-card gating: many pages require a confirmation checkbox before allowing you to continue (this prevents accidental navigation).
- Prism.js integration: code blocks use an okaidia (dark) theme and a copy-to-clipboard button.
- Scenario downloads: Phase 2 attempts to fetch raw `.tfvars` examples from upstream repositories; however, direct client fetches can be blocked by CORS.
	For reliable retrieval, add a small server-side proxy endpoint (for example `/proxy/raw?url=`) that fetches remote raw files server-side and returns them to the browser.
- Finish page: the app now includes a `/finish` page that summarizes what the wizard covered and provides a downloadable text summary.

💾 Persisted choices & summary

- The UI uses localStorage for lightweight persistence of a few selections (for example: `phase2_flow`, `phase2_scenario`, `phase3_deployTarget`).
- The `/finish` page reads those keys (if present) to personalize the experience. If you prefer server-side state, we can add Flask session storage or a small backend API.

📤 How to push to GitHub from your machine

If you prefer using the GitHub CLI (recommended for convenience):

```bash
gh repo create soaand01/alzWizard --public --source=. --remote=origin --push
```

📝 Notes about this repository

- This repository is already created on GitHub at: https://github.com/soaand01/alzWizard
- I committed and pushed recent changes (finish page, README updates, and template edits) to `origin/main`.

🔧 Recommendations / next improvements I can implement

- Add a server-side proxy endpoint (`/proxy/raw`) to avoid CORS issues when fetching raw `.tfvars` from upstream repos.
- Persist user selections server-side (Flask sessions or a small API) if you want multi-device continuity.
- Extract shared UI components (Create/Edit modal) into Jinja2 partials to reduce duplication.
- Add a GitHub Actions workflow to run linters and smoke tests on push/PR.


 
