# pass와 continue의 차이

```python
for element in some_list:
    if not element:
        pass

for element in some_list:
    if not element:
        continue

```

1. pass는 단순히 실행할 코드가 없다는 것을 의미한다.
2. continue는 다음 순번의 loop를 강제적으로 돌도록 하는 것

## break
- 반복문을 종료 시키는 기능

```python
list_ = [1,2,3,4,5,6,7]

for val in list:
    if val % 3 == 0:
        print(val)
        break

```