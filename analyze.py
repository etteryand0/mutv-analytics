from bs4 import BeautifulSoup # for parsing
import requests # for GET request
import sys # for abort

class Parser():
  def __init__(self, method,results):
    self.method_decp = {2:'Достижения',3:'Математика',4:'Естествознание',5:'Английский язык',6:'Итоги'}
    self.oldresults = results
    self.results = results # global results
    link = 'http://arctic-school.com/exam7-8-results/exam-class%s/' # template of the link
    for classroom in [7,8]: # do for 7th and 8th classrooms
      response = requests.get(link % classroom).text # GET html
      self.parse(response,method) # parse
      if classroom == 7:
          self.results7 = self.results
          self.students7 = self.students
      else:
          self.results8 = self.results
      
      self.results = results # reset results
    self.sort_info()
    print(self.achiev7)
    self.output()
  
  def output(self):
    from dicts import Dicts
    Dict = Dicts()
    self.math7 = Dict.math7
    self.achiev7 = Dict.achiev7
    self.summary7 = Dict.summary7
    self.math8 = Dict.math8
    self.achiev8 = Dict.achiev8
    self.summary8 = Dict.summary8
    print(self.students7)
    self.output = '7 класс - {0} \n'.format(str(self.students7))
    subjects = []
    try:
      subjects.append(self.achiev7)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.math7)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.science7)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.english7)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.summary7)
    except AttributeError as e:
      print(e)

    for subject in subjects:
      for key in subject:
        if key == 'title':
          self.output += subject[key] + '\n'
        else:
          if subject[key] != 0 or key == 'худшая': 
            self.output += 'Оценка \"'+key + '\" - ' + str(subject[key]) + '\n'
      self.output += '\n'
    self.output += '\n\n8 класс {0} \n'.format(str(self.students))
    subjects = []
    try:
      subjects.append(self.achiev8)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.math8)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.science8)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.english8)
    except AttributeError as e:
      print(e)
    try:
      subjects.append(self.summary8)
    except AttributeError as e:
      print(e)

    for subject in subjects:
      for key in subject:
        if key == 'title':
          self.output += subject[key] + '\n'
        else:
          if subject[key] != 0 or key == 'худшая':
            self.output += 'Оценка \"'+key + '\" - ' + str(subject[key]) + '\n'
      self.output += '\n'
    print(self.output)




  def sort_info(self):
      print('sort_info()')
      i = 6
      for classroom in [self.results7,self.results8]:
        print('for classroom in self.results')
        i += 1
        for method in self.method:
            if method == 6:
              subject = {'title':'','0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'20':0,'21':0,'22':0,'23':0,'24':0,'25':0,'худшая':0,'лучшая':0,'средняя':0}
            elif method == 2:
              subject = {'title':'','0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'худшая':0,'лучшая':0,'средняя':0}
            else:
              subject = {'title':'','0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'худшая':0,'лучшая':0,'средняя':0} 
            try:
                print('after subject assign')
                print(self.achiev7)
            except:
                print()
            print('{0}, {1}, {2}, {3}'.format(str(method), str(i), subject, '\n'))
            average,worst,best = 0, 5, 0
            z = 0
            for score in classroom[str(method)]:
              try:
                if z == 0 and i == 7:
                  print('after score assign')
                  print(self.achiev7)
              except:
                print()
              z+=1
              score = int(score)
              average += score
              if score < worst:
                worst = score
              if score > best:
                best = score
              
              subject[str(score)] += 1

              subject['худшая'] = worst
              subject['лучшая'] = best
              if i == 7 and z == self.students7:
                print('even before average')
                try:
                  print(self.achiev7)
                except:
                  print('error')
                subject['средняя'] = round(average/self.students7,2)
                if method == 2:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                    f.write('\n    self.achiev7 = %s' % subject)
                  self.achiev7 = subject
                elif method == 3:
                  #print('math called')
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                    f.write('\n    self.math7 = %s' % subject)
                  print('Before amth assign')
                  print(self.achiev7)
                  self.math7 = subject
                elif method == 4:
                  subject['title'] = self.method_decp[method]
                  with open ('dicts.py','a') as f:
                    f.write('\n    self.science7 = %s' % subject)
                  self.science7 = subject
                elif method == 5:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                    f.write('\n    self.english7 = %s' % subjrct)
                  self.english7 = subject
                elif method == 6:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                    f.write('\n    self.summary7 = %s' % subject)
                  self.summary7 = subject
                print(self.achiev7)
              elif i == 8 and z == self.students: # i = 8
                subject['средняя'] = round(average/self.students,2)
                if method == 2:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                      f.write('\n    self.achiev8 = %s' % subject)
                  self.achiev8 = subject
                elif method == 3:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                      f.write('\n    self.math8 = %s' % subject)
                  self.math8 = subject
                elif method == 4:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                      f.write('\n    self.science8 = %s' % subject)
                  self.science8 = subject
                elif method == 5:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                      f.write('\n    self.english8 = %s' % subject)
                  self.english8 == subject
                elif method == 6:
                  subject['title'] = self.method_decp[method]
                  with open('dicts.py','a') as f:
                      f.write('\n    self.summary8 = %s' % subject)
                  self.summary8 = subject



  def parse(self,response,method):
      table = BeautifulSoup(response,'html.parser').find('table') # find table
      trs = table.find_all('tr')[1:] # find all tr
      if len(method) > 1: # if input method is 1
          method = [x+1 for x,i in enumerate(trs[0].find_all('td')) if i.text != ''][1:] # delete empty td from list
          oldresults = self.oldresults
          for i in method: # pop unnecessary items
              oldresults = list(oldresults)
              if str(i) in oldresults:
                  oldresults.remove(str(i))

          for i in oldresults:
            self.results.pop(i)
      self.method = method
      self.students = len(trs) # len of students for average score
      
      # • PARSE • #
      print()
      for tr in trs:
        tr = tr.find_all('td')
        for i in method:
          self.results[str(i)].append(tr[i-1].text)





print('1 - everything\n2 - achievments\n3 - math\n4 - science\n5 - english\n6 - summary')

method = int(input(str('choice: ')))

with open('dicts.py','w') as f:
    f.write('class Dicts():\n  def __init__(self):')
    f.close()

if method not in [1,2,3,4,5,6]:
    sys.exit('\x1b[31minvalid mode\x1b[0m')
elif int(method) == 1:
    method = [2,3,4,5,6]
    results = {'2':[],'3':[],'4':[],'5':[],'6':[]}
else:
    results = {str(method):[]}
    method = list(method)

Parser = Parser(method,results)

print('@mutv\nБот статистика mutv')
