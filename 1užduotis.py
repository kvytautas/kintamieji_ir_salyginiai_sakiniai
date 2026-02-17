# print ("*********** Užduotis1 ************")
# from datetime import datetime
#
# name="Vytautas"
# last_name="Kučinskas"
# birth_year= 1988
# current_year = datetime.now().year
# xx = current_year - birth_year
#
# print("Aš esu ",name,last_name,f"Man yra {xx} metų" )
#
# print ("************ Užduotis2 *************")
#
# import random
# rnd_num1 = random.randint(0, 4)
# rnd_num2 = random.randint(0, 4)
# # rnd_num1=0
# # rnd_num2=2
# print("rnd_num1",rnd_num1)
# print("rnd_num2",rnd_num2)
# # result=round(rnd_num2 / rnd_num1)
# # print("result,"f"{result:.2f}")
# if rnd_num1 == 0 or rnd_num2 == 0:
#     print("dalyba is nulio")
# else:
#     if rnd_num1 == rnd_num2:
#         print(rnd_num1,"lygu",rnd_num2)
#     if  rnd_num1 > rnd_num2:
#         ressult = round(rnd_num1 / rnd_num2,2)
#         print("result1",f"{ressult:.2f}")
#     if  rnd_num2 > rnd_num1:
#         ressult = round(rnd_num2 / rnd_num1,2)
#         print("result2",f"{ressult:.2f}")
#
# print ("************* Užduotis3 **************")
#
#
# rnd_num1 = random.randint(0, 25)
# rnd_num2 = random.randint(0, 25)
# rnd_num3 = random.randint(0, 25)
# # rnd_num1=1
# # rnd_num2=3
# # rnd_num3=3
# print("rnd_num1",rnd_num1)
# print("rnd_num2",rnd_num2)
# print("rnd_num3",rnd_num3)
#
# if rnd_num1 == rnd_num2 and rnd_num1 == rnd_num3:
#     print("Visi lygūs:",rnd_num1)
# # else:
# elif rnd_num1 > rnd_num2 and rnd_num3 > rnd_num1:
#         print("ats",rnd_num1)
# elif rnd_num2 > rnd_num1 and rnd_num3 > rnd_num2:
#         print("ats", rnd_num2)
# elif rnd_num3 > rnd_num1 and rnd_num2 > rnd_num3:
#         print("ats", rnd_num3)
# else:
#     print("Deja, susigeneravo du lygūs skaičiai")
#
# print("************** Užduotis4 ***************")
#
# a = random.randint(1, 10)
# b = random.randint(1, 10)
# c = random.randint(1, 10)
# # print("a",a)
# # print("b",b)
# # print("c",c)
#
# if a + b > c and a + c > b and b + c > a:
#     print(f"Galima iš {a}, {b}, {c} suformuoti trikampį" )
# else:
#     print(f"Negalima iš {a}, {b}, {c} suformuoti trikampio")
import datetime

# print("*************** Užduotis5 ****************")
# import random
#
# vienas = random.randint(0, 2)
# du = random.randint(0, 2)
# trys = random.randint(0, 2)
# keturi = random.randint(0, 2)
#
# print("1",vienas)
# print("2",du)
# print("3",trys)
# print("4",keturi)
#
# ats0=0
# ats1=0
# ats2=0
#
# if vienas > 1:
#     ats2 = ats2 + 1
# elif vienas == 1:
#     ats1 = ats1 + 1
# elif vienas < 1:
#     ats0 = ats0 + 1
#
# if du > 1:
#     ats2 = ats2 + 1
# elif du == 1:
#     ats1 = ats1 + 1
# elif du < 1:
#     ats0 = ats0 + 1
#
# if trys > 1:
#     ats2 = ats2 + 1
# elif trys == 1:
#     ats1 = ats1 + 1
# elif trys < 1:
#     ats0 = ats0 + 1
#
# if keturi > 1:
#     ats2 = ats2 + 1
# elif keturi == 1:
#     ats1 = ats1 + 1
# elif keturi < 1:
#     ats0 = ats0 + 1
#
# print("Turim: ",ats0," nulių",ats1," vienetų",ats2," dvejetų" )

# print("**************** Užduotis6 *****************")
# import random
# rnd_num1 = random.randint(-10, 10)
# rnd_num2 = random.randint(-10, 10)
# rnd_num3 = random.randint(-10, 10)
# # rnd_num1=3
# # rnd_num2=3
# # rnd_num3=3
# print("rnd_num1",rnd_num1)
# print("rnd_num2",rnd_num2)
# print("rnd_num3",rnd_num3)
#
# if rnd_num1 < 0:
#     print(f"[{rnd_num1}]")
# elif rnd_num1 == 0:
#     print(f"({rnd_num1})")
# else:
#     print(f'{{{rnd_num1}}}')
#
# if rnd_num2 < 0:
#     print(f"[{rnd_num2}]")
# elif rnd_num2 == 0:
#     print(f"({rnd_num2})")
# else:
#     print(f'{{{rnd_num2}}}')
#
# if rnd_num3 < 0:
#     print(f"[{rnd_num3}]")
# elif rnd_num3 == 0:
#     print(f"({rnd_num3})")
# else:
#     print(f'{{{rnd_num3}}}')
#
# print("****************** Užduotis7 ******************")
# import random
# rnd_num1 = random.randint(5, 3000)
# # rnd_num1=2001
# minus3proc=0.97
# minus4proc=0.96
#
# if rnd_num1 <= 1000:
#     print(rnd_num1, "žvakės kainuos be nuolaidos", rnd_num1, "EUR")
# elif rnd_num1 > 1000 and rnd_num1 <= 2000:
#     print(rnd_num1,"žvakės kainuos",f"{rnd_num1*minus3proc:.2f}","EUR")
#     print("kaina su 3% nuolaida")
# else:
#     print(rnd_num1,"žvakės kainuos",f"{rnd_num1*minus4proc:.2f}","EUR")
#     print("kaina su 4% nuolaida")

print("******************* Užduotis8 *******************")

import random
rnd_num1 = random.randint(0, 100)
rnd_num2 = random.randint(0, 100)
rnd_num3 = random.randint(0, 100)
# rnd_num1=9
# rnd_num2=9
# rnd_num3=9
print("rnd_num1",rnd_num1)
print("rnd_num2",rnd_num2)
print("rnd_num3",rnd_num3)

avg=(rnd_num1+rnd_num2+rnd_num3)/3
avg2=0
extra=0
print("Vidurkis",round(avg))

if rnd_num1 >= 10 and rnd_num1 <= 90:
    avg2 = rnd_num1
    extra = extra + 1
if rnd_num2 >= 10 and rnd_num2 <= 90:
    avg2 = avg2 + rnd_num2
    extra = extra + 1
if rnd_num3 >= 10 and rnd_num3 <= 90:
    avg2 = avg2 + rnd_num3
    extra = extra + 1
# print("avg2",avg2)
# print("extra",extra)

if extra == 0:
    print("EXTRA vidurkis iš nulio negalimas")
else:
    print("EXTRA vidurkis po apribojimų",round(avg2/extra))

# total_sum = 0
# count = 0
#
# if 10 <= rnd_num1 <= 90:
#     total_sum += rnd_num1
#     count += 1
#
# if 10 <= rnd_num2 <= 90:
#     total_sum += rnd_num2
#     count += 1
#
# if 10 <= rnd_num3 <= 90:
#     total_sum += rnd_num3
#     count += 1

print("******************* Užduotis9 *******************")
# valandos = 0
# minutes = 59
# sekundes = 0

# # sugeneruoju papildomas sekundes
# papildomos_sekundes = random.randint( a: 0, b: 300)
#
# print(f"prideti sekundziu:{papildomos_sekundes}")
#
# # papildomas sekundes prideti prie laiko (laikas sekundemis + papildomos sekundes)
# # valandos+3600 - pervirsис nueina i minutes ir t.t.
# viso_sekundziu = valandos*3600+minutes*60+sekundes+papildomos_sekundes
#
# # perskaiciuoju nauja laika (% 24 - laikas po 23:59:59 prasides nuo 00:00:00)
# naujos_valandos = (viso_sekundziu//3600) % 24
# naujos_minutes = (viso_sekundziu % 3600)//60
# naujos_sekundes = viso_sekundziu % 60
#
# print(f"naujas laikas:{laiko_formatavimas(naujos_valandos,naujos_minutes,naujos_sekundes)}")


print("******************* Užduotis10 *******************")
# 36 salygos kodui
