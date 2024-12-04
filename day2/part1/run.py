#!/usr/bin/env python

def get_safe_reports():
    safe_counter = 0
    filename = 'input.txt'
    with open(filename) as f:
        for line in f:
            report = list(map(int, line.strip().split()))
            if report == sorted(report, reverse=True) or report == sorted(report):
                safe = True
                for n in range(1, len(report)):
                    distance = abs(report[n-1] - report[n])
                    if distance < 1 or distance > 3:
                        safe = False
                        break
                if safe:
                    safe_counter += 1
    return safe_counter


def main():
    safe_reports = get_safe_reports()
    print(f'Number of safe reports: {safe_reports}')

if __name__ == "__main__":
    main()
