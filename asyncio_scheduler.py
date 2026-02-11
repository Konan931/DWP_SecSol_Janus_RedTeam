#!/usr/bin/env python3
# asyncio_scheduler.py - runs a runner at scheduled times (demo)
import asyncio, subprocess, datetime, argparse
async def run_at(cmd, when):
    now = datetime.datetime.utcnow()
    delay = (when - now).total_seconds()
    if delay > 0:
        await asyncio.sleep(delay)
    print(f"Starting scheduled job at {datetime.datetime.utcnow().isoformat()} -> {cmd}")
    subprocess.Popen(cmd, shell=True)
async def main(times):
    tasks=[]
    for t in times:
        tasks.append(asyncio.create_task(run_at(t[1], t[0])))
    await asyncio.gather(*tasks)
if __name__ == '__main__':
    # sample usage: schedule two runs 10s and 20s from now
    times = [(datetime.datetime.utcnow()+datetime.timedelta(seconds=10),"echo job1"), (datetime.datetime.utcnow()+datetime.timedelta(seconds=20),"echo job2")]
    asyncio.run(main(times))
