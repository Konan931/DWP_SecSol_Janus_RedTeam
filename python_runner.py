#!/usr/bin/env python3
# python_runner.py - Simulated real-time inject runner for tabletop exercises
# Usage: python python_runner.py --csv injects_master_all.csv [--speed 1.0] [--webhook http://endpoint] [--dry-run]
import csv, time, argparse, datetime, json, sys, requests

def load_injects(path):
    injects = []
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                row['minute'] = int(row.get('minute') or 0)
            except:
                row['minute'] = 0
            injects.append(row)
    injects.sort(key=lambda x: x['minute'])
    return injects

def send_webhook(url, payload, dry_run=True, timeout=5):
    print(f\"[webhook] {'DRY-' if dry_run else ''}POST to {url} payload keys: {list(payload.keys())}\")
    if dry_run:
        return None
    try:
        resp = requests.post(url, json=payload, timeout=timeout)
        print(f\"[webhook] status={resp.status_code}\")
        return resp
    except Exception as e:
        print(f\"[webhook] error: {e}\")
        return None

def run_simulation(injects, speed=1.0, webhook=None, dry_run=True):
    start = datetime.datetime.utcnow()
    print(f\"Simulation start (UTC): {start.isoformat()} | speed={speed}x | webhook={'set' if webhook else 'none'} | dry_run={dry_run}\")
    for inj in injects:
        # simulated wait until inj['minute'] scaled by speed
        target = start + datetime.timedelta(minutes=inj['minute']/speed)
        while datetime.datetime.utcnow() < target:
            time.sleep(0.5)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        out = {
            'time': now,
            'id': inj.get('id'),
            'minute': inj.get('minute'),
            'phase': inj.get('phase'),
            'type': inj.get('inject_type'),
            'message': inj.get('message'),
            'severity': inj.get('severity')
        }
        print(f\"[{now}] INJECT {out['id']} ({out['phase']}) severity={out['severity']}: {out['message']}\")
        if webhook:
            send_webhook(webhook, out, dry_run=dry_run)
    print(\"Simulation finished.\")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--csv', required=True)
    p.add_argument('--speed', type=float, default=10.0, help='Scale: minutes/simulated-minute (higher = faster)')
    p.add_argument('--webhook', type=str, default=None, help='Optional webhook URL to POST injects to (use --dry-run to avoid actual network calls)')
    p.add_argument('--dry-run', action='store_true', default=True, help='If set, do not actually perform HTTP calls')
    args = p.parse_args()
    injects = load_injects(args.csv)
    run_simulation(injects, speed=args.speed, webhook=args.webhook, dry_run=args.dry_run)
