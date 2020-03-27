#HW3
#Due Date: 03/27/2020, 11:59PM 
########################################
#                                      
# Name:Kaelan Wright
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return True
        else:
            return False



    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        temp = Node(value)
        temp.next = self.top
        self.top = temp
        self.count += 1

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return
        else:
            removed_value = self.top.value
            self.top = self.top.next
            self.count -= 1
            return removed_value

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return None
        else:
            return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except ValueError:
            return False



    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing. Follow PEMDAS
            >>> x=Calculator()
            >>> x._getPostfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('(2.5)')
            '2.5'
            >>> x._getPostfix ('((2))')
            '2.0'
            >>> x._getPostfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 *    5   +   3    ^ -2       +1  +4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            >>> x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')
        '''
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfix_Stack=Stack()
        # YOUR CODE STARTS HERE
        #This code sets up the structure for processing the string
        operator = ["*","/","+","-","^"]
        operator_stack = Stack()
        failure_test_a = False
        failure_test_b = False
        digit_stack=Stack()
        #This code removes whitespace
        txt = " ".join(txt.split())
        #This code converts any ** exponents to ^
        for i in range(len(txt)-1):
            if txt[i] is "*" and txt[i+1] is "*":
                txt[i]="^"
        #This code checks paranthases
        if txt.count("(") is not txt.count(")"):
            return None
        #This code stacks the string
        for i in range(len(txt)):
            postfix_Stack.push(txt[i])
        #This code checks for the double operator error
        while postfix_Stack.count is not 0:
            a = postfix_Stack.pop()
            for j in range(len(operator)):
                if postfix_Stack.peek is operator_stack.peek() and a is operator[j]:
                    return None
                if a is operator[j]:
                    operator_stack.push(a)
                #This code splits the digits into a seperate stack
                elif self.isNumber(a) is True:
                    digit_stack.push(float(a))

        # this breaks the 2 case up
        #case 1
        if txt.count("(") is 0:
            for i in range(len(operator_stack)):
                a = operator_stack.pop()
                postfix_Stack.push(a)
            for i in range(digit_stack.count):
                a = digit_stack.pop()
                postfix_Stack.push(a)
        #case 2
        else:
            print("not ready yet")
        #Final string formatting
        string = []
        for i in range(len(postfix_Stack)):
            string.append(str(postfix_Stack.pop()))
        final_string = " ".join(string)
        return final_string


















                





        


    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('    4  +      3 -2')
            >>> x.calculate
            5.0
            >>> x.setExpr('  2  +3.5')
            >>> x.calculate
            5.5
            >>> x.setExpr('4+3.65-2 /2')
            >>> x.calculate
            6.65
            >>> x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('   2   - 3         *4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 *   (        ( (10 - 2*3)))')
            >>> x.calculate
            12.0
            >>> x.setExpr(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
            >>> x.calculate
            -2.0
            >>> x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr("4++ 3 +2") 
            >>> x.calculate
            >>> x.setExpr("4    3 +2")
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*(2 - 3*2)) ')
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*/(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(')2(*10 - 3*(2 - 3*2) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        # YOUR CODE STARTS HERE

