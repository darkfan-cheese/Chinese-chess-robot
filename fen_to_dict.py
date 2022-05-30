import requests
import json
from PIL import Image

class FenToDict:
    def __init__(self):
        self.latter_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        # return self.dictorg  # 这里返回一个值全为'0'的从a0到i9的字典

    def cal_chess(self, ax_i):
        row_value = eval(ax_i)
        # row_value = self.row_value
        tit = ax_i[-1]
        count = 0
        for i in row_value:
            if i.isdigit():
                count += eval(i)
            else:
                count += 1
                self.dictorg[self.latter_table[count - 1] + tit] = i
            # print(dictorg[latter_table[count-1]+tit])
        return self.dictorg

    def fen_to_the_dict(self, org_gen):
        self.ax_9, self.ax_8, self.ax_7, self.ax_6, self.ax_5, self.ax_4, self.ax_3, self.ax_2, self.ax_1, self.ax_0 = org_gen.split(
            '/')
        self.ax_list_key = ['ax_9', 'ax_8', 'ax_7', 'ax_6',
                            'ax_5', 'ax_4', 'ax_3', 'ax_2', 'ax_1', 'ax_0']
        self.ax_list_value = [self.ax_9, self.ax_8, self.ax_7, self.ax_6,
                              self.ax_5, self.ax_4, self.ax_3, self.ax_2, self.ax_1, self.ax_0]
        self.ax_dict = dict(zip(self.ax_list_key, self.ax_list_value))
        dict_key = []
        non = '0'
        for j in self.latter_table:
            for i in range(10):
                dict_key.append(j + str(i))
        dictvalue = [non for i in range(0, 90)]
        self.dictorg = dict(zip(dict_key, dictvalue))
        self.cal_chess('self.ax_9')
        self.cal_chess('self.ax_8')
        self.cal_chess('self.ax_7')
        self.cal_chess('self.ax_6')
        self.cal_chess('self.ax_5')
        self.cal_chess('self.ax_4')
        self.cal_chess('self.ax_3')
        self.cal_chess('self.ax_2')
        self.cal_chess('self.ax_1')
        self.cal_chess('self.ax_0')
        return self.dictorg

    def inver_list_to_fen(self, ax_i_new):
        self.stri = ''
        count = 0
        inti = 0
        count_i = []
        for i in ax_i_new:
            count += 1
            inti += 1
            if i.isdigit():
                count_i.append(i)
            else:
                count_i.append(i)
                if count_i[inti - 2].isdigit():
                    self.stri += str(count - 1)
                    self.stri += i
                else:
                    self.stri += i
                count = 0
        self.stri += str(count)
        if self.stri[-1] == '0':
            self.stri = self.stri[:-1]
        return self.stri

    def draw_board(self, diction):
        """
        绘制虚拟棋盘
        :param diction:带有棋局信息的字典
        :return: 生成qipan_new.jpg
        """
        qipan = Image.open('images/qipan.png')
        b_ju = Image.open('images/b_ju.png')
        b_ma = Image.open('images/b_ma.png')
        b_pao = Image.open('images/b_pao.png')
        b_shi = Image.open('images/b_shi.png')
        b_xiang = Image.open('images/b_xiang.png')
        b_zu = Image.open('images/b_zu.png')
        jiang = Image.open('images/jiang.png')
        r_bing = Image.open('images/r_bing.png')
        r_ju = Image.open('images/r_ju.png')
        r_ma = Image.open('images/r_ma.png')
        r_pao = Image.open('images/r_pao.png')
        r_shi = Image.open('images/r_shi.png')
        r_xiang = Image.open('images/r_xiang.png')
        shuai = Image.open('images/shuai.png')
        r_bing = r_bing.transpose(Image.ROTATE_180)
        r_ju = r_ju.transpose(Image.ROTATE_180)
        r_ma = r_ma.transpose(Image.ROTATE_180)
        r_pao = r_pao.transpose(Image.ROTATE_180)
        r_shi = r_shi.transpose(Image.ROTATE_180)
        r_xiang = r_xiang.transpose(Image.ROTATE_180)
        shuai = shuai.transpose(Image.ROTATE_180)
        a = int(shuai.size[0] / 2)
        img_dict = {'a0': (66, 956), 'a1': (66, 857), 'a2': (66, 758), 'a3': (66, 659), 'a4': (66, 561),
                    'a5': (66, 461), 'a6': (66, 363), 'a7': (66, 264), 'a8': (66, 164), 'a9': (66, 66),
                    'b0': (165, 956), 'b1': (165, 857), 'b2': (165, 758), 'b3': (165, 659), 'b4': (165, 561),
                    'b5': (165, 461), 'b6': (165, 363), 'b7': (165, 264), 'b8': (165, 164), 'b9': (165, 66),
                    'c0': (263, 956), 'c1': (263, 857), 'c2': (263, 758), 'c3': (263, 659), 'c4': (263, 561),
                    'c5': (263, 461), 'c6': (263, 363), 'c7': (263, 264), 'c8': (263, 164), 'c9': (263, 66),
                    'd0': (363, 956), 'd1': (363, 857), 'd2': (363, 758), 'd3': (363, 659), 'd4': (363, 561),
                    'd5': (363, 461), 'd6': (363, 363), 'd7': (363, 264), 'd8': (363, 164), 'd9': (363, 66),
                    'e0': (462, 956), 'e1': (462, 857), 'e2': (462, 758), 'e3': (462, 659), 'e4': (462, 561),
                    'e5': (462, 461), 'e6': (462, 363), 'e7': (462, 264), 'e8': (462, 164), 'e9': (462, 66),
                    'f0': (561, 956), 'f1': (561, 857), 'f2': (561, 758), 'f3': (561, 659), 'f4': (561, 561),
                    'f5': (561, 461), 'f6': (561, 363), 'f7': (561, 264), 'f8': (561, 164), 'f9': (561, 66),
                    'g0': (660, 956), 'g1': (660, 857), 'g2': (660, 758), 'g3': (660, 659), 'g4': (660, 561),
                    'g5': (660, 461), 'g6': (660, 363), 'g7': (660, 264), 'g8': (660, 164), 'g9': (660, 66),
                    'h0': (758, 956), 'h1': (758, 857), 'h2': (758, 758), 'h3': (758, 659), 'h4': (758, 561),
                    'h5': (758, 461), 'h6': (758, 363), 'h7': (758, 264), 'h8': (758, 164), 'h9': (758, 66),
                    'i0': (857, 956), 'i1': (857, 857), 'i2': (857, 758), 'i3': (857, 659), 'i4': (857, 561),
                    'i5': (857, 461), 'i6': (857, 363), 'i7': (857, 264), 'i8': (857, 164), 'i9': (857, 66)}
        for cod, pie in diction.items():
            if pie == '0':
                continue
            if pie == 'r':
                qipan.paste(b_ju, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'n':
                qipan.paste(b_ma, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'b':
                qipan.paste(b_xiang, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'a':
                qipan.paste(b_shi, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'k':
                qipan.paste(jiang, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'p':
                qipan.paste(b_zu, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'c':
                qipan.paste(b_pao, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))

            if pie == 'R':
                qipan.paste(r_ju, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'N':
                qipan.paste(r_ma, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'B':
                qipan.paste(r_xiang, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'A':
                qipan.paste(r_shi, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'K':
                qipan.paste(shuai, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'P':
                qipan.paste(r_bing, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
            if pie == 'C':
                qipan.paste(r_pao, (list(img_dict[cod])[0] - a, list(img_dict[cod])[1] - a))
        qipan.resize((720, 820), Image.ANTIALIAS)
        qipan.save('qipan_new.png')
        return 'qipan_new.png'

    def new_fen_generated(self, the_dict):
        ax_9_new = []
        ax_8_new = []
        ax_7_new = []
        ax_6_new = []
        ax_5_new = []
        ax_4_new = []
        ax_3_new = []
        ax_2_new = []
        ax_1_new = []
        ax_0_new = []

        for i in self.latter_table:
            ax_9_new.append(the_dict[i + '9'])
            ax_8_new.append(the_dict[i + '8'])
            ax_7_new.append(the_dict[i + '7'])
            ax_6_new.append(the_dict[i + '6'])
            ax_5_new.append(the_dict[i + '5'])
            ax_4_new.append(the_dict[i + '4'])
            ax_3_new.append(the_dict[i + '3'])
            ax_2_new.append(the_dict[i + '2'])
            ax_1_new.append(the_dict[i + '1'])
            ax_0_new.append(the_dict[i + '0'])
        self.new_fen = ''
        str9 = self.inver_list_to_fen(ax_9_new)
        str8 = self.inver_list_to_fen(ax_8_new)
        str7 = self.inver_list_to_fen(ax_7_new)
        str6 = self.inver_list_to_fen(ax_6_new)
        str5 = self.inver_list_to_fen(ax_5_new)
        str4 = self.inver_list_to_fen(ax_4_new)
        str3 = self.inver_list_to_fen(ax_3_new)
        str2 = self.inver_list_to_fen(ax_2_new)
        str1 = self.inver_list_to_fen(ax_1_new)
        str0 = self.inver_list_to_fen(ax_0_new)
        self.new_fen = str9 + '/' + str8 + '/' + str7 + '/' + str6 + '/' + str5 + '/' + str4 + '/' + str3 + '/' + str2 + '/' + str1 + '/' + str0
        return self.new_fen


if __name__ == '__main__':
    ftd = FenToDict()  # 实例化类
    # 给定fen，生成对应的字典
    dic_new = ftd.fen_to_the_dict(org_gen='2b6/9/3k5/9/2b6/4N1B2/9/1c2B4/4K4/3A5')
    print(dic_new)

    # 给定字典，生成对应的fen
    '''
    可以把字典存到一个文件夹里调用
    with open('./字典.txt','r') as rf:
        the_dict = rf.read()
    new_fen = ftd.new_fen_generated(the_dict)
    print(new_fen)
    '''
    the_dict = {'a0': '0', 'a1': '0', 'a2': '0', 'a3': '0', 'a4': '0', 'a5': '0', 'a6': '0', 'a7': '0', 'a8': '0', 'a9':
                 '0', 'b0': '0', 'b1': '0', 'b2': 'c', 'b3': '0', 'b4': '0', 'b5': '0', 'b6': '0', 'b7': '0', 'b8': '0',
                'b9': '0', 'c0': '0', 'c1': '0', 'c2': '0', 'c3': '0', 'c4': '0', 'c5': 'b', 'c6': '0', 'c7': '0',
                'c8': '0', 'c9': 'b', 'd0': 'A', 'd1': '0', 'd2': '0', 'd3': '0', 'd4': '0', 'd5': '0', 'd6': '0',
                'd7': 'k', 'd8': '0', 'd9': '0', 'e0': '0', 'e1': 'K', 'e2': 'B', 'e3': '0', 'e4': 'N', 'e5': '0',
                'e6': '0', 'e7': '0', 'e8': '0', 'e9': '0', 'f0': '0', 'f1': '0', 'f2': '0', 'f3': '0', 'f4': '0',
                'f5': '0', 'f6': '0', 'f7': '0', 'f8': '0', 'f9': '0', 'g0': '0', 'g1': '0', 'g2': '0', 'g3': '0',
                'g4': 'B', 'g5': '0', 'g6': '0', 'g7': '0', 'g8': '0', 'g9': '0', 'h0': '0', 'h1': '0', 'h2': '0',
                'h3': '0', 'h4': '0', 'h5': '0', 'h6': '0',
                'h7': '0', 'h8': '0', 'h9': '0', 'i0': '0', 'i1': '0', 'i2': '0', 'i3': '0', 'i4': '0', 'i5': '0',
                'i6': '0', 'i7': '0', 'i8': '0', 'i9': '0'}
    new_fen = ftd.new_fen_generated(the_dict)
    print(new_fen)