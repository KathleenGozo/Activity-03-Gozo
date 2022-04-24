class lei():
    def hpcal(bas,iv,ev,LVL):
        return ((2*bas+iv+(ev/4)*LVL)/100)+LVL+10

    def otherstat(bas,iv,ev,LVL):
        return ((((2*bas+iv+(ev/4))*LVL)/100)+5)*1.0