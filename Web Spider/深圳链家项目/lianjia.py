import re
import requests
import pymysql
import time
import random
import traceback

class Db:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            port=3306,
            db='lianjia_db',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """创建数据表"""
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS lianjia (
            id INT AUTO_INCREMENT PRIMARY KEY,
            housename VARCHAR(255),
            community_name VARCHAR(255),
            address VARCHAR(255),
            house_type VARCHAR(100),
            area VARCHAR(100),
            floor VARCHAR(100),
            total_price VARCHAR(50),
            unit_price VARCHAR(50),
            agent VARCHAR(100),
            agent_phone VARCHAR(50)
        )
        '''
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert(self, house_info):
        print(house_info)
        """插入房源信息"""
        insert_sql = '''
        INSERT INTO lianjia 
        (housename, community_name, address, house_type, area, floor, total_price, unit_price, agent, agent_phone) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        try:
            self.cursor.execute(insert_sql, (
                house_info['housename'],
                house_info['community_name'], 
                house_info['address'],
                house_info['house_type'],
                house_info['area'],
                house_info['floor'],
                house_info['total_price'],
                house_info['unit_price'],
                house_info['agent'],
                house_info['agent_phone']
            ))
            self.conn.commit()
        except Exception as e:
            print(f"保存数据出错: {e}")
            self.conn.rollback()

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.conn.close()


class Sprawl():
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'lianjia_uuid=f6937e58-f1ee-4753-9138-372a9a621262; _jzqx=1.1730474356.1730474356.1.jzqsr=hip%2Elianjia%2Ecom|jzqct=/.-; _ga=GA1.2.883460143.1730474368; select_city=440300; lianjia_ssid=01b040d5-14a8-4544-bb55-6bc9176c7055; _jzqa=1.338853242103942500.1730474356.1730474356.1733806364.2; _jzqc=1; _jzqckmp=1; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1733806364; HMACCOUNT=F7AC57B969505D56; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192e84f2fad1869-0e9c81a11c7ba8-26011951-3686400-192e84f2fae12f9%22%2C%22%24device_id%22%3A%22192e84f2fad1869-0e9c81a11c7ba8-26011951-3686400-192e84f2fae12f9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.682220605.1733806382; crosSdkDT2019DeviceId=40f40z-sbyxd0-nehomwiqfmyugeb-l1smu0rax; login_ucid=2000000458356068; lianjia_token=2.0010b050e84778c860011d79d9a21b7f2e; lianjia_token_secure=2.0010b050e84778c860011d79d9a21b7f2e; security_ticket=dbwdgVTWgco6gK8pLqOhaI9h/zD9RY8uHzIAS8e1lik2cQWF8iGCrTYpB2hIa/PMEDPOqGMpSxBue2qOv5WY3BYAT0cZIG22lwXoy6JvYLAftwxiqo3e4neMS11Lc7tPWckw/dUz96ecrSyY4XpuThx9IpcZixxnumA9ALx+9QQ=; ftkrc_=89adf78f-b094-4ad8-bcff-7637a34627a0; lfrc_=79ecdbe0-f7e5-4f75-aff2-69a7c49b824b; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1733807132; _qzja=1.1155604136.1730474356407.1730474356407.1733806364369.1733807058699.1733807131599.0.0.0.14.2; _qzjb=1.1733806364369.7.0.0.0; _qzjto=7.1.0; _jzqb=1.7.10.1733806364.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNzNjZDFjOTdhNDc0MmMzOGFjNjVkZGM0OWQ1YjYwNzQ1NWMyNDNkYjQ3YzY0YmFiMzRhMTIwMzIzMDJjMzFkZjhiYWRkNTU1NmViZGU0NTM4MDM5OGZlMDE2OWJiMDgzNjViN2QwODQ2M2Q5NTk1NzRmNjMwYjJkYTc5ZmFlMDI2ZTY0YTBiMjUwZmM5MzllOWM5NWIxYzcxZjViZjdiMWFlODM5NGNhZTg5YjliM2IyMGNmMDgxY2RjYTY0OWIyZTU1OWQxNzYzNjlmY2E2MDNmNDY1NmQ3OGE5MzkzM2M1NTlmNWEwZWY0YThhODVlMjhmOWU2M2I3NzQyYjFiZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0OTI1OGRjZVwifSIsInIiOiJodHRwczovL3N6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_C4R21H79WC=GS1.2.1733806382.2.1.1733807142.0.0.0',
            'Referer': 'https://sz.lianjia.com/ershoufang/pg99/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.cookies = {
          "select_city": "440300",
          "lianjia_ssid": "5d2aea05-eb61-45c4-a4a8-1c3edc70fd69",
          "lianjia_uuid": "c26030d9-1af2-4dec-8cfd-67ac625929fb",
          "Hm_lvt_46bf127ac9b856df503ec2dbf942b67e": "1734568183",
          "HMACCOUNT": "22EB0B5DDFC5B5A2",
          "_jzqa": "1.41198947634201490.1734568183.1734568183.1734568183.1",
          "_jzqc": "1",
          "_jzqckmp": "1",
          "_qzjc": "1",
          "sajssdk_2015_cross_new_user": "1",
          "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22193dc5205cecc3-0c2672af241571-26001151-2073600-193dc5205cf1693%22%2C%22%24device_id%22%3A%22193dc5205cecc3-0c2672af241571-26001151-2073600-193dc5205cf1693%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
          "_ga": "GA1.2.1825200729.1734568194",
          "_gid": "GA1.2.298329925.1734568194",
          "hip": "f2cp8ES3RwcYsR7xrz6GmGmiWB9ueh17KYuXUn8UKrcjwN-JvNFcGE98707WjNg8u50oUB-p3nEfnCd2n85HVRNEdi_0SdWkp8cMGXf_tlKLxiYHQ4JvFla_b7dTjOWTlKfko9WZParjdMphCE2TLhwoKxdki7sEgG55w2iowkQIFI-G_dF8aKqbTw%3D%3D",
          "login_ucid": "2000000458629033",
          "lianjia_token": "2.0015449bd642b1e99304e9b2e700a108aa",
          "lianjia_token_secure": "2.0015449bd642b1e99304e9b2e700a108aa",
          "security_ticket": "VU5/Qp4PUPN7ENzh8qast46hqnBXPkFilvGAIY1F8hndHXhGZp2xbaRzLMaVg/DYZXLGypBd2Cj1EO0tHm7IMdazE94VqYZCibX32s4twJCufBmu7SIuFtl3Q3dwRWxINX2gPhL/zr4HVbG/92NjY/lg0EPhalWuLA4+o1vN3Ns=",
          "ftkrc_": "4a80eda3-5cf6-45b2-bf50-05a7a65977dc",
          "lfrc_": "9934a43d-e5ad-46af-89f1-0263be1534b0",
          "_ga_C4R21H79WC": "GS1.2.1734568194.1.1.1734568493.0.0.0",
          "Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e": "1734568500",
          "srcid": "eyJ0Ijoie1wiZGF0YVwiOlwiOGQ3ZWNlODY4YzMwZjJmNDVlNWEyNjdjMjA2Y2U4OGIxMWNiYWI5ZDNmY2Q5ZmI2YzliNjQyNWQ3ZjA4ZjI1NzNlZjJiZjI4NmMwN2MwMzRmMjZlNGEyY2E5MTY1MmVhNjczY2VkNzU5YWVkMmMyMjUxNWI5MTA2NTg0YTVhNDhlMTAzNjQ1MDQxNWVmMTU5ZTc3ZDQyODgzYWU0M2RjMmQyNTkyN2EyNGQ1YTE4ODgyMDUzN2IzOTA2MDJlNzE5NzU0NjNmOTNiNzdmYmYxYmUyYzAyODRiMmI0MzVhNjM1NjQwZDlhMDY3ZDJiZTBmMzA1NTVkY2Y3OTJlZmIyZVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0M2MwMDI4OVwifSIsInIiOiJodHRwczovL3N6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=",
          "_qzja": "1.944823674.1734568183237.1734568183237.1734568183237.1734568500900.1734568500952.0.0.0.11.1",
          "_qzjb": "1.1734568183237.11.0.0.0",
          "_qzjto": "11.1.0",
          "_jzqb": "1.11.10.1734568183.1"
        }

    def get_html(self, url):
        """获取网页HTML"""
        try:
            response = requests.get(url, headers=self.headers,cookies=self.cookies)
            response.encoding = response.apparent_encoding
            return response.text
        except Exception as e:
            print(f"获取网页出错: {e}")
            print("错误详细信息:")
            # 打印错误详细信息
            print(traceback.format_exc())
            return None

    def get_page_urls(self, base_url):
        """获取所有分页URL"""
        all_page_urls = [base_url + 'pg' + str(page_url) for page_url in range(2,101)]
        # 将起始页链接（base_url）添加到最前面，组成完整的包含所有分页URL的列表
        all_page_urls = [base_url] + all_page_urls
        return all_page_urls
    

    def get_house_list(self, html):
        """获取房源详情链接"""
        return re.findall(r'<a class="noresultRecommend img LOGCLICKDATA" href="(.*?)"', html,re.S)

    def get_house_info(self, html):
        """解析单个房源详情"""
        house_info = {
            'housename': re.findall(r'<h1 class="main".*?>(.*?)</h1>', html, re.S) if re.findall(r'<h1 class="main".*?>(.*?)</h1>', html, re.S) else ['未知房名'],
            'community_name': re.findall(r'<div class="communityName">.*?<a.*?>(.*?)</a>', html, re.S) if re.findall(r'<div class="communityName">.*?<a.*?>(.*?)</a>', html, re.S) else ['未知小区'],
            'address': [' '.join(x) for x in re.findall(r'<span class="info">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', html, re.S)] if re.findall(r'<span class="info">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', html, re.S) else ['未知区域'],
            'house_type': re.findall(r'<div class="room">.*?<div class="mainInfo">(.*?)</div>', html, re.S) if re.findall(r'<div class="room">.*?<div class="mainInfo">(.*?)</div>', html, re.S) else ['未知房型'],
            'area': re.findall(r'<div class="area">.*?<div class="mainInfo">(.*?)</div>', html, re.S) if re.findall(r'<div class="area">.*?<div class="mainInfo">(.*?)</div>', html, re.S) else ['未知面积'],
            'floor': re.findall(r'<div class="room">.*?<div class="subInfo">(.*?)</div>', html, re.S) if re.findall(r'<div class="room">.*?<div class="subInfo">(.*?)</div>', html, re.S) else ['未知楼层'],
            'total_price': [price + '万' for price in re.findall(r'<span class="total">(.*?)</span>', html, re.S)] if re.findall(r'<span class="total">(.*?)</span>', html, re.S) else ['未知总价'],
            'unit_price': [price + '元/平米' for price in re.findall(r'<span class="unitPriceValue">(.*?)<i>', html, re.S)] if re.findall(r'<span class="unitPriceValue">(.*?)<i>', html, re.S) else ['未知单价'],
            'agent': re.findall(r'<a class="ke-agent-sj-name.*?">(.*?)</a>', html, re.S) if re.findall(r'<a class="ke-agent-sj-name.*?">(.*?)</a>', html, re.S) else ['未知经纪人'],
            'agent_phone': [''.join(re.sub(r'<[^>]+>', '', phone).split()) for phone in re.findall(r'<div class="ke-agent-sj-phone ">(.*?)</div>', html, re.S)] if re.findall(r'<div class="ke-agent-sj-phone ">(.*?)</div>', html, re.S) else ['未知电话']
        }

        # 处理提取的数据（取第一个值）
        for key in house_info:
            house_info[key] = house_info[key][0]

        return house_info

    def crawl(self, base_url):
        """主爬虫方法"""
        # 获取首页HTML
        home_html = self.get_html(base_url)
        if not home_html:
            print("获取首页失败")
            return

        # 获取所有分页URL
        page_urls = self.get_page_urls(base_url)

        # 初始化数据库连接
        db = Db()
        try:
            # 遍历每个分页
            for page_url in page_urls:
                print(f"当前页面: {page_url}")

                # 获取当前页面HTML
                page_html = self.get_html(page_url)
                if not page_html:
                    continue

                # 获取当前页的所有房源详情链接
                house_urls = self.get_house_list(page_html)

                # 遍历每个房源详情页
                for house_url in house_urls:
                    # 随机延迟，防止被反爬
                    time.sleep(random.uniform(1, 2))

                    # 获取房源详情页HTML
                    house_html = self.get_html(house_url)
                    if not house_html:
                        continue

                    # 解析房源信息
                    house_info = self.get_house_info(house_html)

                    # 保存到数据库
                    db.insert(house_info)


        except Exception as e:
            print(f"爬虫主程序出错: {e}")
            print("错误详细信息:")
            # 打印错误详细信息
            print(traceback.format_exc())
        finally:
            # 关闭数据库连接
            db.close()


def main():
    base_url = 'https://sz.lianjia.com/ershoufang/'
    spider = Sprawl()
    spider.crawl(base_url)


if __name__ == '__main__':
    main()