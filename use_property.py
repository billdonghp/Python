'''绑定属性时，如果直接把属性暴露出来，虽然写起来简单，
但是没有办法检查参数，导致可以随便更改
@property可以把一件getter方法变成属性，@property又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,val):
        if not isinstance(val,int):
            raise ValueError('score must be integer')
        if val < 0 or val >100:
            raise ValueError('score must between 0 ~ 100')
        self._score=val



        
##s = Student()
##s.score = 60
##print('s_score:',s.score)
