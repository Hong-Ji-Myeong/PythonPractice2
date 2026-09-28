import random

def run_quiz():
    # 퀴즈 데이터 (질문, 보기, 정답 번호)
    questions = [
        {
            "question": "파이썬(Python)은 언제 처음 발표되었을까요?",
            "options": ["1. 1989년", "2. 1991년", "3. 1995년", "4. 2000년"],
            "answer": 2
        },
        {
            "question": "다음 중 파이썬의 기본 데이터 타입(자료형)이 아닌 것은?",
            "options": ["1. int", "2. str", "3. array", "4. float"],
            "answer": 3
        },
        {
            "question": "파이썬에서 함수를 정의할 때 사용하는 키워드는?",
            "options": ["1. func", "2. define", "3. def", "4. function"],
            "answer": 3
        }
    ]
    
    # 문제 순서를 무작위로 섞기
    random.shuffle(questions)
    
    score = 0
    total_questions = len(questions)
    
    print("=" * 40)
    print("       파이썬 퀴즈 앱에 오신 것을 환영합니다!       ")
    print("=" * 40)
    print(f"총 {total_questions}개의 문제가 랜덤으로 출제됩니다.\n")
    
    for i, q in enumerate(questions, 1):
        print(f"[문제 {i}] {q['question']}")
        for option in q['options']:
            print(f"  {option}")
            
        try:
            user_answer = int(input("정답 번호를 입력하세요: "))
            if user_answer == q['answer']:
                print("정답입니다! 🎉\n")
                score += 1
            else:
                print(f"틀렸습니다. 정답은 {q['answer']}번입니다.\n")
        except ValueError:
            print("숫자로 올바르게 입력해주세요. 오답 처리됩니다.\n")
            
    print("=" * 40)
    print("               퀴즈 종료!               ")
    print("=" * 40)
    print(f"총 {total_questions}문제 중 {score}문제를 맞추셨습니다.")
    
    # 결과 피드백
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("만점입니다! 완벽해요! 🏆")
    elif percentage >= 60:
        print("좋은 점수예요! 잘하셨습니다. 👏")
    else:
        print("아쉽네요. 조금 더 공부하고 도전해 보세요! 💪")

if __name__ == "__main__":
    run_quiz()