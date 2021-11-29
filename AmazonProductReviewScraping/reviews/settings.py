import scraper_helper as sh

BOT_NAME = 'reviews'

SPIDER_MODULES = ['reviews.spiders']
NEWSPIDER_MODULE = 'reviews.spiders'

AUTOTHROTTLE_ENABLED = True
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = sh.get_dict(
'''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
cookie: session-id=143-5065477-6172528; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=134-6673698-5515818; session-token=by0ChD+Nvqo3gjFTZrYrMTKIdp1jmsIfBF++8cRKs7W4vkmbxuPKmBWYNcn9XEtoP9Itd3kPgPs1i8bB55Ybk9eTDAgz1aM0CgvSLSDvRV8egsq/WuaLGwda3c1Fxuz6eGuSJDFWaIsYuVPyWjYMKg62Y7yLpE0ELCBJWzyWKYpXAYxgL4KumvA31eBN5vmm; csm-hit=tb:s-KM1MGBAJSXHB82XHA59Q|1638218147027&t:1638218150133&adb:adblk_no; lc-main=en_US
downlink: 10
ect: 4g
rtt: 50
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36

''')

