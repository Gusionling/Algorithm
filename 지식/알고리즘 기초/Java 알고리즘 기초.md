
>[!클래스 명은 'Main', 패키지는 없어야 한다.]

- package없이 클래스명을 Main으로 두고 작성해야 한다. IDE에서 작성할 때 Version Controll을 위해 따로 둘 수 있으나 제출 할 때는 저렇게 해야한다. 

>[!Main 이외에 클래스를 추가로 쓰고 싶다면 public이 아닌 클래스 혹으 Inner클래스를 쓰면 된다.]

![[Pasted image 20240329161855.png]]

>[! main 함수에서 바로 작성 시, 당연하게도 모드걸 static으로 작성해야 한다. ]

- main 함수 자체가 static 함수이기 때문에 static 함수 내에서 사용하는 변수나 함수는 당연히 static 이어야 한다. 
	- 클래스의 static 메소드는 인스턴스 없이 클래스 이름으로 직접 호출될 수 있다. 따라서 static 메소드 내부에서 접근하는 변수들 역시 클래스의 인스턴스에 종속되지 않은 static 변수여야 한다. 
![[Pasted image 20240329163900.png]]
- Main 클래스의 인스터스를 생성한 다음 'solution' 인스턴스 메서드를 호출한다. 

>[!빠르게 입력 받기! Scanner는 느리다.]

- Scanner는 내부적으로 nextFloat( ) 이런걸 호출 시 다음 입력을 찾기 위해 정규식을 사용하므로 느리다. 이걸 쓰면 로직은 맞았는데도 시간초과 날 수도 있다. 
- 그러므로 BufferedReader를 쓰자
- 마찬가지로 String에 대한 split( ) 보다는 StringTokenizer로 짜르는게 더 빠르다. 따라서 입력받을 때 BufferReader와 StringTokenizer로 입력받는다면 빠르게 입력받을 수 있다. 

>[!출력도 System.out.println()은 느리다!]

- BufferedWriter로 출력을 하자
- BufferedReader나 BufferedWriter 둘 다 깔끔하게 맨 끝에 close를 해두는 것이 좋다. 
- 다만 int를 바로 출력할 수 없고, 그렇다고 ""+data 이런식으로 하기엔 String에 대한 '+' 연산 자체가 느리므로 빠른 출력을 쓰는 의미가 퇴색된다.  String.valueOf로 처리하자니 상당히 지저분하다. 그래서 내 경우엔 속도 차이가 크지 않으면서도 사용하기 쉬운 방식을 쓴다. StringBuilder로 출력할 것들을 전부 모아준 다음 그냥 System.out.println()으로 출력해주는 방식으로 다음과 같다.

![[Pasted image 20240329164753.png]]

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```
`BufferedReader`는 입력 스트림을 효율적으로 읽기 위한 클래스이다. 여기서 `System.in`은 표준 입력 스트림(보통은 키보드)을 나타낸다.

```java
int n = Integer.parseInt(br.readLine());
```
사용자로부터 첫 번째 입력을 받아 정수 `n`에 저장합니다. `br.readLine()`은 한 줄을 문자열로 읽고, `Integer.parseInt()`는 이 문자열을 정수로 변환합니다.

```java
StringTokenizer st = new StringTokenizer(br.readLine());
```

`   StringTokenizer` 클래스는 문자열을 여러 토큰으로 분할할 때 사용됩니다. 토큰은 공백, 쉼표, 점 등과 같은 구분자(delimiter)로 분리된 문자열 조각입니다. 기본적으로 `StringTokenizer`는 공백을 구분자로 사용하여 문자열을 분할합니다.

```java
int r = Integer.parseInt(st.nextToken());
int g = Integer.parseInt(st.nextToken());
int b = Integer.parseInt(st.nextToken());
```
`StringTokenizer` 객체가 생성되고 나면, `nextToken()` 메서드를 사용하여 순서대로 토큰을 하나씩 가져올 수 있습니다. 