
#!/usr/bin/env python3
# generate_injects.py - programmatic inject CSV generator
import csv, argparse, datetime, random
from pathlib import Path

def make_injects(output, count=10):
    out = Path(output)
    rows = []
    for i in range(count):
        phase = random.choice(['Signal','Ambiguity','Decision'])
        minute = random.randint(5,180)
        rows.append({
            'id':f'X{i:03d}',
            'minute':minute,
            'phase':phase,
            'inject_type':random.choice(['monitoring_alert','ingest_file','media_inquiry','training_job']),
            'message':f'Synthetic inject message {i} for phase {phase}.',
            'expected_response':'Triage; collect logs; escalate if severity high.',
            'severity':random.choice(['low','medium','high','critical']),
            'artifact_reference':''
        })
    with open(out,'w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print('Wrote', out)

if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'injects_generated.csv'
    make_injects(out, count=50)
