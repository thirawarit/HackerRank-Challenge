if '__main__' == __name__:
    class TestSys:
        attri_1 = int()
        attri_2 = int()
        def callname(self, name , year):
            print("The name of the school is :", name, "that has been :", year, "years")
        def schname():
            print(TestSys.attri_1)

    school = TestSys()
    a = 'test'
    school.callname('BEN', 120)
    
    TestSys.attri_1 = 200
    TestSys.schname()