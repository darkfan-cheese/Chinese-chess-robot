import smbus2  #调用树莓派IIC库
import time
import os

class TTS:
      
    address = None
    TTS_MODULE_I2C_ADDR =  0x40 #传感器的IIC地址

    def __init__(self, bus=1):
        self.address = self.TTS_MODULE_I2C_ADDR
        self.bus = smbus2.SMBus(bus)

    def TTSModuleSpeak(self, sign, words):
        head = [0xFD,0x00,0x00,0x01,0x00]             #文本播放命令
        wordslist = words.encode("gb2312")            #将文本编码格式设为GB2312
        signdata = sign.encode("gb2312")    
        length = len(signdata) + len(wordslist) + 2
        head[1] = length >> 8
        head[2] = length
        head.extend(list(signdata))
        head.extend(list(wordslist))      
        write = smbus2.i2c_msg.write(self.address, head)  
        self.bus.i2c_rdwr(write)
        time.sleep(0.05)
        
if __name__ == '__main__':
    v = TTS()
    #[h?]设置单词发音方式，0为自动判断单词发音方式，1为字母发音方式，2为单词发音方式
    #[v?]设置音量，音量范围为0-10,10为最大音量。
    #[m?]选择发音人，3为小燕（女），51为许久（男）， 52为许多（男）， 53为小萍（女）
    v.TTSModuleSpeak("[h0][v10][m3]","你好,我是超级象棋王,我要用象棋打败你")
    time.sleep(6) # 必要延时，等待播放完成
    #v.TTSModuleSpeak("[v5][m52]", "，我要用象棋打败你")
    #time.sleep(3)
    v.TTSModuleSpeak("[h2][v10][m53]", "Hello, I am Super Chinese Chess Master")