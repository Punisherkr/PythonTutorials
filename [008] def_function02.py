def add_ten_to_age(age):
    new_age = age +10
    #return은 리턴되는 값을 지정한다
    #즉 age 변수에따른 값을 출력한다
    return new_age



#add_ten_to_age(age)이므로  def로 add_ten_to_age(age)로 정의 했으니 뒤에 값에 age변수에 들어갈 값 입력 하면된다.
#그러면add_ten_to_age(age)에서 리턴되는 값이 출력된다
#age를 3이라고 설정해보자
how_old_will_I_be = add_ten_to_age(3)
#그러면 
print(how_old_will_I_be)
#아래 식도 작동하지만 유용하지 않다
print(add_ten_to_age(4))