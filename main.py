import requests
import os

dic_class = {'a': 'genshinimpact', 'b': 'bluearchive', 'c': 'azurlane', 'd': 'honkai', 'e': 'arknights' ,'f':'','':'any'}
image_class = input("你需要生成哪类图片：\na.原神\tb.碧蓝档案\tc.碧蓝航线\td.崩坏三\te.明日方舟\tf:我自己手动输入\t不选则随机\n")
is_r18 = input("是否生成R18(y/n)：")
r18 = ""
class_path = "any"
cnt = 1000
a =''
b =''
for a, b in dic_class.items():
    if (a == image_class):
        class_path = b
        if(class_path==''):
            class_path = input("请输入你想要抓取的关键词：")
        break
if is_r18 == 'y':
    r18 = "r18=1"
else:
    pass
r18_path = r18[:3]
url = f'https://image.anosu.top/pixiv/direct?{r18}&keyword={class_path}' if class_path != 'any' else f'https://image.anosu.top/pixiv/direct?{r18}'
head = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 Edg/122.0.0.0'}
m = 1
if not os.path.exists(f"./{r18_path}image"):
    os.mkdir(f"./{r18_path}image")
if not os.path.exists(f"./{r18_path}image/{class_path}"):
    os.mkdir(f"./{r18_path}image/{class_path}")
for file in os.listdir(f"./{r18_path}image/{class_path}"):
    if os.path.isfile(f"./{r18_path}image/{class_path}/{file}"):
        m += 1

print(f"正在抓取关键词为{class_path}的",end='')
print("r18图片"if is_r18=='y' else "普通图片")
for i in range(m, m + cnt):
    rqs = requests.get(url, headers=head)
    name = rqs.url.split("/")[-1]
    print(f"是否请求成功:{rqs.ok}\t")
    if(rqs.ok!=True):
        continue
    # print('状态码：{rqs.status_code}\n')
    # print(f"请求头:{rqs.headers}\n")
    if(f"没有与{class_path}相关的图片" in rqs.text):
        print(f"没有与{class_path}相关的图片，请更换关键词重试")
        break
    with open(f"./{r18_path}image/{class_path}/{name}", "wb") as file:
        file.write(rqs.content)
    print(f"已下载第{i}/{m + cnt}个:{name}\n")
    # print(f"网页文字:{rqs.text}\n")
