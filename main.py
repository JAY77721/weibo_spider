from weiboSpide import*
import csv


def save_to_csv(data,filename = 'output/weibo_data.csv'):
    #将微博数据存储到csv文件中
    with open(filename,'a',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['id','text','attitudes', 'comments', 'reposts'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    since_id = 5070626380058958
    all_weibos = []
    for page in range(1,11):
        print(f'正在爬取第 {page} 页...')
        json = get_page(since_id)
        # print(json)
        # break
        since_id = json.get('data').get('cardlistInfo').get('since_id')
        result = parse_page(json)
        weibos = list(result)
        all_weibos.extend(weibos)
        for weibo in weibos:
            print(weibo)
            break
            # idex = 0
            # print(f'爬出第{idex}个微博成功')
            # idex +=1
    save_to_csv(all_weibos)
    print("爬取完成，数据已保存到 output/weibo_data.csv")