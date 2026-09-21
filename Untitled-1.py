def calculate_grade(name, scores):
    """학생 이름과 점수를 받아 평균과 등급을 출력합니다."""
    average = sum(scores) / len(scores)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}님의 평균: {average:.2f}, 등급: {grade}")


calculate_grade("김민준", [85, 90, 78])

