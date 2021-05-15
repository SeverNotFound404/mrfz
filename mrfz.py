import random,time
version = "v0.0.6"
t6,t5,t4,t3,lp,hp = 0,0,0,0,0,0
x6 = {1:"艾雅法拉",2:"安洁莉娜",3:"银灰",4:"陈"}
x5 = {1:"白面鸮",2:"德克萨斯",3:"白金",4:"可颂",5:"狮蝎",6:"诗怀雅"}
x4 = {1:"夜烟",2:"远山",3:"杰西卡",4:"流星",5:"白雪",6:"清道夫",7:"红豆",8:"杜宾",9:"缠丸",10:"霜叶",11:"慕斯",12:"砾",13:"暗索",14:"末药",15:"调香师",16:"角峰",17:"蛇屠箱",18:"古米",19:"深海色",20:"地灵",21:"阿消",22:"猎蜂",23:"格雷伊",24:"苏苏洛",25:"桃金娘",26:"红云"}
x3 = {1:"芬",2:"香草",3:"翔羽",4:"玫兰莎",5:"卡提",6:"米格鲁",7:"克洛丝",8:"炎熔",9:"芙蓉",10:"安赛尔",11:"史都华德",12:"梓兰",13:"空爆",14:"月见夜",15:"斑点",16:"泡普卡"}
print("正在与神经网络连接,请稍等……")
time.sleep(random.randint(5,10))
try:
    while True:
        hcy = int(input("请输入合成玉数量(最大6000,最小600(600合成玉抽卡一次)):"))
        if hcy > 6000 or hcy < 600:
            pass
        else:
            break
except:
    print("""合成玉貌似并不是一个合法的数字
与神经网络丢失连接,请重试""")
    hcy = 0
star = random.randint(1,100)
for x in range(hcy // 600):
    random_x6 = random.randint(1,4)
    random_x5 = random.randint(1,6)
    random_x4 = random.randint(1,26)
    random_x3 = random.randint(1,16)
    star = random.randint(1,100)
    if star >= 1 and star <= 2:
        t6 += 1
        hp += 15
        print(f"""
                ******   {x6[random_x6]}
            """)
        time.sleep(0.5)
    elif star >= 3 and star <= 8:
        t5 += 1
        hp += 8
        print(f"""
                *****   {x5[random_x5]}
            """)
        time.sleep(0.5)
    elif star >= 9 and star <= 50:
        t4 += 1
        lp += 30
        print(f"""
                ****   {x4[random_x4]}
            """)
        time.sleep(0.5)
    else:
        t3 += 1
        lp += 3
        print(f"""
                ***   {x3[random_x3]}
            """)
        time.sleep(0.5)
if hcy > 0:
    print(f"抽卡次数{hcy//600}次,六星数量{t6}个,五星数量{t5}个,四星数量{t4}个,三星数量{t3}个")
    print(f"获得了资质凭证{lp}个,高级凭证{hp}个(按照第7次后获得相同干员计算)")
    print(f"version:{version}")