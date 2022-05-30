
class qipan():
    def __init__(self):
        with open('./armdict.txt', 'r') as rf:
            arm_txt = rf.read()
            armdict = eval(arm_txt)
        with open('./chessdict.txt', 'r') as ch:
            chess_txt = ch.read()
            chessdict = eval(chess_txt)
        self.qp = {'a0': [chessdict['a0'], armdict['a0']], 'a1': [chessdict['a1'], armdict['a1']], 'a2': [chessdict['a2'], armdict['a2']], 'a3': [chessdict['a3'], armdict['a3']], 'a4': [chessdict['a4'], armdict['a4']],
                   'a5': [chessdict['a5'], armdict['a5']], 'a6': [chessdict['a6'], armdict['a6']], 'a7': [chessdict['a7'], armdict['a7']], 'a8': [chessdict['a8'], armdict['a8']], 'a9': [chessdict['a9'], armdict['a9']],
                   'b0': [chessdict['b0'], armdict['b0']], 'b1': [chessdict['b1'], armdict['b1']], 'b2': [chessdict['b2'], armdict['b2']], 'b3': [chessdict['b3'], armdict['b3']], 'b4': [chessdict['b4'], armdict['b4']],
                   'b5': [chessdict['b5'], armdict['b5']], 'b6': [chessdict['b6'], armdict['b6']], 'b7': [chessdict['b7'], armdict['b7']], 'b8': [chessdict['b8'], armdict['b8']], 'b9': [chessdict['b9'], armdict['b9']],
                   'c0': [chessdict['c0'], armdict['c0']], 'c1': [chessdict['c1'], armdict['c1']], 'c2': [chessdict['c2'], armdict['c2']], 'c3': [chessdict['c3'], armdict['c3']], 'c4': [chessdict['c4'], armdict['c4']],
                   'c5': [chessdict['c5'], armdict['c5']], 'c6': [chessdict['c6'], armdict['c6']], 'c7': [chessdict['c7'], armdict['c7']], 'c8': [chessdict['c8'], armdict['c8']], 'c9': [chessdict['c9'], armdict['c9']],
                   'd0': [chessdict['d0'], armdict['d0']], 'd1': [chessdict['d1'], armdict['d1']], 'd2': [chessdict['d2'], armdict['d2']], 'd3': [chessdict['d3'], armdict['d3']], 'd4': [chessdict['d4'], armdict['d4']],
                   'd5': [chessdict['d5'], armdict['d5']], 'd6': [chessdict['d6'], armdict['d6']], 'd7': [chessdict['d7'], armdict['d7']], 'd8': [chessdict['d8'], armdict['d8']], 'd9': [chessdict['d9'], armdict['d9']],
                   'e0': [chessdict['e0'], armdict['e0']], 'e1': [chessdict['e1'], armdict['e1']], 'e2': [chessdict['e2'], armdict['e2']], 'e3': [chessdict['e3'], armdict['e3']], 'e4': [chessdict['e4'], armdict['e4']],
                   'e5': [chessdict['e5'], armdict['e5']], 'e6': [chessdict['e6'], armdict['e6']], 'e7': [chessdict['e7'], armdict['e7']], 'e8': [chessdict['e8'], armdict['e8']], 'e9': [chessdict['e9'], armdict['e9']],
                   'f0': [chessdict['f0'], armdict['f0']], 'f1': [chessdict['f1'], armdict['f1']], 'f2': [chessdict['f2'], armdict['f2']], 'f3': [chessdict['f3'], armdict['f3']], 'f4': [chessdict['f4'], armdict['f4']],
                   'f5': [chessdict['f5'], armdict['f5']], 'f6': [chessdict['f6'], armdict['f6']], 'f7': [chessdict['f7'], armdict['f7']], 'f8': [chessdict['f8'], armdict['f8']], 'f9': [chessdict['f9'], armdict['f9']],
                   'g0': [chessdict['g0'], armdict['g0']], 'g1': [chessdict['g1'], armdict['g1']], 'g2': [chessdict['g2'], armdict['g2']], 'g3': [chessdict['g3'], armdict['g3']], 'g4': [chessdict['g4'], armdict['g4']],
                   'g5': [chessdict['g5'], armdict['g5']], 'g6': [chessdict['g6'], armdict['g6']], 'g7': [chessdict['g7'], armdict['g7']], 'g8': [chessdict['g8'], armdict['g8']], 'g9': [chessdict['g9'], armdict['g9']],
                   'h0': [chessdict['h0'], armdict['h0']], 'h1': [chessdict['h1'], armdict['h1']], 'h2': [chessdict['h2'], armdict['h2']], 'h3': [chessdict['h3'], armdict['h3']], 'h4': [chessdict['h4'], armdict['h4']],
                   'h5': [chessdict['h5'], armdict['h5']], 'h6': [chessdict['h6'], armdict['h6']], 'h7': [chessdict['h7'], armdict['h7']], 'h8': [chessdict['h8'], armdict['h8']], 'h9': [chessdict['h9'], armdict['h9']],
                   'i0': [chessdict['i0'], armdict['i0']], 'i1': [chessdict['i1'], armdict['i1']], 'i2': [chessdict['i2'], armdict['i2']], 'i3': [chessdict['i3'], armdict['i3']], 'i4': [chessdict['i4'], armdict['i4']],
                   'i5': [chessdict['i5'], armdict['i5']], 'i6': [chessdict['i6'], armdict['i6']], 'i7': [chessdict['i7'], armdict['i7']], 'i8': [chessdict['i8'], armdict['i8']], 'i9': [chessdict['i9'], armdict['i9']]}
        self.qpd = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                    'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                    'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                    'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                    'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                    'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                    'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                    'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                    'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']
        self.qpdic = ['0']*90  # 棋盘字典

    def gbdic(self, i, cla):
        self.qpdic[i] = cla

    def yolo2qp(self, centerx, centery, cla):  #将识别结果转为棋盘上的点，并更新棋盘字典
        for i in range(90):
            k = self.qpd[i]
            x = self.qp[k][0][0]
            y = self.qp[k][0][1]
            dlt = (centerx-x)*(centerx-x)+(centery-y)*(centery-y)
            if dlt<400:
                self.gbdic(i, cla)
                break
