import re
import time
from urllib.request import urlopen, urlretrieve


# 下载HTML
def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html


# 从html中解析出图片URL
def getImg(html):
    reg = r'src="(.*?\.gif)"'
    imgre = re.compile(reg);
    htmld = html.decode('utf-8')
    imglist = imgre.findall(htmld)
    return imglist


# 下载处理
def imgDownload(imgUrl):
    urlretrieve(imgUrl, '%s' % imgUrl[-7:])


# 主函数
def main():
    picture = '''https://cdn.heweather.com/cond_icon/100.png
https://cdn.heweather.com/cond_icon/101.png
https://cdn.heweather.com/cond_icon/102.png
https://cdn.heweather.com/cond_icon/103.png
https://cdn.heweather.com/cond_icon/104.png
https://cdn.heweather.com/cond_icon/200.png
https://cdn.heweather.com/cond_icon/201.png
https://cdn.heweather.com/cond_icon/202.png
https://cdn.heweather.com/cond_icon/203.png
https://cdn.heweather.com/cond_icon/204.png
https://cdn.heweather.com/cond_icon/205.png
https://cdn.heweather.com/cond_icon/206.png
https://cdn.heweather.com/cond_icon/207.png
https://cdn.heweather.com/cond_icon/208.png
https://cdn.heweather.com/cond_icon/209.png
https://cdn.heweather.com/cond_icon/210.png
https://cdn.heweather.com/cond_icon/211.png
https://cdn.heweather.com/cond_icon/212.png
https://cdn.heweather.com/cond_icon/213.png
https://cdn.heweather.com/cond_icon/300.png
https://cdn.heweather.com/cond_icon/301.png
https://cdn.heweather.com/cond_icon/302.png
https://cdn.heweather.com/cond_icon/303.png
https://cdn.heweather.com/cond_icon/304.png
https://cdn.heweather.com/cond_icon/305.png
https://cdn.heweather.com/cond_icon/306.png
https://cdn.heweather.com/cond_icon/307.png
https://cdn.heweather.com/cond_icon/308.png
https://cdn.heweather.com/cond_icon/309.png
https://cdn.heweather.com/cond_icon/310.png
https://cdn.heweather.com/cond_icon/311.png
https://cdn.heweather.com/cond_icon/312.png
https://cdn.heweather.com/cond_icon/313.png
https://cdn.heweather.com/cond_icon/400.png
https://cdn.heweather.com/cond_icon/401.png
https://cdn.heweather.com/cond_icon/402.png
https://cdn.heweather.com/cond_icon/403.png
https://cdn.heweather.com/cond_icon/404.png
https://cdn.heweather.com/cond_icon/405.png
https://cdn.heweather.com/cond_icon/406.png
https://cdn.heweather.com/cond_icon/407.png
https://cdn.heweather.com/cond_icon/500.png
https://cdn.heweather.com/cond_icon/501.png
https://cdn.heweather.com/cond_icon/502.png
https://cdn.heweather.com/cond_icon/503.png
https://cdn.heweather.com/cond_icon/504.png
https://cdn.heweather.com/cond_icon/507.png
https://cdn.heweather.com/cond_icon/508.png
https://cdn.heweather.com/cond_icon/900.png
https://cdn.heweather.com/cond_icon/901.png
https://cdn.heweather.com/cond_icon/999.png
'''
    imglist = picture.split("\n")
    for imgurl in imglist:
        print(imgurl)
        print('%s' % imgurl[-7:])
    for imgurl in imglist:
        imgDownload(imgurl)

        # 执行主函数


if __name__ == '__main__':
    main()
