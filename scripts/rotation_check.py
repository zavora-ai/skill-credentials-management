#!/usr/bin/env python3
"""Check which credentials need rotation based on age and policy."""
import json, sys
from datetime import datetime

def check(credentials):
    results = []
    for cred in credentials:
        last_rotated = cred.get("last_rotated", "")
        max_age_days = cred.get("max_age_days", 90)
        if last_rotated:
            rotated = datetime.fromisoformat(last_rotated.replace("Z", "+00:00")).replace(tzinfo=None)
            age_days = (datetime.now() - rotated).days
            needs_rotation = age_days > max_age_days
            results.append({**cred, "age_days": age_days, "needs_rotation": needs_rotation, "overdue_by": max(0, age_days - max_age_days)})
    return sorted(results, key=lambda x: x.get("overdue_by", 0), reverse=True)

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
