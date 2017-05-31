## 2017.05.31 Practical Training with 조교

1) ./manage.py makemigrations blog 왜 여기서 blog를 치면 안될까?

왜냐하면 setting.py 안에 INSTALLED_APPS 안에 blog를 추가하지 않아서,

2) makemigrations 와 migrate 차이는, DB에 일단 Post 모델을 업로드 대기상태, migrate는 실제로 업데이트함

3) staticfiles_dirs 블로그 1,2,3

4) context의 용도 도구이고, render는 그림그리기 도화지

5) 키 값으로 접근한다

6) 

기호|명령어
---|---
{% %} | 장고 명령어
{{ }} | 장고 불러오기
{% end %} | 명령어 종료
{% csrf_token %} | forms와 세트

