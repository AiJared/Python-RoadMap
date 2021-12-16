names = ['Symon', 'Vicky',['Frankline', 'Tonny',['Joseph','Ann']]]
names2 = ['Emmanuel','Jared',['Frank','Irene',['Patterson','Bruno'],'Peter']]
names.extend(names2[2][2])
print(names)
names.insert(3,names2[2][3])
names[2].index('Tonny')
print(names.insert(names[2].index('Tonny'), names2[2][2][1]))