#  복잡한 표현식 대신 헬퍼 함수 작성

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

print(repr(my_values))


#  로직을 반복해서 사용해야 한다면 헬퍼 함수 만드는게 좋음

def get_first_int(values, key, default=0):
    found = values.get(key,[''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')
print(green)