# 장고로 만든 간단한 RESTfull API 클론코딩 

## 개발 시 사용한 세팅
```
Python 3.11.0
Django 4.1.5
djangorestframework 3.14.0
sqllite 3.37.2
```

## 목적
* RESTfull API를 django와 Python을 사용하여 데이터를 Json형식으로 주고받는 것을 연습해본다.

## open API 연계
* nexon developers 연계
* OAuth 2.0 : Authorization Code Grant 인증 방식 사용 (인증키)
    * OAuth2.0 에서 가장 많이 사용되는 인증방식, Accesstoken을 얻기 위해 사용되는 인증방식이다.
    * S2S 방식으로 백엔드서버가 있는 서비스에 적용하기 적합하다.
    * 클라이언트는 써드파티 서비스의 백엔드 서버이다.
    * client-secret, Access-token과 같은 민감정보가 외부에 노출되지 않아 보안상 안전


## 참조
* https://yooloo.tistory.com/150
