#!/usr/bin/env python3
import random,time,os
version = "v0.0.6"
t6,t5,t4,t3,lp,hp = 0,0,0,0,0,0
cur_path = os.getcwd()
pool = f"{cur_path}/PrizePool"
Counts = open(f"{pool}/Counts.txt").read().split(",")
x3, x4, x5, x6 = {}, {}, {}, {}
spx5 = []
spx6 = []

def check_special(in_list, star):
	for i in in_list:
		if i.startswith("*"):
			if star == 5:
				spx5.append(i+"*")
			else:
				spx6.append(i+"*")

def zip_to_dict(in_list, star):
	idx = star-3
	
	return dict(zip(list(range(1, int(Counts[idx])+1)), in_list))

def read_prize_pool(path):
	if os.path.exists(pool):
		results = []
		
		s3 = open(f"{pool}/3Stars.txt","r").read().split(",")
		s4 = open(f"{pool}/4Stars.txt","r").read().split(",")
		s5 = open(f"{pool}/5Stars.txt","r").read().split(",")
		s6 = open(f"{pool}/6Stars.txt","r").read().split(",")
		
		check_special(s5, 5)
		check_special(s6, 6)
		
		set_of_str = [s3, s4, s5, s6]
		
		for x in range(3, 7):	
			for i in set_of_str:
				results.append(zip_to_dict(i, x))
				
		return results[:4]
	else:
		x6 = {1:"艾雅法拉",2:"安洁莉娜",3:"银灰",4:"陈"}
		x5 = {1:"白面鸮",2:"德克萨斯",3:"白金",4:"可颂",5:"狮蝎",6:"诗怀雅"}
		x4 = {1:"夜烟",2:"远山",3:"杰西卡",4:"流星",5:"白雪",6:"清道夫",7:"红豆",8:"杜宾",9:"缠丸",10:"霜叶",11:"慕斯",12:"砾",13:"暗索",14:"末药",15:"调香师",16:"角峰",17:"蛇屠箱",18:"古米",19:"深海色",20:"地灵",21:"阿消",22:"猎蜂",23:"格雷伊",24:"苏苏洛",25:"桃金娘",26:"红云",27:"安比尔"}
		x3 = {1:"芬",2:"香草",3:"翔羽",4:"玫兰莎",5:"卡提",6:"米格鲁",7:"克洛丝",8:"炎熔",9:"芙蓉",10:"安赛尔",11:"史都华德",12:"梓兰",13:"空爆",14:"月见夜",15:"斑点",16:"泡普卡",17:"安德切尔"}
		
chara = read_prize_pool(cur_path)
x3, x4, x5, x6 = chara[0], chara[1], chara[2], chara[3]

print("卡池概率提升六星:{}\n卡池概率提升五星:{}".format(", ".join(spx6),",".join(spx5)))

try:
	while True:
		hcy = int(input("请输入合成玉数量(最大60000,最小600(600合成玉抽卡一次)):"))
		if hcy > 60000 or hcy < 600:
			pass
		else:
			break
except:
	print("""合成玉貌似并不是一个合法的数字
与神经网络丢失连接,请重试""")
	hcy = 0
	
star = random.randint(1,101)
for x in range(hcy // 600):
	random_x4 = random.randint(1,len(x4.keys()))
	random_x3 = random.randint(1,len(x3.keys()))
	star = random.randint(1,100)
	if spx5 != []:
		if random.randint(1,101) <= 70:
			get_up_x5 = True
		else:
			get_up_x5 = False
			random_x5 = random.randint(1,len(x5.keys()))
		
	if spx6 != []:
		if random.randint(1,101) <= 70:
			get_up_x6 = True
		else:
			get_up_x6 = False
			random_x6 = random.randint(1,len(x5.keys()))
	
	if star >= 1 and star <= 2:
		t6 += 1
		hp += 15
		if get_up_x6:
			print(f"""
				******   {random.sample(spx6, 1)[0]}
				""")
		else:
			print(f"""
				******   {x6[random_x6]}
				""")
		time.sleep(0.5)
		
	elif star >= 3 and star <= 9:
		t5 += 1
		hp += 8
		if get_up_x5:
			print(f"""
				*****   {random.sample(spx5, 1)[0]}
				""")
		else:
			print(f"""
				*****   {x6[random_x5]}
				""")
		time.sleep(0.5)
		
	elif star >= 10 and star <= 61:
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