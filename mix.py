from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty,NumericProperty,StringProperty
from kivy.uix.widget import Widget
from kivy.properties  import ObjectProperty
import random
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-VLE1SI35;Database=Project;Trusted_Connection=yes; ')
cursor = conn.cursor()

Builder.load_string("""
#: import CheckBox kivy.uix.checkbox
<CustomPopup>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "TRANSACTION FAILED"
        on_press: root.dismiss()
<CustomPopup1>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "INVALID USERNAME OR PASSWORD"
        on_press: root.dismiss()
<CustomPopup2>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "INVALID CARD NUMBER OR CVV"
        on_press: root.dismiss()
<CustomPopup3>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "INSUFFICIENT AMOUNT"
        on_press: root.dismiss()
<CustomPopup4>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "PLEASE ENTER THE VALUES"
        on_press: root.dismiss()  
<CustomPopup5>:
    size_hint: .5,.5
    auto_dismiss:False
    title: "The Popup"
    Button:
        text: "SUCCESSFUL"
        on_press: root.dismiss()             
<CustLabel@Label>
    color: 1, 1, 1, 1
<SampBoxLayout>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel:
            text: "Select Payment Method"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.8
    
        CheckBox:
            id: debit_input
            font_size: 20
            group: "select_payment"
            value: root.DebitCard
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            height: 35
            width: 300
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"
        CustLabel:
            id: debit_label
            text: "Debit Card"
            font_size: 30
            right: debit_input.x + 60
            center_y: root.top * 0.6
    
        CheckBox:
            id: credit_input
            font_size: 20
            group: "select_payment"
            value: root.CreditCard
            center_x: root.width * 0.5
            center_y: root.top * 0.5
            height: 35
            width: 300
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_three"
        CustLabel:
            id: credit_label
            text: "Credit Card"
            font_size: 30
            right: credit_input.x + 60
            center_y: root.top * 0.5
        CheckBox:
            id: netbank_input
            font_size: 20
            group: "select_payment"
            value: root.NetBanking
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            height: 35
            width: 300
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_four"
        CustLabel:
            id: netbank_label
            text: "NetBanking"
            font_size: 30
            value: root.NetBanking
            right: netbank_input.x + 60
            center_y: root.top * 0.4
            
<LoginScreen>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Login"
            color: (0,0,0,1)
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.8
        Label:
            id: username_label
            text: "Username"
            color: (0,0,0,1)
            font_size: 30
            right: username_input.x - 60
            center_y: root.top * 0.6
        TextInput:
            id: username_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            height: 35
            width: 300
        Label:
            id: password_label
            text: "Password"
            color: (0,0,0,1)
            font_size: 30
            right: password_input.x - 60
            center_y: root.top * 0.5
        TextInput:
            id: password_input
            font_size: 20
            password: True
            center_x: root.width * 0.5
            center_y: root.top * 0.5
            height: 35
            width: 300
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: password_input.y - 102
            text: "login"
            size: (150,100)
            on_press: 
                root.login()
                

<CustLabel1@Label>:
    color: (0,0,0,1)

<DebitCard>:
    Widget:
    
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel1:
            text: "DEBIT CARD"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.8
        CustLabel1:
            id: CardNumber_label
            text: "Card Number"
            font_size: 30
            right: CardNumber_input.x - 60
            center_y: root.top * 0.6
        TextInput:
            id: CardNumber_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            height: 35
            width: 300
        CustLabel1:
            id: ExpireDate_label
            text: "Expire Date"
            font_size: 30
            right: ExpireDate_input.x - 60
            center_y: root.top * 0.5
        TextInput:
            id: ExpireDate_input
            font_size: 20
            text: "MM"
            on_touch_down:
                self.text = ""
            center_x: root.width * 0.4
            center_y: root.top * 0.5
            height: 35
            width: 100
        TextInput:
            id: ExpireDate_input1
            font_size: 20
            text: "YY"
            on_touch_down:
                self.text = ""
            center_x: root.width * 0.6
            center_y: root.top * 0.5
            height: 35
            width: 100
        CustLabel1:
            id: CVV_label
            text: "CVV"
            font_size: 30
            right: CVV_input.x - 60
            center_y: root.top * 0.4
        TextInput:
            id: CVV_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            height: 35
            width: 300
    
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: CVV_input.y - 102
            text: "Pay"
            size: (150,100)
            on_press:
                root.debit_pay()


<CreditCard>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (1,1,1,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel1:
            text: "CREDIT CARD"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.8
        CustLabel1:
            id: CardNumber_label
            text: "Card Number"
            font_size: 30
            right: CardNumber_input.x - 60
            center_y: root.top * 0.6
        TextInput:
            id: CardNumber_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            height: 35
            width: 300
        CustLabel1:
            id: ExpireDate_label
            text: "Expire Date"
            font_size: 30
            right: ExpireDate_input.x - 60
            center_y: root.top * 0.5
        TextInput:
            id: ExpireDate_input
            font_size: 20
            text: "MM"
            on_touch_down:
                self.text = ""
            center_x: root.width * 0.4
            center_y: root.top * 0.5
            height: 35
            width: 100
        TextInput:
            id: ExpireDate_input1
            font_size: 20
            text: "YY"
            on_touch_down:
                self.text = ""
            center_x: root.width * 0.6
            center_y: root.top * 0.5
            height: 35
            width: 100
        CustLabel1:
            id: CVV_label
            text: "CVV"
            font_size: 30
            right: CVV_input.x - 60
            center_y: root.top * 0.4
        TextInput:
            id: CVV_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            height: 35
            width: 300
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: CVV_input.y - 102
            text: "Pay"
            size: (150,100)
            on_press:
                root.login_press()
                
<NetBanking>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        Spinner:
            text: "Select The Bank"
            values:["State Bank Of India","HDFC Bank","ICICI Bank","Axis Bank","Punjab National Bank"]
            id: spinner_id
            center_x: root.width * 0.5
            center_y: root.top  * 0.7
            size: (250,100)
            on_text: root.spinner_clicked(spinner_id.text)
    
        Button:
            id: select_bank
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            text: "Pay"
            size: (150,100)
            on_press:
                root.login_press()
                

<Transaction>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel:
            text: "MAKE PAYMENT"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.9
        CustLabel:
            id: payfrom_label
            text: "Pay From:"
            font_size:30
            right: payfrom_input.x - 60
            center_y: root.top * 0.7
        Spinner:
            text: "--Select Account-- "
            values:[root.acount_no]
            id: payfrom_input
            center_x: root.width * 0.5
            center_y: root.top  * 0.7
            size: (300,40)
            on_press:on_text: root.spinner_clicked()
        CustLabel:
            id:payto_label
            text: "Pay To:"
            font_size:30
            right: payto_input.x - 49
            center_y: root.top * 0.6
        TextInput:
            id: payto_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:amountpay_label
            text: "Amount Pay To:"
            font_size:30
            right: amountpay_input.x - 70
            center_y: root.top * 0.5
        TextInput:
            id: amountpay_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.5
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:remark_label
            text: "Remark:"
            font_size:30
            right: remark_input.x - 60
            center_y: root.top * 0.4
        TextInput:
            id: remark_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            multiline: True
            height: 35
            width: 300
        Button:
            id: otp_label
            font_size: 20
            right: remark_input.x - 60
            center_y: root.top * 0.3
            text: root.generated_otp
            size: (100,50)
            on_press:on_text: root.OTP()
        TextInput:
            id:otp_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.3
            multiline: True
            height: 35
            width: 300    
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: otp_input.y - 102
            text: "Pay"
            size: (150,100)
            on_press:root.transcation()

<TransactionDebit>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel:
            text: "MAKE PAYMENT"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.9
        
        CustLabel:
            id:payto_label
            text: "Pay To:"
            font_size:30
            right: payto_input.x - 49
            center_y: root.top * 0.7
        TextInput:
            id: payto_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.7
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:amountpay_label
            text: "Amount Pay To:"
            font_size:30
            right: amountpay_input.x - 70
            center_y: root.top * 0.6
        TextInput:
            id: amountpay_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:remark_label
            text: "Remark:"
            font_size:30
            right: remark_input.x - 60
            center_y: root.top * 0.5
        TextInput:
            id: remark_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.5
            multiline: True
            height: 35
            width: 300
        Button:
            id: login_button
            font_size: 20
            right: remark_input.x - 60
            center_y: root.top * 0.4
            text: root.generated_otp
            size: (100,50)
            on_press:on_text: root.OTP()
        TextInput:
            id:otp_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            multiline: True
            height: 35
            width: 300
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: otp_input.y - 102
            text: "Pay"
            size: (150,100)
            on_press:root.transcation()

<TransactionCredit>:
    Widget:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        CustLabel:
            text: "MAKE PAYMENT"
            font_size: 60
            center_x: root.width * 0.5
            center_y: root.top * 0.9
        
        CustLabel:
            id:payto_label
            text: "Pay To:"
            font_size:30
            right: payto_input.x - 49
            center_y: root.top * 0.7
        TextInput:
            id: payto_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.7
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:amountpay_label
            text: "Amount Pay To:"
            font_size:30
            right: amountpay_input.x - 70
            center_y: root.top * 0.6
        TextInput:
            id: amountpay_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.6
            multiline: False
            height: 35
            width: 300
        CustLabel:
            id:remark_label
            text: "Remark:"
            font_size:30
            right: remark_input.x - 60
            center_y: root.top * 0.5
        TextInput:
            id: remark_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.5
            multiline: True
            height: 35
            width: 300
        Button:
            id: otp_label
            font_size: 20
            right: remark_input.x - 60
            center_y: root.top * 0.4
            text: root.generated_otp
            size: (100,50)
            on_press:on_text: root.OTP()
        TextInput:
            id:otp_input
            font_size: 20
            center_x: root.width * 0.5
            center_y: root.top * 0.4
            multiline: True
            height: 35
            width: 300
        Button:
            id: login_button
            font_size: 20
            center_x: root.width * 0.5
            center_y: otp_input.y - 102
            text: "Pay"
            size: (150,100)
            on_press:root.transcation()
""")
selected_value=set()
a=[]
d=[]
cre=[]
net=[]
net_otp=[0]
deb_otp=[0]
cre_otp=[0]
popupmenu=set()
class LoginScreen(Screen):

    def login(self,*args):
        username = self.ids.username_input
        username_text = username.text
        password = self.ids.password_input
        password_text = password.text

        x=selected_value.pop()

        if x == 1:
            cursor.execute("SELECT  [Id],[UserName],[Password] FROM [Project].[dbo].[Debit_login]")
            c = 0
            de= d[0]
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                if username_text == row.UserName and password_text == row.Password and de==row.Id:
                    #a.append(row.UserName)
                    c = 1
                    print(a)
                    self.manager.transition.direction = "left"
                    self.manager.transition.duration = 1
                    self.manager.current = "screen_six1"
            if (c != 1):
                popupmenu.add(1)
                open_popup()

        if x==2:
            cursor.execute("SELECT  [Id],[UserName],[Password] FROM [Project].[dbo].[Credit_login]")
            c = 0
            cr = cre[0]
            print(cr)
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                if username_text == str(row.UserName) and password_text ==str(row.Password) and cr==row.Id:
                    #a.append(row.UserName)
                    c = 1
                    print(a)
                    self.manager.transition.direction = "left"
                    self.manager.transition.duration = 1
                    self.manager.current = "screen_six2"
            if (c != 1):
                popupmenu.add(1)
                open_popup()
        if x==3:
            cursor.execute("SELECT [Id],[UserName],[Password]FROM [Project].[dbo].[Net_login]")
            c=0
            while 1:
                row = cursor.fetchone()
                if not row:
                    break
                if username_text ==row.UserName  and password_text == row.Password :
                    a.append(row.UserName)
                    net.append(row.Id)
                    c = 1
                    print(a)
                    self.manager.transition.direction = "left"
                    self.manager.transition.duration = 1
                    self.manager.current = "screen_six"
            if(c!=1):
                popupmenu.add(1)
                open_popup()

        selected_value.add(x)



def open_popup():
    x1 = popupmenu.pop()
    if x1==1:
        the_popup = CustomPopup1()
        the_popup.open()
    if x1==2:
        the_popup = CustomPopup()
        the_popup.open()
    if x1==3:
        the_popup = CustomPopup2()
        the_popup.open()
    if x1==4:
        the_popup = CustomPopup3()
        the_popup.open()
    if x1==5:
        the_popup = CustomPopup4()
        the_popup.open()
    if x1==6:
        the_popup = CustomPopup5()
        the_popup.open()

class SampBoxLayout(Screen):
    checkbox_is_active = ObjectProperty(False)

    DebitCard = ObjectProperty(True)
    CreditCard = ObjectProperty(False)
    NetBanking = ObjectProperty(False)


class DebitCard(Screen):
    def debit_pay(self,*args):
        selected_value.add(1)
        cardnumber = self.ids.CardNumber_input
        cardnumber_text = cardnumber.text
        cvv = self.ids.CVV_input
        cvv_text = cvv.text
        print(type(cardnumber_text))
        print(cvv_text)
        cursor.execute("SELECT [Id],[DebitCardNo],[CVV] FROM [Project].[dbo].[Debit_login]")
        c=0
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            if cardnumber_text == str(row.DebitCardNo) and cvv_text == str(row.CVV):
                d.append(row.Id)
                c = 1
                print(d)
                self.manager.transition.direction = "left"
                self.manager.transition.duration = 1
                self.manager.current = "screen_five"
        if (c != 1):
            popupmenu.add(3)
            open_popup()



class CustomPopup(Popup):
    pass
class CustomPopup1(Popup):
    pass
class CustomPopup2(Popup):
    pass
class CustomPopup3(Popup):
    pass
class CustomPopup4(Popup):
    pass
class CustomPopup5(Popup):
    pass
class CreditCard(Screen):
    def login_press(self):
        selected_value.add(2)
        cardnumber = self.ids.CardNumber_input
        cardnumber_text = cardnumber.text
        cvv = self.ids.CVV_input
        cvv_text = cvv.text
        print(type(cardnumber_text))
        print(cvv_text)
        cursor.execute("SELECT [Id],[CreditCardNo],[CVV] FROM [Project].[dbo].[Credit_login]")
        c = 0
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            if cardnumber_text == str(row.CreditCardNo) and cvv_text == str(row.CVV):
                cre.append(row.Id)
                c = 1
                print(cre)
                self.manager.transition.direction = "left"
                self.manager.transition.duration = 1
                self.manager.current = "screen_five"
        if (c != 1):
            popupmenu.add(3)
            open_popup()

class NetBanking(Screen):
    def spinner_clicked(self, value):
        pass
    def login_press(self):
        spiiner1= self.ids.spinner_id
        spiiner1_text=spiiner1.text
        if spiiner1_text !="Select The Bank" :
            selected_value.add(3)
            self.manager.transition.direction = "left"
            self.manager.transition.duration = 1
            self.manager.current = "screen_five"

class Transaction(Screen):
    acount_no = StringProperty('')
    generated_otp = StringProperty('')
    def spinner_clicked(self, *args):
        x1=a[0]
        cursor.execute("SELECT [UserName],[AccountNo] FROM [Project].[dbo].[Net_login] ")
        while 1:
            row = cursor.fetchone()

            if not row:
                break
            if row.UserName==x1:
                x = row.AccountNo
                self.acount_no = str(x)

    def OTP(self, *args):
        otp = random.randint(100000, 999999)
        net_otp.append(otp)
        self.generated_otp = str(otp)
    def transcation(self):
        x1 = net[0]
        payfrom=self.ids.payfrom_input
        payfrom_text = payfrom.text
        payto=self.ids.payto_input
        payto_text=payto.text
        otp1 = net_otp[-1]
        otp=self.ids.otp_input
        otp_text=otp.text
        amount=self.ids.amountpay_input
        amount_text=amount.text

        cursor.execute("SELECT [Id],[Amount]FROM [Project].[dbo].[Net_login]")
        while 1:
            row = cursor.fetchone()

            if not row:
                break
            if row.Id ==x1 :
                x = row.Amount

        if payfrom_text!= '--Select Account--' and payto_text != "" and amount_text != "" and otp_text == str(otp1):

            amt = int(amount_text)
            print("hello")
            if(x>=amt):
                newAmount= x-amt
                print(newAmount)
                cursor.execute("UPDATE [Project].[dbo].[Net_login] SET Amount=? WHERE Id=? ", newAmount, x1)
                conn.commit()
                conn.close()
                popupmenu.add(6)
                open_popup()
                self.manager.transition.direction = "left"
                self.manager.transition.duration = 1
                self.manager.current = "screen_one"
            else:
                popupmenu.add(4)
                open_popup()
        else:
            popupmenu.add(5)
            open_popup()



class TransactionDebit(Screen):
    generated_otp = StringProperty('')

    def OTP(self, *args):
        otp = random.randint(100000, 999999)
        deb_otp.append(otp)
        self.generated_otp = str(otp)

    def transcation(self):
        x1 = d[0]
        payto = self.ids.payto_input
        payto_text = payto.text
        otp1 = deb_otp[-1]
        otp = self.ids.otp_input
        otp_text = otp.text
        amount = self.ids.amountpay_input
        amount_text = amount.text

        cursor.execute("SELECT [Id],[Amount] FROM [Project].[dbo].[Debit_login]")
        while 1:
            row = cursor.fetchone()

            if not row:
                break
            if row.Id == x1:
                x = row.Amount

        if payto_text != "" and amount_text != "" and otp_text == str(otp1):

            amt = int(amount_text)
            print("hello")
            if (x >= amt):
                newAmount = x - amt
                print(newAmount)
                cursor.execute("UPDATE [Project].[dbo].[Debit_login] SET Amount=? WHERE Id=? ", newAmount, x1)
                conn.commit()
                conn.close()
                popupmenu.add(6)
                open_popup()
                self.manager.transition.direction = "left"
                self.manager.transition.duration = 1
                self.manager.current = "screen_one"
            else:
                popupmenu.add(4)
                open_popup()
        else:
            popupmenu.add(5)
            open_popup()


class TransactionCredit(Screen):
    generated_otp = StringProperty('')

    def OTP(self, *args):
        otp = random.randint(100000, 999999)
        cre_otp.append(otp)
        self.generated_otp = str(otp)
    def transcation(self):
        x1 = cre[0]
        payto = self.ids.payto_input
        payto_text = payto.text
        otp1 = cre_otp[-1]
        otp = self.ids.otp_input
        otp_text = otp.text
        amount = self.ids.amountpay_input
        amount_text = amount.text

        cursor.execute("SELECT [Id],[Amount] FROM [Project].[dbo].[Credit_login]")
        while 1:
            row = cursor.fetchone()

            if not row:
                break
            if row.Id == x1:
                x = row.Amount

        if payto_text != "" and amount_text != "" and otp_text == str(otp1):

            amt = int(amount_text)

            if (x >= amt):
                newAmount = x - amt
                print(newAmount)
                cursor.execute("UPDATE [Project].[dbo].[Credit_login] SET Amount=? WHERE Id=? ", newAmount, x1)
                conn.commit()
                conn.close()
                popupmenu.add(6)
                open_popup()
                self.manager.transition.direction = "left"
                self.manager.transition.duration = 1
                self.manager.current = "screen_one"
            else:
                popupmenu.add(4)
                open_popup()
        else:
            popupmenu.add(5)
            open_popup()




screen_manager= ScreenManager()

screen_manager.add_widget(SampBoxLayout(name="screen_one"))
screen_manager.add_widget(DebitCard(name="screen_two"))
screen_manager.add_widget(CreditCard(name="screen_three"))
screen_manager.add_widget(NetBanking(name="screen_four"))
screen_manager.add_widget(LoginScreen(name="screen_five"))
screen_manager.add_widget(Transaction(name="screen_six"))
screen_manager.add_widget(TransactionDebit(name="screen_six1"))
screen_manager.add_widget(TransactionCredit(name="screen_six2"))

class MixApp(App):

    def build(self):
        return screen_manager


sample_app=MixApp()
sample_app.run()