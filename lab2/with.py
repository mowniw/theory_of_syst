studentsNumber=['1111 1001','1111 1002','1111 1003','1111 1004','1111 1101','1111 1102',
                '1111 1103','1111 1104','1111 1105','1111 1106','1111 1107','1111 1108',
                '1111 1109','1111 1110','1111 1111','1111 1112','1111 1113','1111 1114',
                '1111 1115','1111 1116','1111 1117','1111 1118','1111 1119','1111 1120',
                '1111 1121','1111 1122','1111 1123','1111 1124','1111 1125','1111 1126',
                '1111 1127','1111 1128','1111 1129','1111 1130','1111 1131','1111 1132',
                '1111 1133','1111 1134','1111 1135','1111 1136','1111 1137','1111 1138',
                '1111 1139','1111 1140','1111 1141','1111 1142','1111 1143','1111 1144',
                '1111 1145','1111 1146'
                ]


students=['Старовойтов Александр Викторович','Гусельникова Анастасия Витальевна',
          'Захарова Полина Дмитриевна','Шапошник Катерина Дмитриевна',
          'Первый Антон Антонович ', 'Второй Илья Витальевич' ,
          'Третий Валерий Альбертович' , 'Четвертый Игорь Витальевич',
          'Пятый Михаил Дмитриевич ','Шестой Виктор Сергеевич ',
          'Седьмой Антон Иванович' , 'Восьмой Илья Антонович' ,
          'Девятый Игорь Андреевич' , 'Десятый Андрей Андреевич' ,
          'Одиннадцатый Роберт Евгеньевич' , 'Двенадцатый Максим Пантелеевич' ,
          'Тринадцатый Тарас Григорович' , 'Четырнадцатый Илья Витальевич' ,
          'Пятнадцатый Валерий Семенович' , 'Шестнадцатый Олег Максимович' ,
          'Семнадцатый Игорь Олегович' , 'Восемнадцатый Константин Геннадьевич',
          'Девятнацатый Иван Александрович' , 'Двадцатый Антон Максимович' ,
          'Двадцатьпервый Илья Евгеньевич' ,'Двадцатьвторой Данил Алексеевич' ,
          'Двадцатьтретий Артем Михайлович' , 'Двадцатьчетвертый Василий Павлович' ,
          'Двадцатьпятый Владимир Дмитриевич' ,'Двадцатьшестой Андрей Игнатьевич' ,
          'Двадцатьседьмой Александр Леонардович' , 'Двадцатьвосьмой Василий Иванович' ,
          'Двадцатьдевятый Марк Ильич' , 'Тридцатый Николай Михайлович' ,
          'Тридцатьпервый Данил Леонидович' , 'Тридцатьвторой Виктор Алексеевич' ,
          'Тридцатьтретий Евгений Иванович' ,'Тридцатьчетвертый Сергей Петрович' ,
          'Тридцатьпятый Антон Антонович' , 'Тридцатьшестой Сергей Федерович' ,
          'Тридцатьседьмая Анна Арнольдовна' ,'Тридцатьвосьмой Лев Александрович' ,
          'Тридцатьдевятый Юрий Павлович' , 'Сороковая Татьяна Александровна' ,
          'Сорокпервый Павел Кузьмич' ,'Сороквторая Мария Иосифовна' ,
          'Сороктретий Лев Григорьевич' ,'Сорокчетвертый Михаил Прокопьевич' ,
          'Сорокпятая Виктория Алексеевна' ,'Сорокшестой Александр Евгеньевич'
            ]

meals=[4,5,6,5,2,6,3,6,1,10,5,2,6,10,8,2,4,8,2,4,6,7,2,4,1,7,3,7,3,5,6,3,4,
       6,3,7,2,3,4,7,8,4,5,7,2,5,2,3,4,2 ]

smoking=[0,0,0,0,1,5,2,6,23,32,2,6,23,96,2,3,6,6,23,6,2,3,5,2,3,4,11,5,7,1,3,6,1,
         7,2,1,0,35,7,8,3,5,6,0,1,3,4,1,2,3,6   ]

sport=[2,4,3,3,0,2,5,1,2,4,6,7,2,5,1,5,1,2,5,2,6,7,3,2,5,3,4,6,2,3,4,6,2,3,
       6,1,0,5,6,2,3,6,2,1,0,3,6,2,3,6     ]

lessons=[5,5,5,5,3,6,1,7,3,6,1,0,2,0,3,5,1,6,2,4,6,1,2,6,2,6,2,4,7,0,2,1,5,2,6,
         1,6,1,3,6,1,2,5,3,6,2,3,6,1,3     ]

sleep=[8,8,9,8,6,7,8,4,7,3,4,11,7,2,6,8,3,5,7,6,8,9,10,11,7,8,6,12,11,8,7,9,6,
       8,10,7,4,8,8,10,11,8,6,7,8,12,10,6,8,11  ]
a=' '
#print('1',8*a,'|')

health=[0]*50
pit=['test']*50
sig=['test']*50
zan=['test']*50
urok=['test']*50
son=['test']*50
zdor=['test']*50


for i in range(50):
    if meals[i]<3:
        pit[i]='недостаточно'
    else:
        if meals[i]<7:
            pit[i]='достаточно'
        else:
            if meals[i]<11:
                pit[i]='избыток'

#for i in range(50): 
    #print(pit[i].rstrip("''"),end=',')
for i in range(50):
    if smoking[i]<1:
        sig[i]='норма'
    else:
        if smoking[i]<2:
            sig[i]='немного'
        else:
            if smoking[i]<7:
                sig[i]='избыток'
            else:
                if smoking[i]<101:
                    sig[i]='переизбыток'


for i in range(50):
    if sport[i]<1:
        zan[i]='недостаточно'
    else:
        if sport[i]<5:
            zan[i]='норма'
        else:
            if sport[i]<8:
                zan[i]='переизбыток'

                
for i in range(50):
    if lessons[i] <3:
        urok[i]='недостаточно'
    else:
        if lessons[i]<5:
            urok[i]='мало'
        else:
            if lessons[i]<8:
                urok[i]='норма'

for i in range(50):
    if sleep[i]<8:
        son[i]='недостаточно'
    else:
        if sleep[i]<10:
            son[i]='норма'
        else:
            if sleep[i]<12:
                son[i]='выше нормы'
            else:
                if sleep[i] <13:
                    son[i]='избыток'

for i in range(50):
    if pit[i]=='достаточно':
        health[i]+=1
    if sig[i]=='норма':
        health[i]+=1
    if zan[i]=='норма':
        health[i]+=1
    if son[i]=='норма':
        health[i]+=1


    if health[i]==0:
        zdor[i]='неуд.'
    else:
        if health[i]==1:
            zdor[i]='ниже ср.'
        else:
            if health[i]==2:
                zdor[i]='среднее'
            else:
                if health[i]<5:
                    zdor[i]='здоров'
                    
#for i in range(50):
    
    #print(pit[i].rstrip("''"),end=',')
    #print(sig[i].rstrip("''"),end=',')
    #print(zan[i].rstrip("''"),end=',')
    #print(son[i].rstrip("''"),end=',')
#i=1
#b=len(pit[i])
#print('пищ.в день    |',end='')
#print(pit[i],end=(12-b)*a+'|')

k=0
k1=13
print('Строим систему данных c семантикой:')
while k<50:
    print('Номер студента|',end=' ')
    for i in range(k,k1):#первые 13
        print(studentsNumber[i],end='  | ')#.rstrip('\n'))
    print()
    print('пищ.в день    |',end='')
    for i in range(k,k1):
            b=len(pit[i])
            print(pit[i],end=(12-b)*a+'|')
    print()
    print('сиг.в день    |',end='')
    for i in range(k,k1):
            b=len(sig[i])
            print(sig[i],end=(12-b)*a+'|')
    print()
    print('зан.спор.в нед|',end='')
    for i in range(k,k1):
            b=len(zan[i])
            print(zan[i],end=(12-b)*a+'|')
    print()
    print('посещ.зан.    |',end='')
    for i in range(k,k1):
        b=len(urok[i])
        print(urok[i],end=(12-b)*a+'|')
    
    print()
    print('время на сон  |',end='')
    for i in range(k,k1):
        b=len(son[i])
        print(son[i],end=(12-b)*a+'|')
    print()
    print('сост. здор.   |',end='')
    for i in range(k,k1):
        b=len(zdor[i])
        print(zdor[i],end=(12-b)*a+'|')
    print()
    print()
    print()

    k=k+13
    k1=k1+13
    if k==39:
        k1=50
    if k>39:
        break
    #if k>38:
      #  k=50
    

#print(zdor)











      
