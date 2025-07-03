import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    """Return the grade for a score, given the breakpoints and grades."""
    i = bisect.bisect(breakpoints, score)
    return grades[i]

scores = [33, 99, 77, 70, 90, 89, 100, 59, 60, 61]
grades = [grade(score) for score in scores]

print(f"Scores: {scores}")
print(f"Grades: {grades}")