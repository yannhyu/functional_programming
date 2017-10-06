# Traditional approach with if statements
def t_grade_description(gp):
    """Dutch grades range between 0 and 10"""
    if gp > 7:
        return 'good'
    if gp > 5:
        return 'sufficient'
    return 'insufficient'

print(t_grade_description(8))
print(t_grade_description(6))
print(t_grade_description(4))

# FP approach with if expression
fp_approach = lambda gp: 'good' if gp > 7 else 'sufficient' if gp > 5 else 'insufficient'
print(fp_approach(8))
print(fp_approach(6))
print(fp_approach(4))