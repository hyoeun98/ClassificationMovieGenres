### Mecab 사용자 사전 적용
- https://github.com/Pusnow/mecab-ko-msvc, https://github.com/Pusnow/mecab-ko-dic-msvc 최신 버전 설치 후
- C:\mecab\user-dic\xxx.csv 수정 (글자 깨질 시 메모장으로)
- C:\mecab\tools\add-userdic-win.ps1 실행
  - C:\mecab\mecab-ko-dic\user-xxx.csv 단어 비용 수정 (필요 시)
- C:\mecab\tools\compile-win.ps1 실행
- mecab = Mecab("C:/mecab/mecab-ko-dic")
  - 경로 명시 
