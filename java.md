## java

- 오버로딩과 오버라이딩 차이

오버로딩(Overloading)

두 메서드가 같은 이름을 갖고 있으나 인자의 수나 자료형이 다른 경우

```java

public double computeArea(Circle c){}
public double computeArea(Circle c1, Circle c2){}
public double computeArea(square c){}

```

오버라이딩(Overriding)

상위 클래스의 메소드와 이름의 용례가 같은 함수를 하위 클래스에 재정의 하는 것
상속관계 있는 클래스 간에 이름의 메소드를 정의

```java

public abstract class Shape {
    public void printMe() {System.out.println("Shape");}
    public abstract double computeArea();
}

public class Circle extends Shape {
    private double rad = 5;
    @Override
    public void printMe() {System.out.println("Shape");}
    public double computeArea(){return rad * rad * 3.15;}
}

public class Ambigous extends Shape {
    private double area = 10;
    public double computeArea() {return area;}
}
```

- call by value 와 reference 차이

call by value(값에 의한 호출)

```
함수가 호출될 때, 메모리 공간 안에서는 함수를 위한 별도의 임시공간이 생성

함수 호출시 전달되는 변수의 값을 복사하여 함수의 인자로 전달. 복사된 인자는 지역변수 특성을 가진다.

따라서 함수 안에서 인자의 값이 변경되어도, 외부의 변수의 변경되지 않는다.
```

call by reference(참조에 의한 호출)

```
함수가 호출될 때, 메모리 공간 안에서는 함수를 위한 별도의 임시공간 생성 

호출방식은 함수 호출시 인자로 전달되는 변수의 레퍼런스를 전달한다 (해당 변수를 가리킨다.)

따라서 함수 안에서 인자의 값이 변경되면, argument로 전달된 객체의 값도 함께 변경된다.
```

- 객체지향 프로그래밍과 절차지향 프로그래밍 차이

```

절차지향 프로그래밍

- 실행하고자 하는 절차를 정하고, 이 절차대로 프로그래밍하는 방법
- 목적을 달성하기 위한 일의 흐름에 중점
- 순차적 실행에 초점

객체지향 프로그래밍

- 실세상의 물체를 객체로 표현하고, 이들 사이의 관계, 상호작용 프로그램을 나타냄
- 객체를 추출하고 객체들의 관계를 결정하고 이들의 상호작용에 필요한 함수와 변수를 설계 및 구현
- 핵심은 연관되어 이쓴 변수와 메서드를 하나의 그룹으로 그룹핑
- 객체간의 관계/조직에 초점

```

- 클래스 객체 인스턴스 차이

클래스 class

```
객체를 만들어 내기 위한 설계도 혹은 틀
연관되어 있는 변수와 메서드의 집합
```

객체 object

```
소프트웨어 세계에 구현할 대상
클래스에 선언된 모양 그대로 생성된 실체
```

- 동기 비동기 

동기 (Synchronous)

```
말 그대로 동시에 일어난다.
요청과 그 결과가 동시에 일어난다.

설계가 매우 간단하고 직관적이지만 결과가 주어질 때까지 대기해야한다.

```

비동기 (Asynchronous)

```
동시에 일어나지 않는 것을 의미
요청과 결과가 동시에 일어나지 않는다.

동기보다는 복잡하지만 결과가 주어지는데 시간이 걸리더라도
그 시간동안 다른 작업을 할 수 있으므로 자원을 효율적으로
사용할 수 있습니다.
```