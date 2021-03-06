# algorithm

1. stack

```
Stack은 선형 자료구조로, LIFO나중에 들어간 원소가 먼저 나오는 형태입니다.
함수의 콜/스택, 브라우저 뒤로가기에 쓰입니다.

```

2. Queue

```
FIFO구조로 컴퓨터 버퍼에 사용되는 선형 알고리즘입니다.
remove(),is_empty(),peek(),add()로 구성됩니다.
Queue는 먼저 들어간 원소가 먼저 나오는 구조입니다.
컴퓨터 버퍼에 주로 사용됩니다.

```

3. 이진탐색

```
데이터가 정렬돼있는 배열에서 특정한 값을 찾아내는 알고리즘.
배열의 중간에 있는 임의의 값을 선택하여 찾고자 하는 값 X와 비교한다. 
X가 중간 값보다 작으면 중간 값 기준으로 좌측의 데이터들을 대상으로 탐색한다. 
해당 값을 찾을 때까지 이 과정을 반복한다.

이진탐색알고리즘은 정렬된 데이터가 아니면 적용이 불가능
```

4. 해시테이블(hash table)

```
효율적인 탐색을 위한 자료구조로서 키(key)를 값(value)에 대응시킨다.

충돌이 자주 발생한다면 최악의 경우 수행시간은 O(N)이 된다.
N은 키의 개수

충돌을 최소화 할 경우는 O(1)탐색 시간이 걸린다.

```

- 해시테이블에서 충돌 해결하는 방법

1. 연결리스트를 이용한 체이닝(chaining)
```
해시테이블의 각 원소가 연결리스트로 대응된 방법
데이터를 그냥 연결리스트에 추가하면 된다.
충돌되는 횟수가 꽤 작을 경우에는 이 방법 사용
```


5. 트리(tree)

- 트리는 하나의 루트 노드를 갖는다.
- 루트노드는 0개 이상의 자식 노드를 갖고있다.
- 그 자식 노드 또한 0개 이상의 자식 노드를 갖고 있고,
이는 반복적으로 정의 된다.

트리에는 사이클(cycle)이 존재할 수 없다.

6. 그래프(graph)

트리는 사이클(cycle)이 없는 하나의 연결 그래프(connected graph)이다.

```
그래프는 단순히 노드와 그 노드를 연결하는
간선(edge)를 하나로 모아놓은 것과 같다.

```

- 그래프의 탐색

```
깊이 우선 탐색(DFS)은 루트노드에서 시작해서
다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

넓게 탐색하기 전에 깊게 탐색한다는 뜻

너비 우선 탐색(BFS)는 루트노드에서 시작해서 인접한 
노드를 먼저 탐색하는 방법을 말한다.

깊게 탐색하기 전에 넓게 탐색한다는 뜻
```