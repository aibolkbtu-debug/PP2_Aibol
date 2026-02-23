import sys
from datetime import datetime

def get_data(line):
    parts = line.strip().split()
    date_part = parts[0]
    tz_part = parts[1].replace('UTC', '')
    
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    sign = 1 if tz_part[0] == '+' else -1
    h, m = map(int, tz_part[1:].split(':'))
    offset = sign * (h * 3600 + m * 60)
    
    return dt.timestamp() - offset, dt.year, dt.month, dt.day, offset

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def solve():
    lines = sys.stdin.readlines()
    if len(lines) < 2: return
    
    b_utc, b_y, b_m, b_d, b_offset = get_data(lines[0])
    c_utc, c_y, c_m, c_d, c_offset = get_data(lines[1])
    
    results = []
    for year in [c_y, c_y + 1, c_y + 2]:
        ty, tm, td = year, b_m, b_d
        if b_m == 2 and b_d == 29 and not is_leap(year):
            tm, td = 2, 28
            
        target_dt = datetime(ty, tm, td)
        target_utc = target_dt.timestamp() - b_offset
        
        diff = target_utc - c_utc
        if diff >= 0:
            results.append(int(diff))
            
    s = min(results)
    print((s + 86399) // 86400)

if __name__ == "__main__":
    solve()