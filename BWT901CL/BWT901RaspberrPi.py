import serial 
import struct
def hex_to_short (raw_data) :
    return list (struct. unpack("hhh", bytearray (raw_data)))

DEVICE = '/dev/rfcommo'
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