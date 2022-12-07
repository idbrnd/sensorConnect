
작업 OS: Window10

# 1. 센서 세팅
라디오노드 터미널 다운로드

https://www.radionode365.com/kr/customer/download.php?bgu=view&idx=141

![](https://velog.velcdn.com/images/new_ego_doc/post/f52cf241-b695-4f16-95ef-a080c3297b56/image.png)

해당 그림의 `RadioNodeTerm`을 실행시켜주면 

![](https://velog.velcdn.com/images/new_ego_doc/post/3057df0f-e510-4551-8d9c-8b85b593bd2e/image.png)

회색 바탕의 프로그램이 시작된것을 보실 수 있으십니다.

RN171을 window 서버와 (usb)연결 시켜주면 

![](https://velog.velcdn.com/images/new_ego_doc/post/c56aa010-d1d1-49b3-a89a-724b0cc141f4/image.png)

별도의 전원은 필요없습니다. 화면에 CONF라고 표시가 되면 USB 설정 준비가 완료된 것 입니다.

![](https://velog.velcdn.com/images/new_ego_doc/post/1ea0e84e-dbcc-455c-bf75-0f28a8d44d17/image.png)

초록색 화면이 보이게 되고

"radionode114" 를 입력하게 되면 설정 터미널로 접속하게 됩니다.

![](https://velog.velcdn.com/images/new_ego_doc/post/11b89d26-86f8-46cb-a92d-cf006ff6dd20/image.png)

Enter를 치게 되면

![](https://velog.velcdn.com/images/new_ego_doc/post/6c700e0b-d276-4a88-be28-108b86ab8f67/image.png)

설정화면으로 진입됩니다.

```text
* 주의사항: 라디오노드의 펌웨어 업데이트를 꼭꼭 확인해보시길 바랍니다. 
(간혹이라고는 했지만 대부분의 센서들의 펌웨어 업데이트가 안되어서 데이터들이 모두 들어오지 않는 경우가 비일비재한듯 합니다.)
```

`“2.System Setup”` 메뉴로 진입하여 

`“B.Set Destination of HTTP”`를 선택합니다. 

3개의 목적지 중에서 `“2:CUSTOMER_V2″`를 선택합니다. 

![](https://velog.velcdn.com/images/new_ego_doc/post/4d0f0b5c-e6f0-4f7c-847d-dfc4e68b1305/image.png)

데이터의 목적지를 사용자 정의 서버 V2로 선택한 것입니다.

---

서버의 주소와 어플리케이션을 설정합니다.

`“4.HTTP Destination Setup”` 에서 설정을 합니다. 

![](https://velog.velcdn.com/images/new_ego_doc/post/9b0f91eb-ddde-49b9-85cd-d794fe976e51/image.png)

### 1. hostname을 설정합니다

<img src="https://velog.velcdn.com/images/new_ego_doc/post/e4de032a-11a6-4260-8abd-8c3321a9e71b/image.png" width="500" height="500"/>
<!-- ![a](https://velog.velcdn.com/images/new_ego_doc/post/e4de032a-11a6-4260-8abd-8c3321a9e71b/image.png){: width="100px" height="100px"} -->

`“A.Set HTTP Host URL”`를 선택합니다. 

`Enter Host URL: |` 다음과 같이 나오면 통신할 hostname을 적어주면 됩니다.

ex) `Enter Host URL: `183.111.79.82

### 2. "포트번호"를 설정합니다
<img src="https://velog.velcdn.com/images/new_ego_doc/post/e4de032a-11a6-4260-8abd-8c3321a9e71b/image.png" width="500" height="500"/>
<!-- ![b](https://velog.velcdn.com/images/new_ego_doc/post/d3f312fe-be11-4b70-beed-3e572516f653/image.png){: width="100" height="100"} -->

`“B.Set HTTP Host Port”`를 선택합니다. 

`Enter Host Port: |` 다음과 같이 나오면 통신할 hostname을 적어주면 됩니다.

ex) `Enter Host Port: `183.111.79.82

### 3. checkin endpoint 설정합니다
<img src="https://velog.velcdn.com/images/new_ego_doc/post/5ed85153-3471-4349-8ad7-26ccd6b7aba5/image.png" width="500" height="500"/>
<!-- ![d](https://velog.velcdn.com/images/new_ego_doc/post/5ed85153-3471-4349-8ad7-26ccd6b7aba5/image.png){: width="100" height="100"} -->

### 4. datain endpoint 설정합니다

<img src="https://velog.velcdn.com/images/new_ego_doc/post/d95b1281-3a1f-41a0-9cfe-61cfa6bc776d/image.png" width="500" height="500"/>
<!-- ![e](https://velog.velcdn.com/images/new_ego_doc/post/d95b1281-3a1f-41a0-9cfe-61cfa6bc776d/image.png){: width="100" height="100"} -->

저장을 확정하려면 마지막에 Q를 해서 `“4.HTTP Destination Setup”` 를 빠져나오는것까지 해주면 된다.

## 여기까지가 기기세팅 마무리!
---


# 2. 서버사이드 설정

### Check-in

![](https://velog.velcdn.com/images/new_ego_doc/post/4fb75a50-496f-42da-bc00-82ecad5c4ff7/image.png)

위와같이, 요청값이 나오게되며 **응답값**은 아래와같이 나오기만 하면 checkin 세팅이 끝납니다 

응답 charset 이 ascii or Latin1 string 인지만 확인하시면 됩니다.
editor 의 charset 이 utf-8 이면 버퍼에 encoding to ascii 한 후 내려주면 됩니다.

RN17x or RN400 에서 unicode or utf-8 charset parsing 을 지원하지 않습니다.

그리고 timestamp 는 unix timestamp(1970.01.01 ~ ) seconds( not miliseconds )를 리턴해야합니다.

![](https://velog.velcdn.com/images/new_ego_doc/post/b3c9e41a-ba84-490f-9e35-e62786623f19/image.png)

결론적으로 checkin이 되어야 data-in을 주고 받기 때문에 반드시 필요요건으로 수반되는 요청-응답 입니다.

### Data-in

![](https://velog.velcdn.com/images/new_ego_doc/post/4e0f3438-f868-4719-9aae-512620618765/image.png)

`COO`부분을 참고 하면 '|'을 기점으로 0.00,20.82,0.00,759.00 이 나오며 해당내용을 파싱해서 사용!

![](https://velog.velcdn.com/images/new_ego_doc/post/61d26e28-41c1-4960-8550-78c5beafc23e/image.png)

선택요건이지만 위에서 나온 응답값과 같이 
```xml
<xml>
<root>
<ack>ok</ack>
</root>
</xml>
```
을 응답값을 보내주어 

## 참조: radionode 공식사이트

링크1: https://help.radionode365.com/knowledge-base/rn17x-http-config

링크2: https://docs.google.com/document/d/1OsK21Y8tSvgxZspjh-ZxDVpi7ltV9qa0RS-rukoa6-U/edit 