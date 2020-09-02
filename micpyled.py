import socket,machine,utime#导入gpio操作库
old_time=0
LED = machine.Pin(2, machine.Pin.OUT)#GPIO2输出模式
addr_info = socket.getaddrinfo("tcp.tlink.io",8647)
addr = addr_info[0][-1]
s = socket.socket()
s.connect(addr)#连接服务器
s.send(b'FL03VD0S65PYX1MO')#发送消息
print('connect....')
while True:
    data = s.recv(500).decode('utf8')#接收后解码，源码是字节型
    if data == '1':
        LED.value(1)
        # print('open LED')
    if data == '0':
        LED.value(0)
        # print('close')
    run_time=utime.time()
    if run_time-old_time>=50:
        s.send('[H:%d][S:2][D?3][T:d]'%run_time)#50秒就发一次心跳
        old_time=run_time
    print(data)