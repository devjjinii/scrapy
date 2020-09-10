## Scrapy

* pip install scrapy
* scrapy startproject "프로젝트이름"
* scrapy genspider "크롤러이름" "크롤링페이지주소"
* scrapy crawl "크롤러이름"
* scrapy crawl "크롤러이름" -o "저장할 파일명" -t "csv/xml/json"
    * json 한글깨짐 > settings.py > FEED_EXPORT_ENCODING='utf-8' 추가
    * scrapy crawl "" -o "".json -t json
* setting.py > ITEM_PIPELINES 주석 제거 (파이프라인 사용)
    * 데이터 후처리, 조건 등 추가할 때 