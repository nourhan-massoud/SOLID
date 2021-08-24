# Interface Segregation Principle
# -------------------------------
# The Interface Segregation Principle states that “No client should be forced to depend on methods it does not use”.

# The Interface Segregation Principle suggests creating smaller interfaces known as “role interfaces” instead of a large interface consisting of multiple methods. 
# By segregating the role-based methods into smaller role interfaces, the clients would depend only on the methods that are relevant to it.

# wrong behavior
class Printer():
    def only_print(self):
        pass

    def only_scan(self):
        pass

    def only_fax(self):
        pass

# if another developer use or inhert from Printer class for new class named EchoPrinter()
# this new class should print only
# if use main class (Printer) this new class(EchoPrinter) will forced to depend on methods it does not use(scan-fax)
# that make Interface Segregation Principle broken !

# Right behavior
class IPrinter():
    pass

class IScaner():
    pass

class IFax():    
    pass

# if create new class named EchoPrinter - SuperPrinter inherit
class EchoPrinter():
    # use IPrinter only
    pass

class SuperPrinter():
    # use IPrinter - IScaner - IFax
    pass

# Interface Segregation و Liskov Substitution ايه الفرق بين 
#  فعلا الاتنين قريبين جدا من بعض علشان انت شايف ان ف الاخر انا بفصل وبحل المشكلة 
# اه الاتنين بيتحلوا بالفصل بس الفرق ف المعتقدات ما بينهم 
# ---------------------------------------------------------------------
# entities(Perent and Child)
# في ال Liskov بيقول لازم ال تشايلد يقدر يحل محل ال بيرنت 
# يعني مينفعش يتحط في موقف انه يحل محله و ميعرفش 
# ----------------------------------------------------------------------
# في ال Interface
# لازم انا ك بيرنت احترم احتياج ال تشايلد و مفرضش عليهم حاجه مش عايزنها 