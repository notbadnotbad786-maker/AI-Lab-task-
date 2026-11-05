

def symbolic_rule(score, complete):
    if complete and score >= 70:
        return "Review "
    else:
        return " Hold"

def threshold_rule(probability):
    if probability >= 0.70:
        return "Review"
    else:
        return "Hold"

cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]

print("case  |  symbolic  |  threshold  |  disagreement ")

for name, score, complete, probability in cases:
    symbolic_result = symbolic_rule(score, complete)
    threshold_result = threshold_rule(probability)
    print(name, symbolic_result, threshold_result, symbolic_result != threshold_result, sep="  |  ")