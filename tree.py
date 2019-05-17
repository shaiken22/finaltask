class MyTrie(object):
    def __init__(self):
        self.root = Node(None, 0)

    def insert(self,word):
        """Insert word into the tree"""
        self.root.insert(word)
        self.root._updateFreq()
        
    def search(self,word):
        """find given *word* in tree, if not occures False is returned"""
        return self.root.search(word)
 
    def printMaxFreq(self):
        """print all the prefixes with given prefix *pref*, with the maximum frequency"""
        self.root.printMaxFreq()

    @property
    def children(self):
        return self.root.children
    
    

class Node(object):
    def __init__(self, val, cnt = 1):
        self.__value = val
        self.__children = []
        self.__count = cnt
    
    @property
    def value(self):
        return self.__value

    @property
    def count(self):
        return self.__count
    
    @property
    def children(self):
        return [x for x in self.__children]
    
    def _updateFreq(self):
        self.__count += 1

    def add_child(self,value,early_child=False):
        if early_child:
            tmpt = Node(value)
            tmpt.__count -= 1
            self.__children.append(tmpt)
        else:
            self.__children.append(Node(value))
        self.__children.sort()
    
    def insert(self,word):
        if len(word)>1:
            s = word[0]
            word = word[1:]
            for c in self.children:
                if c.has_value(s):
                    c._updateFreq()
                    c.insert(word)
                    break
            else:
                self.add_child(s,True)
                self.insert(s+word)
        else:
            s = word
            for c in self.children:
                if c.has_value(s):
                    c._updateFreq()
                    break
            else:
                self.add_child(s)

    def has_value(self,letter):
        return self.__value == letter

    def search(self,word):
        nbr = 0
        node = self
        while nbr!=None:
            try:
                s = word[0]
            except IndexError:
                if node.count==sum([n.count for n in node.children]):
                    nbr=None
                break
            word = word[1:]
            for c in node.children:
                nbr+=c.count
                if c.has_value(s):
                    sumleft = sum([n.count for n in c.children])
                    if c.count!=sumleft:
                        nbr+= c.count-sumleft
                    nbr -= c.count
                    node = c
                    break
                else:
                    nbr=None
            if len(node.children)<=0:
                break
        if nbr!=None and len(word)>0:
            return False

        if nbr==None:
            return False
        else:
            return True

    def printMaxFreq(self):
        node = self
        prefidx = 0

        q = node.children
        mx = -1

        while len(q) != 0:
            cur = q.pop()
            mx = max(mx, cur.count)
            q += cur.children

        q = node.children
        res = []
        x = ''

        for curr in q:
            x = ''
            cur = curr
            while(cur.count == mx):
                x += cur.__value
                res.append(x)

                if len(cur.children) == 0:
                    break
                else:
                    cur = cur.children[0]

        for i in range(len(res) - 1):
            print(res[i], end=', ')
        print(res[-1])

    def __gt__(self, node2):
        return self.__value > node2.value
    