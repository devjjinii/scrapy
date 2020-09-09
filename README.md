## Scrapy

* pip install scrapy
* scrapy startproject "프로젝트이름"
* scrapy genspider "크롤러이름" "크롤링페이지주소"
* scrapy crawl "크롤러이름"
* scrapy crawl "크롤러이름" -o "저장할 파일명" -t "csv/xml/json"
    * json 한글깨짐 > settings.py > FEED_EXPORT_ENCODING='utf-8' 추가
    * scrapy crawl "" -o "".json -t json