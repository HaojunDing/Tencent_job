'''
任务目标:
    1, 通过关键字 抓取腾讯社会招聘招聘信息
    2, 用户自定义爬取前几页
    3, 建立相应关键字的数据库
'''

import requests as s
from lxml import etree
from urllib import parse
from Mysql_tx import Mysql_conn

m = Mysql_conn()


base_url = 'https://hr.tencent.com/position.php?{kw}&tid=0&lid=2156&start={page}'


def run(kw, pag):
    for page in range(pag):
        page = page * 10
        print(page)
        kwe = {
            'keywords': kw
        }
        kwe = parse.urlencode(kwe).encode('utf-8').decode('utf-8')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }
        url = base_url.format(kw=kwe, page=page)
        print(url)
        html = s.get(url, headers=headers).text

        html_ele = etree.HTML(html)
        tr_list = html_ele.xpath('//table[@class="tablelist"]')[0]

        for tr_ele in tr_list[1:-1]:
            tetle = tr_ele.xpath('./td[1]/a')[0].text
            clas = tr_ele.xpath('./td[2]')[0].text
            num = tr_ele.xpath('./td[3]')[0].text
            site = tr_ele.xpath('./td[4]')[0].text
            rtime = tr_ele.xpath('./td[5]')[0].text
            link = tr_ele.xpath('./td[1]/a/@href')
            print(tetle)
            sql = 'insert into tencent (tetle, clas, num, site, rtime, link)VALUES (%s, %s, %s, %s, %s, %s)'
            data = tetle, clas, num, site, rtime, link
            m.ins(sql, data)


if __name__ == '__main__':
    kw = input('请输入要获取的职位: ')
    page = int(input('请输入要爬取得页数: '))
    run(kw, page)



