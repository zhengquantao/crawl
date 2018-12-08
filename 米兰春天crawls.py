import requests
import json
import pymysql


#  获取店铺信息
def get_shop(url):
    kv = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0\
        .3440.106Safari / 537.36',
        'Referer': 'https: // h5.youzan.com / v2 / ump / multistore / homepage?kdt_id = 18669836 & offline_redirect = \
        https % 3A % 2F % 2Fh5.youzan.com % 2Fv2 % 2Fshowcase % 2Fgoods % 2FbriefGoodsWithTags.json % 3Ftag_alias % 5B % 5D % 3D3fuv2ms7 % 26perpage % 3D44',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Cookie': 'DO_CHECK_YOU_VERSION = 1;KDTSESSIONID = YZ488754298260307968YZqnc1w1H4;yz_ep_page_type_track = \
        iDJ3GNJDHbhHtOl6W3j3ZA % 3D % 3D;yz_log_ftime = 1536569706744;yz_log_uuid = 6825ce90 - 33c2 - 94b8 - 8169 - \
        2915fa4b87dc;_canwebp = 1;gr_user_id = 206c6e42 - d893 - 4559 - af0c - 04fba2bf19e3;_kdt_id_ = 18669836;\
        Hm_lvt_7bec91b798a11b6f175b22039b5e7bdd = 1536576473, 1538397537;nobody_sign = YZ488754298260307968YZqnc1w1H4;\
        yz_log_seqb = 1538619256507;Hm_lvt_679ede9eb28bacfc763976b10973577b = 1538309228, 1538363094, 1538486436, \
        1538619258;css_base = e76619006e57e80;css_goods = 1943a81d3941b1b;css_showcase = d81604421eb4318;\
        css_showcase_admin = 324df160da167a8;css_buyer = e5d58de420ec4cd;css_base_wxd = 499f4d24535c97b;\
        css_new_order = b5dbb4d1e3747a9;css_trade = 59d2eee6054e60e;yz_log_seqn = 10;Hm_lpvt_679ede9eb28bacfc763976b10973577b = 1538619378'
    }
    # 新建字典
    ls = {}
    for i in range(1, 3):
        # 获取所有店铺信息
        r = requests.get(url.format(i), headers=kv)
        shop_html = r.text
        # json信息转成字典
        shop_htmls = json.loads(shop_html)
        # print(shop_htmls, type(shop_htmls))
        # 分别获取店铺信息
        for n in shop_htmls['data']['list']:
            id = n['id']
            address = n['name']
            # print(address)
            # id对应address店地址
            ls[id] = address
    return ls


# 获取店铺商品数据
def get_goods_html(url, mes, lst):
    # 连接MySQL
    db = pymysql.connect(host='127.0.0.1', port=3306, db='pysql', user='root', passwd='12345678', charset='utf8')
    cursor = db.cursor()  # 创建游标
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN, zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'KDTSESSIONID': 'YZ488754298260307968YZqnc1w1H4',
        'Cookie': 'DO_CHECK_YOU_VERSION=1; KDTSESSIONID=YZ488754298260307968YZqnc1w1H4; yz_ep_page_type_track=iDJ3GNJDHbhHtOl6W3j3ZA%3D%3D; yz_log_ftime=1536569706744; yz_log_uuid=6825ce90-33c2-94b8-8169-2915fa4b87dc; _canwebp=1; Hm_lvt_7bec91b798a11b6f175b22039b5e7bdd=1536576473; gr_user_id=206c6e42-d893-4559-af0c-04fba2bf19e3;\
     _kdt_id_=18669836; css_base=e76619006e57e80; css_showcase_admin=324df160da167a8; css_base_wxd=499f4d24535c97b; css_buyer=e5d58de420ec4cd; css_goods=1943a81d3941b1b; css_new_order=b5dbb4d1e3747a9; css_showcase=d81604421eb4318; css_trade=59d2eee6054e60e; nobody_sign=YZ488754298260307968YZqnc1w1H4; yz_log_seqb=1538363093050;\
      Hm_lvt_679ede9eb28bacfc763976b10973577b=1538036491,1538228299,1538309228,1538363094; Hm_lpvt_679ede9eb28bacfc763976b10973577b=1538364290; yz_log_seqn=561',
        'Host': 'h5.youzan.com',
        'Pragma': 'no-cache',
        'Referer': 'https://h5.youzan.com/v2/home/10xp8m96e?reft=1538364209207&spm=f46693896',
    }
    for n in mes:
        for s in lst:
            r = requests.get(url.format(s, n),  headers=header)
            if r != '':
                # 将json转成字典
                html = json.loads(r.text)
                # 分别获取个个商品信息
                for i in html['data'][0][s]:
                    shop = mes[n]
                    title = i['title']
                    time = i['created_time']
                    price = i['price']
                    image_url = i['image_url']
                    print(shop, title, time, price, image_url)
                    cursor.execute("insert into supershop(shop, title, times, price, image_url) values(%s, %s, %s, %s, %s)", (shop, title, time, price, image_url))
            else:
                continue
    db.commit()  # 提交更新



if __name__ == '__main__':
    shop_url = "https://h5.youzan.com/v2/ump/multistore/recommendofflinelistNew.json?id=20484253&perpage=10&page={}&kdt_id=18669836"
    goods_url = "https://h5.youzan.com/v2/showcase/goods/briefGoodsWithTags.json?tag_alias%5B%5D={}&oid={}"
    ls = [20205562, 20356228, 20405625, 20404378, 20459041, 20460543, 21430061, 21454693, 20484810, 20484253, 52635604,
          52635712, 52636207, 52634304, 52635107, 52635304, 53292128]
    # 加密后商品的分类
    goods_ls = ['13zpe3s41', 'vio4ds6w', 'pwe2eov71', 'vwmipgg7', '1h8cj3qx3', 'nrayj0kf1', '1099g83fp', 'ryxuyhr7', 'd23ao5eg1',\
                'dmb1ger3', '19ewi7lua', '10meycm5m', '176eqqnw8', '1brsfl2wb', '3fuv2ms7', '7xhlmaun', 'chb32dac', 'fqqmas4q',\
                'gbdppwx1', 'm8nol604', 'ueptnj05', 'wksayue9']
    msg = get_shop(shop_url)
    get_goods_html(goods_url, msg, goods_ls)