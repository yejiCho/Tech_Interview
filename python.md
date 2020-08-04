1. decorator

```
함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수이다.
일반적으로 함수의 전처리나 후처리에 대한 필요가 있을때 사용을 한다.
또한 데코레이터를 이용해, 반복을 줄이고 메소드나 함수의 책임을 확장한다.
```

- 데코레이터의 구조
함수로 만드는 데코레이터는 일반적으로 아래와 같은 구조를 가지고 있다.

```python

def out_func(func): # 기능을 추가할 함수를 인자로
    def inner_func(*args, **kwargs):
        return func(*args, **kwargs)
    return inner_func

```

- [python 데코레이터](https://medium.com/@hckcksrl/python-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator-980fe8ca5276)