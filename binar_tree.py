class Node: # это класс узла/вершины
    def __init__(self,data):
        self.data = data
        self.left = self.right = None


class Tree: # это класс дерева из вершин
    def __init__(self):
        self.root = None # по кд корень пустой



    def __find(self,node,parent,value):# здесь мы ищем конерктный узел

        if node is None: #если корень пустой
            return None , parent, False

        if value == node.data:
            return node, parent, True # если нашли узел

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node,parent,False #если узла не существует



    def append(self, object):
        if self.root is None: # назначение корня (главной вершины)
            self.root = object
            return object

        son , parent , flag_find = self.__find(self.root,None,object.data)

        if not flag_find and son: # в случае если узла нет то мы добовляем его
            if object.data < son.data:
                son.left = object
            else:
                son.right = object
        return object




    def show_wide_tree(self,node):
        if node is None:
            return

        vershi = [node]

        while vershi:
            vershi_node = []

            for x in vershi:
                print(x.data,end=" " )
                if x.left:
                    vershi_node += [x.left]
                if x.right:
                    vershi_node += [x.right]
            print()
            vershi = vershi_node




    def show_tree(self,node ):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def __del_leaf(self,son,parent):

        if parent.left == son:
            parent.left = None

        if parent.right == son:
            parent.right = None



    def __del_one_child(self,son,parent):
        if parent.left == son:
            if son.left is None:
                parent.left = son.right
            if son.right is None:
                parent.right = son.left
        if parent.right == son:
            if son.left is None:
                parent.right = son.right
            if son.right is None:
                parent.right = son.left

    def __find_min(self,node,parent):
        if node.left:
            return self.__find_min(node.left,node)

        return node, parent



    def del_node(self, key):
        son, parent, flag_find = self.__find(self.root,None,key)

        if not flag_find:
            return None

        if son.left is None and son.right is None:
            self.__del_leaf(son,parent)

        elif son.left is None or son.right is None:
            self.__del_one_child(son,parent)

        else:
            son_right, parent_right = self.__find_min(son.right,son)
            son.data = son_right.data
            self.__del_one_child(son_right,parent_right)



boshki = [10,5,7,16,13,2,20]

dyb = Tree()

for x in boshki:
    dyb.append(Node(x))
#dyb.del_node(20)

dyb.show_wide_tree(dyb.root)
