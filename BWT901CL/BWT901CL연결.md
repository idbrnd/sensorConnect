작업 OS: Raspberry pi OS (Raspberry Pi 4 공식 지원 OS)

# Raspberry PI 와 RC-06(해당 센서) 연결

## RC-06 MAC address 찾기

![image](https://user-images.githubusercontent.com/53653597/209905086-49994be0-4bf0-4b33-9563-6096672b10b0.png)

![image](https://user-images.githubusercontent.com/53653597/209905156-dac16813-59d6-4838-a57c-3067cc59b598.png)

"scan on" 입력해서 연결 가능한 블루투스 모듈 찾기

![image](https://user-images.githubusercontent.com/53653597/209905345-b5cdf6fb-0059-46ca-b3bc-34a6a9ce0e0c.png)

노란색으로 된 부분이 MAC 주소!

`00:0C:BF:09:25:2F` 를 찾았으며

**"scan off"** 해당 스캔을 종료해줍니다.

![image](https://user-images.githubusercontent.com/53653597/209905454-f03e83f3-3680-49b8-8b57-2e405950c11e.png)

**exit**으로 bluetoothctl에서 빠져 나옵니다

![image](https://user-images.githubusercontent.com/53653597/209907192-ce0d9973-22f4-4222-b758-598feb4d807a.png)


## rfcomm bind

해당 컴퓨터(라즈베리파이)와 바인드 작업을 실행합니다.

```shell
rfcomm bind 0 00:0C:BF:09:25:2F
```

0 을 포트 넘버로 해당 기기와 연결이 되면 해당 포트로 통신합니다.

## Checking binding

위의 스크립트로 `/dev/rfcomm0`가 생성되었는지 확인해 줍니다.

```bash
ls /dev/rfcomm0
```
bind 된 포트 넘버가 `N`이라면 `/dev/rfcommN`으로 생성됩니다.

<br>
<br>

# 시리얼 통신

**`BWT901RaspberrPi.py`** 파일의 코드를 사용해서 해당 값이 어떻게 들어오는지 확인해보면 됩니다.

```python
import serial 
import struct
def hex_to_short (raw_data) :
    return list (struct. unpack("hhh", bytearray (raw_data)))

DEVICE = '/dev/rfcomm0'
BAUD_RATE = 115200

# Connect to the device
ss = serial. Serial (DEVICE, BAUD_RATE)
print ('Connect to', DEVICE)
# Send data
# ss.write (b'hello\n')
# Receive data


while (True) :
    # 길이가 44로 고정
    data = ss. read (44) 
        #0x55가 아니면 시작 지점이 아니기 때문에 시작지점 확인 
        if (data [0] != 0×55) :
            continue
        
        # BWT901CL Manual.pdf 참조
        #hex array의 두번째 요소가 0x50 ~ 54,59 의 경우 각각 확인
        if (data [1] == 0×50): # 날짜 및 현재 시간 정보
            print ("year", data [2]) 
            print ("month", data[3]) 
            print ("day", data [4])
        
        if (data [1] == 0×51): # 가속도와 각도
            #print (51, data)
            acc = [hex_to_short(data[2:8])[i] / 32768.0 * 16 for i in range (0,3)]
            angle = [hex_to_short(data [14:20])[i] / 32768.0 * 180 for i in range (0,3)]
            print("acc" ‚acc)
            print("angle", angle)
            continue
        
        if (data [1] == 0×52): # angluar velocity의 정보
            #print (52, data)
            angularVelocity = [hex_to_short(data[2:8])[i] / 32768.0 * 2000 for i in range (0,3)]
            print ("angularVelocity", angularVelocity)
            continue
        
        if (data[1] == 0×53) : # 실제 각도 값
            #print (53, data)
            angle = [hex_to_short(data[2:8])[i] / 32768.0 * 180 for i in range (0,3)]
            print("angle" ‚angle)
            continue
        
        if (data [1] == 0×54): # magnetic 정보 추출
            #print (54, data)
            magnetic = [hex_to_short(data[2:8])[i] for i in range (0,3)]
            print("magnetic" magnetic)
            continue
        
        if (data [1] == 0×59):
            print(59, data)
```
