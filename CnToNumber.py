numberDic = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5', '六': '6', '七': '7', '八': '8', '九': '9','两': '2','壹':'1','贰':'2','叁':'3','肆':'4','伍':'5','陆':'6','柒':'7','捌':'8','玖':'9','拾':'0'}
bitDic = {'十': '0', '百': '00', '千': '000', '万': '0000', '亿': '00000000'}


def cn2num(cnnumb):
    numstr = ''
    del_num = 0
    wanstr = ''
    for index,chr in enumerate(cnnumb):
        numkeys = numberDic.keys()
        bitkeys = bitDic.keys()
        if chr in numkeys:
            numstr += numberDic[chr]
        elif chr in bitkeys:
            numstr += bitDic[chr]
            if chr == '万' and wanstr != '':
                sp = wanstr.split('.')
                if sp[0].isdigit():
                    sum = int(sp[0])*10000
                    if len(sp) == 2:
                        for index,spp in enumerate(sp[1]):
                            sum+=int(spp)*pow(10,3-index)
                    return cnnumb[del_num:len(cnnumb)],str(sum)
        else:
            if chr.isdigit() or chr == '.':
                wanstr += str(chr)
            else:
                return cn2num(cnnumb[index+1:len(cnnumb)])
                del_num += 1
    return cnnumb[del_num:len(cnnumb)],str(str2number(numstr))

def str2number(numstr):
    numlist = list(numstr)
    numlist.reverse()
    sum = 0
    index_sum = 0#标记相乘10的位数
    index_num = 1#标记非0数字
    bit_flag = 1 #1.表示万以内，2表示万以上亿以内，3.亿以上
    for index,chr in enumerate(numlist):
        chrint = int(chr)
        if chrint > 0:
            sum_len = len(str(sum))
            if bit_flag == 2 and index_sum<8:
                index_sum = sum_len
            if bit_flag ==3:
                index_sum = sum_len
            index_num = chrint
            sum += index_num * pow(10,(index_sum))
            sum_len = len(str(sum))
            if sum_len >= 5 and sum_len <9:
                bit_flag = 2
            elif sum_len >= 9:
                bit_flag = 3
            index_sum = 0
        else:
            index_sum += 1
            if index == len(numlist)-1:#解决 十一万五百二十 这种情况
                sum += 1 * pow(10, (index_sum+len(str(sum))-1))

    return sum
