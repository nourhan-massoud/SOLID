# Dependency Inversion Principle

# a). High level module should not depend on low level modules. Both should depend on abstractions
# b). Abstractions should not depend on details. Details should depend on abstractions.

# wrong (مينفعش الاعتماديه تكون بشكل مباشر ع كلاس ال جيميل و الهوتميل لازم يكون في وسيط)
# high level (parent or mail thing use it to send email)
# ال نوتيفيكشن كلاس بتعتمد او بتستخدم ال جيميل و ال هوتميل كلاس
# المشكله : لو غيرت في ال جيميل او اضيف مثلا كده هغير في ال نوتفكيشن 
# ف كده ال نوتفكيشن كلاس مش كلوزد و جه غلط !!ocd
# 

# high level
class notification():
    self.gmailObj
    self.hotmailObj
    

# low level
class gmail():
    def send(self):
        pass

class hotmail():
    def send(self):
        pass    

# -----------------------------------------------------

# high level
class notification():
    pass
    # use interface IMessage (abistraction level)
    # لازم ال هاي ليفيل ميعتمدش ع ال لو ليفل ولكن يعتمد ع ال ابستراكشن ليفيل
