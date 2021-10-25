import pandas as pd

df = pd.read_csv('Data.csv')

sequences = df['Promoter sequence'].values

def pre(sequences):
    list_all = []
    for sequence in sequences:
        # 用all_pre 这一字典来存放{位置：pre特性},因为一个键不能对应多个值
        all_pre = {}
        # 未突变，两方向pre_________________________________________________________________________________________
        preR = sequence.find('tgaaac')
        while preR != -1:
            all_pre.update({preR: 'tgaaac'})
            preR = sequence.find('tgaaac', preR + 1)

        preL = sequence.find('gtttca')
        while preL != -1:
            all_pre.update({preL: 'gtttca'})
            preL = sequence.find('gtttca', preL + 1)

        # 1位突变，3种，左右________________________________________________________________________________________
        preM11R = sequence.find('agaaac')
        while preM11R != -1:
            all_pre.update({preM11R: 'agaaac'})
            preM11R = sequence.find('agaaac', preM11R + 1)

        preM13R = sequence.find('cgaaac')
        while preM13R != -1:
            all_pre.update({preM13R: 'cgaaac'})
            preM13R = sequence.find('cgaaac', preM13R + 1)

        preM14R = sequence.find('ggaaac')
        while preM14R != -1:
            all_pre.update({preM14R: 'ggaaac'})
            preM14R = sequence.find('ggaaac', preM14R + 1)

        preM11L = sequence.find('gtttct')
        while preM11L != -1:
            all_pre.update({preM11L: 'gtttct'})
            preM11L = sequence.find('gtttct', preM11L + 1)

        preM13L = sequence.find('gtttcg')
        while preM13L != -1:
            all_pre.update({preM13L: 'gtttcg'})
            preM13L = sequence.find('gtttcc', preM13L + 1)

        preM14L = sequence.find('gtttcc')
        while preM14L != -1:
            all_pre.update({preM14L: 'gtttcc'})
            preM14L = sequence.find('gtttcc', preM14L + 1)

        # 2位突变，3种，左右________________________________________________________________________________________
        preM21R = sequence.find('taaaac')
        while preM21R != -1:
            all_pre.update({preM21R: 'taaaac'})
            preM21R = sequence.find('taaaac', preM21R + 1)

        preM22R = sequence.find('ttaaac')
        while preM22R != -1:
            all_pre.update({preM22R: 'ttaaac'})
            preM22R = sequence.find('ttaaac', preM22R + 1)

        preM23R = sequence.find('tcaaac')
        while preM23R != -1:
            all_pre.update({preM23R: 'tcaaac'})
            preM23R = sequence.find('tcaaac', preM23R + 1)

        preM21L = sequence.find('gtttta')
        while preM21L != -1:
            all_pre.update({preM21L: 'gtttta'})
            preM21L = sequence.find('gtttta', preM21L + 1)

        preM22L = sequence.find('gtttaa')
        while preM22L != -1:
            all_pre.update({preM22L: 'gtttaa'})
            preM22L = sequence.find('gtttaa', preM22L + 1)

        preM23L = sequence.find('gtttga')
        while preM23L != -1:
            all_pre.update({preM23L: 'gtttga'})
            preM23L = sequence.find('gtttga', preM23L + 1)

        # 3位突变，3种，左右________________________________________________________________________________________
        preM32R = sequence.find('tgtaac')
        while preM32R != -1:
            all_pre.update({preM32R: 'tgtaac'})
            preM32R = sequence.find('tgtaac', preM32R + 1)

        preM33R = sequence.find('tgcaac')
        while preM33R != -1:
            all_pre.update({preM33R: 'tgcaac'})
            preM33R = sequence.find('tgcaac', preM33R + 1)

        preM34R = sequence.find('tggaac')
        while preM34R != -1:
            all_pre.update({preM34R: 'tggaac'})
            preM34R = sequence.find('tggaac', preM34R + 1)

        preM32L = sequence.find('gttaca')
        while preM32L != -1:
            all_pre.update({preM32L: 'gttaca'})
            preM32L = sequence.find('gttaca', preM32L + 1)

        preM33L = sequence.find('gttgca')
        while preM33L != -1:
            all_pre.update({preM33L: 'gttgca'})
            preM33L = sequence.find('gttgca', preM33L + 1)

        preM34L = sequence.find('gttcca')
        while preM34L != -1:
            all_pre.update({preM34L: 'gttcca'})
            preM34L = sequence.find('gttcca', preM34L + 1)

        # 4位突变，3种，左右________________________________________________________________________________________
        preM42R = sequence.find('tgatac')
        while preM42R != -1:
            all_pre.update({preM42R: 'tgatac'})
            preM42R = sequence.find('tgatac', preM42R + 1)

        preM43R = sequence.find('tgacac')
        while preM43R != -1:
            all_pre.update({preM43R: 'tgacac'})
            preM43R = sequence.find('tgacac', preM43R + 1)

        preM44R = sequence.find('tgagac')
        while preM44R != -1:
            all_pre.update({preM44R: 'tgagac'})
            preM44R = sequence.find('tgagac', preM44R + 1)

        preM42L = sequence.find('gtatca')
        while preM42L != -1:
            all_pre.update({preM42L: 'gtatca'})
            preM42L = sequence.find('gtatca', preM42L + 1)

        preM43L = sequence.find('gtgtca')
        while preM43L != -1:
            all_pre.update({preM43L: 'gtgtca'})
            preM43L = sequence.find('gtgtca', preM43L + 1)

        preM44L = sequence.find('gtctca')
        while preM44L != -1:
            all_pre.update({preM44L: 'gtctca'})
            preM44L = sequence.find('gtctca', preM44L + 1)

        # 5位突变，3种，左右________________________________________________________________________________________
        preM52R = sequence.find('tgaatc')
        while preM52R != -1:
            all_pre.update({preM52R: 'tgaatc'})
            preM52R = sequence.find('tgaatc', preM52R + 1)

        preM53R = sequence.find('tgaacc')
        while preM53R != -1:
            all_pre.update({preM53R: 'tgaacc'})
            preM53R = sequence.find('tgaacc', preM53R + 1)

        preM54R = sequence.find('tgaagc')
        while preM54R != -1:
            all_pre.update({preM54R: 'tgaagc'})
            preM54R = sequence.find('tgaagc', preM54R + 1)

        preM52L = sequence.find('gattca')
        while preM52L != -1:
            all_pre.update({preM52L: 'gattca'})
            preM52L = sequence.find('gattca', preM52L + 1)

        preM53L = sequence.find('ggttca')
        while preM53L != -1:
            all_pre.update({preM53L: 'ggttca'})
            preM53L = sequence.find('ggttca', preM53L + 1)

        preM54L = sequence.find('gcttca')
        while preM54L != -1:
            all_pre.update({preM54L: 'gcttca'})
            preM54L = sequence.find('gcttca', preM54L + 1)

        # 6位突变，3种，左右________________________________________________________________________________________
        preM61R = sequence.find('tgaaaa')
        while preM61R != -1:
            all_pre.update({preM61R: 'tgaaaa'})
            preM61R = sequence.find('tgaaaa', preM61R + 1)

        preM62R = sequence.find('tgaaat')
        while preM62R != -1:
            all_pre.update({preM62R: 'tgaaat'})
            preM62R = sequence.find('tgaaat', preM62R + 1)

        preM64R = sequence.find('tgaaag')
        while preM64R != -1:
            all_pre.update({preM64R: 'tgaaag'})
            preM64R = sequence.find('tgaaag', preM64R + 1)

        preM61L = sequence.find('ttttca')
        while preM61L != -1:
            all_pre.update({preM61L: 'ttttca'})
            preM61L = sequence.find('ttttca', preM61L + 1)

        preM62L = sequence.find('atttca')
        while preM62L != -1:
            all_pre.update({preM62L: 'atttca'})
            preM62L = sequence.find('atttca', preM62L + 1)

        preM64L = sequence.find('ctttca')
        while preM64L != -1:
            all_pre.update({preM64L: 'ctttca'})
            preM64L = sequence.find('ctttca', preM64L + 1)

        list_all.append(all_pre)
    return list_all

def str_append(s, n):
    output = ''
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output

def mute(list_all):
    newdata = []
    for m, o in enumerate(sequences):
        temp_seq = str_append('0', len(o))
        for l, all_pre in enumerate(list_all):
            if m == l:
                for item in all_pre.items():
                    if item[1] in o:
                        temp = temp_seq[:item[0]] + item[1] + temp_seq[item[0] + len(item[1]):]
                        temp_seq = temp
        newdata.append(temp)
    return newdata

if __name__ == '__main__':
    main()
