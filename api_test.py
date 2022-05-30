import requests
import time

def sendw(api_open, player='w'):
    api_all = "http://www.chessdb.cn/chessdb.php?action=queryall&learn=1&board="
    api_queue = "http://www.chessdb.cn/chessdb.php?action=queue&board="
    url_all = api_all + api_open + ' ' + player
    print(url_all + '\n')
    ret = requests.post(url=url_all)
    a = ret.content.decode('utf-8')  # todo:添加自动计算的过程
    print(a)
    if 'nobestmove' in a or 'unknown' in a:
        print('开始进行自动计算')
        url_queue = api_queue + api_open + ' ' + player
        print(url_queue + '\n')
        ret_queue = requests.post(url=url_queue)
        api_queue = ret_queue.content.decode('utf-8')
        print('api_queue:', api_queue)
        time.sleep(5.5)

        if 'ok' in api_queue:
            ret = requests.post(url=url_all)
            a = ret.content.decode('utf-8')
            print(a)
            if 'unknown' in a:
                print('再次计算')
                sendw(api_open, player)

    if 'search' in a:
        # b = a[7:11]
        d = a.split('|')
        c = d[-1]
        b = c[7:11]
        print(b)
    elif 'move' in a:
        print('计算成功')
        b = (a[5:9])
        print(b)
    else:
        b = a
    return b


if __name__ == '__main__':
    # sendw(api_open='1C3abn1/5k3/1c3a1c1/p3R1p1r/9/9/P3P3P/9/2R6/2BAKAB2', player='b')
    sendw(api_open='rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR')
