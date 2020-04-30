import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 베이스오일 게시판
for i in range(1,2):
    data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=078&sort=&page=' + str(i),headers=headers)
    data.encoding = None
    soup = BeautifulSoup(data.text, 'html.parser')
    ingredients = soup.select('td > div.tb-center')[4:]
    if ingredients is not None:
        for ing in ingredients:
            img_url = ing.select_one('img')['src']
            title = ing.select_one('li.dsc').text.strip()
            desc = ing.select_one('li.dsc2').text.strip()
            base_price_str = ing.select_one('li.price').text.strip().split(' ')[56].replace(",","").replace("원","")
            base_price = int(base_price_str)
            option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
            # 옵션 페이지
            data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
            data2.encoding = None
            soup = BeautifulSoup(data2.text, 'html.parser')
            options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
            for opt in options:
                if opt is not None:
                    option = (str(opt).split('">')[1].split('</')[0])
                    if '+' in option:
                        volume = option.split("(")[0]
                        additional_price = int(option.split("+")[1].split(")")[0].replace(",",""))
                        price = base_price + additional_price
                        print(volume)
                        print(additional_price)
                    else:
                        volume = option
                        additional_price = 0
                        print(volume)
                        print(additional_price)
                else:
                    break



            #
            # for opt in options:
            #     if opt is not None:
            #         additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
            #         volume = str(opt).split('title="')[1].split('"')[0]
            #         price = base_price + additional_price
            #         inci =
            #         doc = {
            #             'source' : '오일공구',
            #             'category' : '베이스오일',
            #             'INCI' :
            #             'img_url' : img_url,
            #             'title' : title,
            #             'desc' : desc,
            #             'price' : price,
            #             'volume' : volume
            #             }
            #
            #         print(doc)
            #
            #     else:
            #         break

#
# # 아로마오일 게시판
# for i in range(1,100):
#     data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=079&sort=&page=' + str(i),headers=headers)
#     data.encoding = None
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ingredients = soup.select('td > div.tb-center')[4:]
#     if ingredients is not None:
#         for ing in ingredients:
#             img_url = ing.select_one('img')['src']
#             title = ing.select_one('li.dsc').text.strip()
#             desc = ing.select_one('li.dsc2').text.strip()
#             base_price_str = ing.select_one('li.price').text.strip().split(' ')[56].replace(",", "").replace("원", "")
#             base_price = int(base_price_str)
#             option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
#
#             # 옵션 크롤링
#             data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
#             data2.encoding = None
#             soup = BeautifulSoup(data2.text, 'html.parser')
#             options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
#             for opt in options:
#                 if opt is not None:
#                     additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
#                     volume = str(opt).split('title="')[1].split('"')[0]
#                     price = base_price + additional_price
#                     doc = {
#                         'source' : '오일공구',
#                         'category' : '아로마오일',
#                         'img_url' : img_url,
#                         'title' : title,
#                         'desc' : desc,
#                         'price' : price,
#                         'volume' : volume
#                     }
#
#                 else:
#                     break
#
# # 프래그런스 게시판
# for i in range(1,100):
#     data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=080&sort=&page=' + str(i),headers=headers)
#     data.encoding = None
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ingredients = soup.select('td > div.tb-center')[4:]
#     if ingredients is not None:
#         for ing in ingredients:
#             img_url = ing.select_one('img')['src']
#             title = ing.select_one('li.dsc').text.strip()
#             desc = ing.select_one('li.dsc2').text.strip()
#             base_price_str = ing.select_one('li.price').text.strip().split(' ')[56]
#             base_price = int(base_price_str)
#             option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
#
#             # 옵션 크롤링
#             data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
#             data2.encoding = None
#             soup = BeautifulSoup(data2.text, 'html.parser')
#             options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
#             for opt in options:
#                 if opt is not None:
#                     additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
#                     volume = str(opt).split('title="')[1].split('"')[0]
#                     price = base_price + additional_price
#                     doc = {
#                         'source': '오일공구',
#                         'category': '프래그런스',
#                         'img_url': img_url,
#                         'title': title,
#                         'desc': desc,
#                         'price': price,
#                         'volume': volume
#                     }
#
#                 else:
#                     break
#
#
# #플로럴워터 게시판
# for i in range(1,100):
#     data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=002&sort=&page=' + str(i),headers=headers)
#     data.encoding = None
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ingredients = soup.select('td > div.tb-center')[4:]
#     if ingredients is not None:
#         for ing in ingredients:
#             img_url = ing.select_one('img')['src']
#             title = ing.select_one('li.dsc').text.strip()
#             desc = ing.select_one('li.dsc2').text.strip()
#             base_price_str = ing.select_one('li.price').text.strip().split(' ')[56]
#             base_price = int(base_price_str)
#             option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
#
#             # 옵션 크롤링
#             data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
#             data2.encoding = None
#             soup = BeautifulSoup(data2.text, 'html.parser')
#             options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
#             for opt in options:
#                 if opt is not None:
#                     additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
#                     volume = str(opt).split('title="')[1].split('"')[0]
#                     price = base_price + additional_price
#                     doc = {
#                         'source': '오일공구',
#                         'category': '플로럴워터',
#                         'img_url': img_url,
#                         'title': title,
#                         'desc': desc,
#                         'price': price,
#                         'volume': volume
#                     }
#
#                 else:
#                     break
#
#
# #화장품원료 게시판
# for i in range(1,26):
#     data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=081&sort=&page=' + str(i),headers=headers)
#     data.encoding = None
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ingredients = soup.select('td > div.tb-center')[4:]
#     for ing in ingredients:
#         img_url = ing.select_one('img')['src']
#         title = ing.select_one('li.dsc').text.strip()
#         desc = ing.select_one('li.dsc2').text.strip()
#         base_price_str = ing.select_one('li.price').text.strip().split(' ')[56]
#         base_price = int(base_price_str)
#         option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
#
#         # 옵션 크롤링
#         data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
#         data2.encoding = None
#         soup = BeautifulSoup(data2.text, 'html.parser')
#         options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
#         for opt in options:
#             if opt is not None:
#                 additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
#                 volume = str(opt).split('title="')[1].split('"')[0]
#                 price = base_price + additional_price
#                 doc = {
#                     'source': '오일공구',
#                     'category': '화장품원료',
#                     'img_url': img_url,
#                     'title': title,
#                     'desc': desc,
#                     'price': price,
#                     'volume': volume
#                 }
#
#             else:
#                 break
#
# #비누원료 게시판
# for i in range(1,20):
#     data = requests.get('http://www.go5109.com/shop/shopbrand.html?type=X&xcode=082&sort=&page=' + str(i),headers=headers)
#     data.encoding = None
#     soup = BeautifulSoup(data.text, 'html.parser')
#     ingredients = soup.select('td > div.tb-center')[4:]
#     for ing in ingredients:
#         img_url = ing.select_one('img')['src']
#         title = ing.select_one('li.dsc').text.strip()
#         desc = ing.select_one('li.dsc2').text.strip()
#         base_price_str = ing.select_one('li.price').text.strip().split(' ')[56]
#         base_price = int(base_price_str)
#         option_url = str(ing.select_one('ul.info > li > div.thumb > a')).split('branduid=')[1].split('&')[0]
#
#         # 옵션 크롤링
#         data2 = requests.get('http://www.go5109.com/shop/shopdetail.html?branduid=' + option_url, headers=headers)
#         data2.encoding = None
#         soup = BeautifulSoup(data2.text, 'html.parser')
#         options = soup.select('td > div.opt-wrap > dl > dd > select.basic_option > option')[1:]
#         for opt in options:
#             if opt is not None:
#                 additional_price = int(str(opt).split('matrix="')[1].split('price="')[1].split('"')[0])
#                 volume = str(opt).split('title="')[1].split('"')[0]
#                 price = base_price + additional_price
#                 doc = {
#                     'source': '오일공구',
#                     'category': '비누원료',
#                     'img_url': img_url,
#                     'title': title,
#                     'desc': desc,
#                     'price': price,
#                     'volume': volume
#                 }
#
#             else:
#                 break