import requests
from MeituanSpider.settings import GAODE_API_KEY
from shapely.geometry import Point, MultiPoint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
}
city_url = 'https://restapi.amap.com/v3/config/district?subdistrict={0}&extensions=all&key={1}&s=rsv3&output=json&keywords={2}'


def city_point(city):
    """
    :param city:需要查询的城市
    :return:城市内的符合要求的等距坐标

    """
    list_p = []
    list_q = []
    # 根据接口查询城市边界的坐标
    url = city_url.format(0, GAODE_API_KEY, city)
    response = requests.get(url=url, headers=headers)
    data = response.json()
    # 获得城市边界坐标
    poly = data['districts'][0]['polyline']
    # 不匹配岛屿
    poly = re.sub('\|.*\|',';',poly)
    # 将坐标进行处理，获得四个角落的坐标，构造一个矩形网络
    poly_list1 = poly.split(';')
    poly_list2 = list(zip(*[a.split(',') for a in poly_list1]))
    max_lng = max([int(a.replace('.', '')) for a in poly_list2[0]])
    min_lng = min([int(a.replace('.', '')) for a in poly_list2[0]])
    max_lat = max([int(a.replace('.', '')) for a in poly_list2[1]])
    min_lat = min([int(a.replace('.', '')) for a in poly_list2[1]])
    # 纬度1°为111.3195km，经度每度为111.3195cos(纬度)
    g = int((max_lng - min_lng) * 102.3022 / 4242640)
    g1 = [round(min_lng + i * 4242640 / 102.3022) for i in range(1, g)]
    h = int((max_lat - min_lat) * 111.3195 / 4242640)
    h1 = [round(min_lat + i * 4242640 / 111.3195) for i in range(1, h)]
    # 获得矩形网络内距离为4.2km的所有坐标
    while g1:
        g11 = g1.pop()
        for j in h1:
            list_p.append((g11, j))
    k = [a.split(',') for a in poly_list1]
    coords = [tuple(map(int, (i.replace('.', ''), j.replace('.', '')))) for i, j in k]
    poly = MultiPoint(coords).convex_hull
    # 根据判断所有属于城市内的坐标并返回值
    print(len(list_p))
    for p in list_p:
        if poly.contains(Point(p)):
            list_q.append(p)

    return [(a / 1000000, b / 1000000) for a, b in list_q]
