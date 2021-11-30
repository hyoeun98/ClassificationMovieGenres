# MovieClassification
- 영화의 줄거리를 보고 장르를 분류


### workflow
1. watcha에서 영화 정보 crawling(제목, 줄거리, 평점, 장르, 태그, 연도, 국가) -> watcha_crawling.csv
2. watcha_crawling.csv를 cleaning -> movies.csv
3. 각 영화의 등장인물을 crawling -> mecab의 user dictionary 등재
4. mecab을 통해 tokenization << 지금
5. word2cev?
