# Lab 1 :-- Task 02

MIN_SCORE = 70         
MIN_ATTENDANCE = 75 
MIN_LETTERS = 1         

def check_score(score):
    return score >= MIN_SCORE

def check_documents(documents_complete):
    return documents_complete

def check_attendance(attendance):
    return attendance >= MIN_ATTENDANCE

def check_letters(letters):
    return letters >= MIN_LETTERS

def screen_student(score, documents_complete, attendance, letters):
    
    failed = []
    if not check_score(score):
        failed.append("score  < %d " % MIN_SCORE)
    if not check_documents(documents_complete):
        failed.append("documents incomplete")
    if not check_attendance(attendance):
        failed.append("attendance   <   %d%%" % MIN_ATTENDANCE)
    if not check_letters(letters):
        failed.append("no recommendation letter")
    if failed:
        return "Hold", "; ".join(failed)
    return "Review", "all conditions met"


tests = [
    ("T1_pass", 85, True, 90, 2, "Review"),
    ("T2_fail_attendance", 85, True, 60, 2, "Hold"),
    ("T3_fail_recommend", 85, True, 90, 0, "Hold"),
    ("T4_boundary", 70, True, 75, 1, "Review"),
]

print("Thresholds are synthetic lab assumptions.")
passed = 0
for name, score, docs, attendance, letters, expected in tests:
    actual, reason = screen_student(score, docs, attendance, letters)
    ok = actual == expected
    if ok:
        passed += 1
    print("_" * 60)
    print("Case     :", name)
    print("Input    : score=%d, docs_complete=%s, attendance=%d, letters=%d" % (score, docs, attendance, letters))
    print("Expected :", expected)
    print("Actual   :", actual)
    print("Reason   :", reason)
    print("Match    :", "PASS" if ok else "FAIL")
print("_" * 60)
print(" %d /%d test cases match expect" % (passed, len(tests)))