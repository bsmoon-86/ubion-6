## 지도 시각화 
## 패키지 설치 
install.packages('ggiraphExtra')
library(ggiraphExtra)
library(ggplot2)

## 미국 주별 강력 범죄율 정보
head(USArrests)
str(USArrests)
library(tibble)
crime = rownames_to_column(USArrests, var = 'state')
head(crime)

## state 컬럼의 데이터를 전부 소문자로 변경
crime$state = tolower(crime$state)

## 지도 데이터 패키지
install.packages('maps')

states_map = map_data('state')
View(states_map)

ggChoropleth(
  data = crime, 
  aes(fill = Murder, 
      map_id = state
      ), 
  map = states_map, 
  interactive = T
)

