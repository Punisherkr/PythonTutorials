days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
##########################################################
##########################################################

for d in days:
    print(d)
    #     Prints out
    ###   Mon
    ###   Tue
    ###   Wed
    ###   Thu
    ###   Fri
    ###   Sat
    ###   Sun
##########################################################
print("분리선1")
##########################################################
# days 라는 집단 안에서 e는
# 순서대로 읽다가 "Thu"값에서 출력을 중단한다
#(break)
# 그  e값을 print
for e in days:
    if(e=="Thu"):break
    print(e)
    #     Prints out
    ###   Mon
    ###   Tue
    ###   Wed
    
##########################################################
print("분리선2")
##########################################################
# days 라는 집단 안에서 f는
# 순서대로 읽다가 "Wed"값에서 출력을 중단하지 않고
#(continue)
#"Wed"를 제외하고 나머지
# 그  f값을  나열 순서대로 print
for f in days:
    if(f=="Wed"):continue
    print(f)
