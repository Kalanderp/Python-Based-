def check_pass_fail(marks):
    if marks >= 50:
        return "Passed"
    else:
        return "Failed"
student_marks = 45
result = check_pass_fail(student_marks)
print(result)
