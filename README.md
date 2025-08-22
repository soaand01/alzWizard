
# ALZ Wizard

A lightweight Flask + Bootstrap UI that guides teams through the Azure Landing Zones (ALZ) Accelerator bootstrap and related flows.

This repository contains a multi-page wizard with focused pages and client-side helpers that make it easier to prepare VCS repos, configure bootstrap inputs, and fetch example Platform Landing Zone `.tfvars` scenarios.

Key features

- Phase-based guidance for the ALZ Accelerator (VCS, inputs, bootstrap flows)
- Centralized client-side navigation and gating (per-card confirmation checkboxes)
- Prism.js dark-themed code blocks with copy-to-clipboard buttons
- Scenario selector for Platform Landing Zone `.tfvars` examples (download and preview)

Quick start (local development)

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

If this project has a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

At a minimum you'll need Flask for local testing:

```bash
pip install flask
```

3. Run the app

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Open http://localhost:5000

What to look for

- `templates/` — Jinja2 templates powering the wizard pages.
- `templates/phases/phase2.html` — Phase 2 bootstrap page with scenario selector and download support.
- `static/` — images and other assets used by the UI.

Notes & recommendations

- Client-side fetches of raw files from GitHub can be blocked by CORS. For reliable fetching, add a small server-side proxy endpoint (e.g. `/proxy/raw?url=`) that fetches remote raw content server-side and returns it to the browser.
- The current UI includes form-generation helpers for simple scenarios; complex `.tfvars` or nested HCL constructs may not parse perfectly. Prefer editing the raw content for exact fidelity.

How to push to GitHub (local commands)

I cannot create or push a remote repository from here. Use one of the methods below on your machine.

Option B — use GitHub CLI (if installed)

```bash
gh repo create soaand01/<repo> --public --source=. --remote=origin --push
```

Optional next steps I can implement for you

- Add a small server-side proxy route to remove CORS issues when fetching raw `.tfvars` files.
- Extract the Create/Edit modal into a shared Jinja2 partial and reuse it across the Terraform flow pages.
- Add a GitHub Actions workflow to run linters or unit tests on PRs.

License

----

Add a `LICENSE` file (MIT recommended) if you want to open-source this repository.

If you want me to attempt creating the remote repo and pushing from here, tell me and provide explicit consent and the mechanism (e.g., GitHub CLI + authenticated environment or a personal access token). Do not post secrets in chat unless you truly intend to provide them securely.
