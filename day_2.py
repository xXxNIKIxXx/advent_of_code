def is_safe_report(report):
    levels = list(map(int, report.split()))
    increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

def is_almost_safe_report(report):
    levels = list(map(int, report.split()))
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        increasing = all(1 <= modified_levels[j+1] - modified_levels[j] <= 3 for j in range(len(modified_levels) - 1))
        decreasing = all(1 <= modified_levels[j] - modified_levels[j+1] <= 3 for j in range(len(modified_levels) - 1))
        if increasing or decreasing:
            return True
    return False

with open('day_2.txt') as f:
    reports = f.readlines()

safe_reports_count = count_safe_reports(reports)
print(f"Number of safe reports: {safe_reports_count}")