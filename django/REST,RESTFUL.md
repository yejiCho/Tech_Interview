# REST가 의미하는 것

```
REST(REpresentational State Transfer)
표현된 상태라고 할수 있다.

즉, REST는 통신을 통해 자원의 표현된 상태를 주고받는 것에 대한 아키텍쳐 가이드라인이라고 할 수 있다.
```

- 사실 주고 받는 것은 리소스가 아니다.

```
우리가 API를 통해 주고 받는 리소스는 어떤 문서일수도 있고,
이미지 또는 단순한 JSON데이터일 수도 있다.
하지만 사실 우리는 리소스를 직접 주고 받는 것이 아니다.
```

```json
GET https://iamserver.com/api/users/2
Host: iamserver.com
Accept: application/json
```

```
클라이언트는 이 API 엔드포인트를 사용하여 서버에게 2번 유저의 자원을 요청했고, 서버가 요청을 성공적으로 처리했다면 클라이언트는 서버로부터 대략 이런 느낌의 응답을 받을 수 있다.
```

```json
HTTP/1.1 200 OK
Content-Length: 45
Content-Type: application/json

{
    id:2,
    name:'Evan',
    org:'Viva Republica',
}

```

- 리소스를 표현한 상태라는 것의 의미

```
앞서 이야기했듯이 REST가 이야기하는 Representation State라는 단어는 원본 리소스를 표현한 상태라는 것을 의미

원본 리소스는 데이터베이스에 저장된 하나의 로우로서 존재하지만 클라이언트에게 이걸 그대로 넘겨줄 수는 없으니
서버가 원본 리소스를 읽어와서 적당한 상태로 표현해주는 것
```

```json
GET https://iamserver.com/api/users/2
Host: iamserver.com
Accept: application/json
```

```
앞서 이야기했듯이, REST는 결국 리소스를 어떻게 하면 명확하게 표현할 수 있을지에 대한 것에 집중하는 아키텍처 스타일이다. 하지만 우리가 HTTP API를 사용할 때는 단순히
리소스의 표현 상태만으로는 클라이언트가 API를 호출했을 때
서버에서 정확히 어떤 일이 발생하는지 알기가 어렵다.

REST는 단지 리소스가 표현된 상태만을 이야기할 뿐, 어떠한 "행위"에 대해서는 이야기하고 있지 않기 때문이다.
하지만, 클라이언트가 서버의 API를 사용할 때 원하는 것은 
소스를 생성하거나 삭제하거나 수정하는 등 명백히 어떠한
행위이다.
```
# RESTful API

```
RESTful API는 REST아키텍쳐를 통해 표현된 리소스와 더불어
어떠한 행위를 명시할 수 있는 HTTP메소드와 URI까지 활용하게
되며, 각 요소들이 표현하고 있는 것들은 다음과 같다.
```

1. 리소스가 어떻게 표현되는지? - REST
2. 어떤 리소스인지? - URI
3. 어떤 행위인지? - HTTP 메소드

- URI를 사용하여 어떤 리소스인지 표현하자
```
RESTful API의 URI는 이 API가 어떤 리소스에 대한 API인지를
나타내는 요소이다.
```

- 리소스의 계층을 표현하기
```
일반적으로 유저들은 각각 고유한 ID를 가지고 있는 경우가 많으니, 이 ID를 사용하면 특정한 표현할 수 있는데...

GET /users/2
```

- URI에는 행위가 표현되면 안된다.
```
RESTful API의 URI를 설계할 때, 중요한 것은 URI에 어떠한 행위를 의미하는 표현이 포함되어서는 안된다.
```

```
POST /users/2/delete
```

### HTTP 메소드를 사용하여 어떤 행위인지 표현하자

- API를 사용하여 하게되는 행위는 CRUD(CREATE,READ,UPDATE,DELETE)
- 몇가지 특수한 경우를 제외하면 단 5가지의 HTTP메소드만으로 정의가능

|Method|의미|
|:-:|:-:|
|GET|리소스를 조회한다.|
|POST|리소스를 대체한다.|
|DELETE|리소스를 삭제한다.|
|POST|리소스를 생성한다.|
|PATCH|리소스의 일부를 수정한다.|