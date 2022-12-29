# 백터 데이터의 타입 생성
a = c (1,2,3,4,5)
a
b <- 1:5
b
c(1,2) -> c
a = c(1, 'moon')
a
#행렬 
d = array(1:20, dim=c(4,5))
d
e = matrix(1:10, nrow=2)
e

#리스트 (python에서 dict 형태와 흡사)
f = list(name = "test", age = 20, phone="01012345678")
f
f["name"]

#데이터프레임 
df = data.frame(name=c("test", "test2"), 
                age = c(30, 20), 
                phone = c('01012345678', '01098765432'))
df

#if문
a = 10
if (a > 5){
  print('a는 5보다 크다')
}

if (a > 15){
  print("a는 15보다 크다")
}else if (a >= 10){
  print("a는 10보다 크거나 같거나 15보다 작거나 같다. ")
}else {
  print("a는 10보다 작다")
}

#which문 ( python 에서는 index() )
name = c("test", "test2", "test3")
which(name == 'test2')
which(name == "test5")
which(name != "test2")

# 함수 (function 키워드로 함수를 선언)
# 매개변수가 없는 경우
func_1 = function(){
  return("Hello R")
}
func_1()

# 매개변수가 있는 경우
func_2 = function(x, y){
  result = x ^ y
  return(result)
}
func_2(5, 2)

'%s%' = function(x, y){
  result = x ^ y
  return(result)
}
5%s%2

#매개변수의 기본값 설정
func_4 = function(x, y=5){
  result = x ^ y 
  return(result)
}
func_4(2)     #32
func_4(2, 10) ##1024

## 매개변수의 개수가 가변인 경우
## python def func(x, *y)
func_5 = function(x, ...){
  print(x)
  print(c(...))
}
func_5(1,2,3,4,5,6)
func_5(1,2,3)


##백터형 데이터를 가지고 데이터프레임 생성
##백터데이터의 길이가 동일 해야 가능
name = c("test", "test2", "test3", "test4")
grade = c(1,3,2,1)
student = data.frame(name, grade)
student

midturm = c(70, 80, 60, 90)
final = c(60, 90, 80, 90)
scores = cbind(midturm, final)
scores

students = data.frame(student, scores)
students

gender = c("M", "F", "F", "M")
students = cbind(students, gender)
students

## 중간 성적과 기말 성적의 합을 새로운 컬럼을 추가 
## 새로운 컬럼의 이름은 total_score
## case1
total_score = midturm + final
total_score
cbind(students, total_score)
## 특정 컬럼의 데이터를 추출
students[["midturm"]]
students$midturm
students[[3]]

# case2 
total_score_2 = students$midturm + students[['final']]
cbind(students, total_score_2)


## 행을 추가하는 함수 rbind()
## rbind()는 데이터프레임의 형태와 같은 형태의 
## 데이터프레임을 추가

new_student = data.frame(
    name = "test5", 
    grade = 3, 
    midturm = 80, 
    final = 60, 
    gender = 'F'
)
new_student
rbind(students, new_student) -> students

## 데이터프레임의 필터링 
## 데이터프레임명[행의 기준, 열의 기준]
students[1, ]
students[c(2,4), ]
students[1:3, ]

## 해당 인덱스만 제외하고 출력
students[-1, ]

## 조건을 이용해서 필터링 
## 학년이 2학년 이상인 경우
students$grade >= 2
students[students$grade >=2, ]

## 정렬 - 기본값 오름차순
order(students$grade)
students[order(students$grade), ]

## 내림차순
order(students$grade, decreasing = TRUE)
order(-students$grade)
