def outermethod():
    class Node:
        def dis(self):
            class SubNode1:
                def __init__(self, data):
                    self.data = data

                def value(self):
                    return self.data

                class SubNode2:
                    def __init__(self, data):
                        self.data = data

                    def value(self):
                        return self.data

                    class SubNode3:
                        def __init__(self, data):
                            self.data = data

                        def value(self):
                            return self.data

                        class SubNode4:
                            def __init__(self, data):
                                self.data = data

                            def value(self):
                                return self.data

                            class SubNode5:
                                def __init__(self, data):
                                    self.data = data

                                def value(self):
                                    return self.data


            obj1 = SubNode1(data=8)
            obj2 = obj1.SubNode2(data=obj1.value())
            obj3 = obj2.SubNode3(data=obj2.value())
            obj4 = obj3.SubNode4(data=obj3.value())
            obj5 = obj4.SubNode5(data=obj4.value())
            return obj5.value()

    obj = Node()
    return obj.dis()


result = outermethod()
print(result)
