"""Project with Polinomial creata by linked lists"""
class Mono:
    """Class to describe to define one monomial"""
    def __init__(self,coefficient,degree,nex=None) -> None:
        """takes main parametrs"""
        self.coefficient=coefficient
        if coefficient==0:
            self.degree=0
        else:
            self.degree=degree
        self.next=nex
    def __eq__(self, __value: object) -> bool:
        """compares two examples of class"""
        if not isinstance(__value,Mono):
            return False
        return self.coefficient==__value.coefficient and self.degree==__value.degree
    def __str__(self) -> str:
        """Print main information"""
        if self.coefficient>1 or self.coefficient<-1:
            if self.degree>1:
                return f"Mono: {self.coefficient}x**{self.degree}"
            if self.degree==1:
                return f"Mono: {self.coefficient}x"
            return f"Mono: {self.coefficient}"
        if self.coefficient==1:
            if self.degree>1:
                return f"Mono: x**{self.degree}"
            if self.degree==1:
                return "Mono: x"
            return "Mono: 1"
        if self.coefficient==-1:
            if self.degree>1:
                return f"Mono: -x**{self.degree}"
            if self.degree==1:
                return "Mono: -x"
            return "Mono: -1"
        return "Mono: 0"
    def __repr__(self) -> str:
        """print main information in lists"""
        return f'Mono(coeff={self.coefficient}, degree={self.degree})'
class Polynomial:
    """Class to describe polynomial by linkedlists with mono clasess"""
    def __init__(self,*args) -> None:
        """function takes main parametres"""
        if not args:
            self.head=Mono(0,0)
        else:
            link=None
            degree=0
            for i in args[::-1]:
                if isinstance(i,Polynomial):
                    opp=reverse(i.head)
                    while opp is not None:
                        new=Mono(opp.coefficient,opp.degree)
                        new.next=link
                        link=new
                        opp=opp.next
                else:
                    if i.degree>degree:
                        degree=i.degree
                    new=Mono(i.coefficient,i.degree)
                    new.next=link
                    link=new
            self.head=new
            self.degree=degree
    def __str__(self) -> str:
        """print main information"""
        st=""
        if self.head.coefficient==0 and self.head.next==None:
            return "Polynomial: 0"
        temp=self.head
        while temp is not None:
            if temp.coefficient>0:
                st+="+"+str(temp)[6:]
            elif temp.coefficient==0:
                temp=temp.next
                continue
            else:
                st+=str(temp)[6:]
            temp=temp.next
        if st and st[0]=="+":
            return "Polynomial: "+st[1:]
        return "Polynomial: "+st
    def __repr__(self) -> str:
        """print main information in lists"""
        st="Polynomial("
        temp=self.head
        while temp is not None:
            st+=repr(temp)+" -> "
            temp=temp.next
        return st[:-4]+")"
    def copy(self):
        """create copy of Polynomial"""
        return Polynomial(self)
    def sort(self):
        """sort Polynomial by degree of mono"""
        head=self.head
        link=None
        while head is not None:
            minimun_deg=head.degree
            minimun_cof=head.coefficient
            itt=head
            while itt is not None:
                if itt.degree<=minimun_deg:
                    minimun_deg=itt.degree
                    minimun_cof=itt.coefficient
                itt=itt.next
            find=Mono(minimun_cof,minimun_deg)
            place=head
            previous=None
            while place.coefficient!=find.coefficient or place.degree!=find.degree:
                previous=place
                place=place.next
            if previous:
                previous.next=place.next
            else:
                head=place.next
            new=Mono(minimun_cof,minimun_deg,link)
            link=new
        self.head=new
    def simplify(self):
        """Add all mono with same degree"""
        head=self.head
        ff=head
        while ff is not None:
            degree=ff.degree
            past=ff
            pp=ff.next
            while pp is not None:
                if pp.degree==degree:
                    ff.coefficient+=pp.coefficient
                    past.next=pp.next
                elif pp.coefficient==0:
                    past.next=pp.next
                else:
                    past=pp
                pp=pp.next
            ff=ff.next
        self.head=head
    def eval_at(self,num):
        """ evalueta Polynonomial if x==numerate"""
        new=self.head
        total=0
        while new is not None:
            total+=num**new.degree*new.coefficient
            new=new.next
        return total
    def __eq__(self, value: object) -> bool:
        """compares two Polynomial"""
        if isinstance(value,Polynomial):
            return self.eval_at(0)==value.eval_at(0) and self.eval_at(1)==value.eval_at(1)\
 and self.eval_at(10)==value.eval_at(10)
        return self.eval_at(0)==value
    def __hash__(self) -> int:
        """allow add polynomial to set"""
        return self.eval_at(0)
    @property
    def derivative(self):
        """will return a new polynomial that is the derivative
of the original, using the power rule."""
        new=Polynomial(self)
        past=None
        pp=new.head
        while pp is not None:
            if pp.degree>0:
                pp.coefficient*=pp.degree
                pp.degree-=1
            else:
                past.next=pp.next
            past=pp
            pp=pp.next
        new.simplify()
        return new
    def __add__(self,value):
        """add two Polynomial"""
        frst=Polynomial(self)
        scnd=Polynomial(value)
        frst.simplify()
        scnd.simplify()
        head=frst.head
        while head is not None:
            half_head=scnd.head
            while half_head is not None:
                if half_head.degree==head.degree:
                    head.coefficient+=half_head.coefficient
                half_head=half_head.next
            head=head.next
        return frst
    def __sub__(self,value):
        """subtracts two polynomial"""
        frst=Polynomial(self)
        scnd=Polynomial(value)
        frst.simplify()
        scnd.simplify()
        head=frst.head
        while head is not None:
            half_head=scnd.head
            while half_head is not None:
                if half_head.degree==head.degree:
                    head.coefficient-=half_head.coefficient
                half_head=half_head.next
            head=head.next
        return frst
    def __mul__(self,value):
        """multiplies two polynomial"""
        new=Mono(0,0)
        head=self.head
        if isinstance(value,Polynomial):
            while head is not None:
                half_head=value.head
                while half_head is not None:
                    new=Polynomial(Mono(head.coefficient*half_head.coefficient,\
head.degree+half_head.degree),new)
                    half_head=half_head.next
                head=head.next
            new.simplify()
            new.sort()
            return new
        while head is not None:
            new=Polynomial(Mono(head.coefficient*value,\
head.degree),new)
            head=head.next
        new.simplify()
        new.sort()
        return new
    def __rmul__(self,other):
        """multiplies two polynomial"""
        return self*other

def reverse(head:Mono):
    """function to reverse linked list"""
    new=None
    link=None
    while head is not None:
        new=Mono(head.coefficient,head.degree,link)
        link=new
        head=head.next
    return new
