# MovieClassification
- 영화의 줄거리를 보고 장르를 분류

### Pipeline
1. Crawling (>5000 movies)
2. Preprocessing
    - Story 추출
    - 개행문자 제거
    - 
4. ModelForSequenceClassification

### 고려할 점
- 한 movie에 대해 genre가 여러 개일 경우
  - 각 genre는 같은 weight를 가지는 것으로 한다.  

### Reference
- [multi-label classification /w Bert](https://medium.com/huggingface/multi-label-text-classification-using-bert-the-mighty-transformer-69714fa3fb3d)
- 
