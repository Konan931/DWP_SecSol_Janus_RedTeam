# DWP Security Solutions - Janus Red Team Toolkit (Prototype)

Generated: 2026-02-11T06:55:27.476188Z

## Contents
- `injects_bank_250.csv` — 250 synthetic injects (safe-by-design) for tabletop exercises.
- `runner_ui/` — Flask-based Runner Web UI prototype to simulate inject timeline and optionally POST webhooks to internal lab endpoints.
- `synthetic_forensic_logs_extended.csv` — Extended synthetic logs for forensics exercises.
- `tools/` — helper scripts (parsers, generators) and runner examples in Go/C/Ruby (created in earlier iteration).
- `docs/` — playbooks and tabletop facilitator guides (placeholders).

## Quickstart (local)
1. Open a terminal in the repo root.
2. Run `python -m pip install -r runner_ui/requirements.txt`
3. Start UI: `python runner_ui/app.py`
4. Browse to http://localhost:8080 and use the controls. Default is dry-run (no webhook posts).

## Safety & Legal
- All injects and logs are synthetic and intentionally void of PII or operational exploit code.
- Use only in internal lab/VPC environments. Do not run webhook targets against the public internet unless you know the endpoint is internal and trusted.
