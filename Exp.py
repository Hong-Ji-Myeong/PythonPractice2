def print_elements():
	print("원소 목록:")
	print("물")
	print("불")
	print("바람")
	print("흙")

def element_action(element, action):
    if action == "공격":
        print(f"{element} 원소가 공격했습니다.")
    elif action == "방어":
        print(f"{element} 원소가 방어했습니다.")
    else:
        print("공격 또는 방어만 선택할 수 있습니다.")


def element_action(element, action):
	if action == "공격":
		print(f"{element} 원소가 공격했습니다.")
	elif action == "방어":
		print(f"{element} 원소가 방어했습니다.")
	else:
		print("공격 또는 방어만 선택할 수 있습니다.")


print_elements()

for element in ["물", "불", "바람", "흙"]:
	element_action(element, "공격")
	element_action(element, "방어")
