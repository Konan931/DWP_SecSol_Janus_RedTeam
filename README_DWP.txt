
DWP Security Solutions - Red Team Artifacts
Generated: 2026-02-11T06:46:35.536507Z

Artifacts in this directory:
- injects_master_all.csv (master list with base + variants)
- injects_phase1_signal.csv, injects_phase2_ambiguity.csv, injects_phase3_decision.csv
- injects_master.csv (original)
- synthetic_forensic_logs_extended.csv (forensics)
- python_runner.py (simulated real-time runner, optional webhook)
- go_runner.go (Go runner)
- asyncio_scheduler.py, go_scheduler.go (scheduler examples)
- role PDFs with branding: *_DWP.pdf
- parser examples: parse_injects.go, parse_injects.c, parse_injects.rb
- generate_injects.py (generator)

Usage notes:
- All injects & logs are synthetic and safe-by-design for tabletop exercises.
- python_runner.py supports --webhook and --dry-run. By default --dry-run is True (no network calls).
- If you want actual webhook posting during runs, run with --dry-run False and provide a webhook URL. Ensure the endpoint is internal and trusted.

Legal & Safety:
- Do not use any of these artifacts against real production systems or with PII. These are for controlled lab environments only.
- Keep all network endpoints internal. DWP Security Solutions assumes no liability for misuse.
