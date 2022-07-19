# MovieClassification
- 영화의 줄거리를 보고 장르를 분류

### Pipeline
1. Crawling (at least, 10000 movies)
2. Preprocessing -> ([id, story, genre])
3. ModelForSequenceClassification

### 고려할 점
- 한 movie에 대해 genre가 여러 개일 경우
  - 각 genre는 같은 weight를 가지는 것으로 한다.
- 줄거리에서 등장인물명이 방해가 되지 않을까?
  - 제거하기 어려움
  - 인명을 모두 special token으로 치환?
- 각 영화의 genre의 수가 다를 경우?
  - threshold를 정해야 할 듯
- metric은?
  - f1 score(recall, precision이 모두 중요함)

### Reference
- [multi-label classification](https://medium.com/huggingface/multi-label-text-classification-using-bert-the-mighty-transformer-69714fa3fb3d)
- [kaggle competition](https://www.kaggle.com/competitions/movie-genre-classification)
