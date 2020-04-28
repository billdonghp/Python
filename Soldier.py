'''
  多态
'''

class Soldier():
    def attack(self):
        print("军人进攻")
    def defend(self):
        print("军人防守")


class Master(Soldier):
    def attack(self):
        print("法师进攻")
    def defend(self):
        print("法师防守")


class Cavalry(Soldier):
    def attack(self):
        print("骑兵进攻")
    def defend(self):
        print("骑兵防守")

class Archer(Soldier):
    def attack(self):
        print("箭手进攻")
    def defend(self):
        print("箭手防守")


if __name__ == '__main__':
    m = Master()
    c = Cavalry()
    a = Archer()

    kingsArmy = []
    kingsArmy.append(m)
    kingsArmy.append(c)
    kingsArmy.append(a)

    cmd = input("国王，请下命令吧\n")

    if cmd == '99':
        for s in kingsArmy:
            s.attack()
    elif cmd == '00':
        for s in kingsArmy:
            s.defend()
    elif cmd == '11':
        for s in kingsArmy:
            if  isinstance(s,Cavalry):
                s.attack()
            else:
                s.defend()
    else:
        print("你说的啥玩儿啊!")
