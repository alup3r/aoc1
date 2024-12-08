from icecream import ic

with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

safe_reports = 0

for report in reports:
    for i in range(len(report)):
        report_copy = report[:i] + report[i+1:]
        
        if report_copy == sorted(report_copy) or report_copy == sorted(report_copy, reverse=True):
            diffs = [abs(b-a) for a, b in zip(report_copy, report_copy[1:])]
            if all(1 <= diff <= 3 for diff in diffs):
                safe_reports += 1
                break

ic(f'The number of safe reports (with a max 1 unsafe level) is: {safe_reports}')
