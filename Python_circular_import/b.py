

def print_b():
    print('b')

# 순환 참조 장애를 피하기 위해 함수 내에 import해서 해당 함수가 호출될 때만 import되도록 위치


def print_c():
    import a
    print('c')
    a.print_a()
