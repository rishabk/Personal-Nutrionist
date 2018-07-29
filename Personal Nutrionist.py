from tkinter import *
import tkinter
from fatsecret import Fatsecret
import webbrowser
import tkinter.messagebox as tkmessagebox

fs = Fatsecret("53d896611f274c93918b1ecfc3163e98", "53419fc7c2db4861b3360d0b7b89653f")


root=Tk()
root.geometry('800x800')
# root.attributes("-fullscreen" , True)

def enterDetails():
    global bmi, bmiLabel, b, n, a
    h=float(Height1.get())
    w=float(Weight1.get())
    n=Name1.get()
    a=int(Age1.get())
    hh=float(h*h)
    b = float(w/hh)
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    bmiLabel = Label(f1, text="Your BMI is : ", fg="yellow", font=("Arial", 25, "bold italic"), bg="#172c3e")
    bmiLabel.place(x=150, y=70)

    bmi = Label(f1, text=b, fg="yellow", font=("Arial", 25, "bold italic"), bg="#172c3e")
    bmi.place(x=380, y=70)
    break1=['BREAKFAST:','Fruit or fruit juice: 1 orange or 1 glass of orange juice',
            'Cereal with milk and sugar:1/2 cup of breakfast cereal or porridge,with ½ cup of full-cream milk and sugar',
            'LUNCH:','Roll with butter and cheese :1 whole-wheat roll or 2-3 whole-wheat biscuits with 2tbsp margarine and 30g of cheese',
            'Potato: 1 large potato or sweet potato,/rice/pasta',
            'AFTERNOON TEA:','Sandwiches with filling:2 slices of whole-wheat bread with 2 T peanut butter or cream cheese with chopped nuts or egg mayonnise',
            'SUPPER:','Fruit juice: 1 glass','Meat or fish or cheese or eggs :90 g portion or 1-2 eggs',
            'BEDTIME:','Milk drink: 1 cup of Milo or Ovaltine made with full-cream milk', 'Biscuits: 2-3 biscuits']
    break2=['BREAKFAST:','Banana:1 small','Whole-wheat bread:2 slices','LUNCH:','Chinese noodles:soft-type','1 chapati : 1 bowl of dal','Apple','1 tea : Unsweetened','DINNER:' ,'Broccoli : stir fry with vegetables',
            'Steamed brown rice : 1 cup']
    break3=['BREAKFAST:','4 idlis with 1 cup sambar and ¼ cup coconut chutney : 1 cup green tea + 4 almonds','LUNCH:','3 rotis : 1 serving white rice','1 cup dal : ½ cup mixed vegetable curry ',' chicken curry + 1 cup salad ',' 1 cup buttermilk: (after 20 min)',
            'DINNER:','3 rotis + ½ cup mixed vegetable curry','chickpeas/fish : ½ cup yogurt + ½ cup salad ',' 1 cup warm milk with a pinch of turmeric :before bed']
    break4=['BREAKFAST:','a plate of 2-3 idlis and sambar','MID-MORNING:','eat a cup of yogurt, half an apple, a handful of nuts ',
            'LUNCH:','a cup of cooked brown rice with a good vegetable curry','EVENING SNACK:','have a cup of milk and any fruit like watermelon','DINNER:','eat one roti without oil, half a cup of vegetable curry. Also, include a bowl of fruit or vegetable salad']
    num=280
    if (b<18.5):
        underweightlabel=Label(f1, text="You are underweight", fg="yellow", font=("Arial", 20, "bold"), bg="#172c3e")
        underweightlabel.place(x=250, y=180)
        for i in break1:
            dietlabel=Label(f1, text=i, fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
            dietlabel.place(y=num)
            num=num+30
            
        
    elif (b>=18.5 and b <24.9):
        normalweightlabel=Label(f1, text="Your weight is normal", fg="yellow", font=("Arial", 20, "bold"), bg="#172c3e")
        normalweightlabel.place(x=250, y=200)
        for i in break2:
            dietlabel=Label(f1, text=i, fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
            dietlabel.place(y=num)
            num=num+30

    elif (b>=24.9 and b<29.9):
        overweightlabel=Label(f1, text="You are overweight", fg="yellow", font=("Arial", 20, "bold"), bg="#172c3e")
        overweightlabel.place(x=250, y=200)
        for i in break3:
            dietlabel=Label(f1, text=i, fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
            dietlabel.place(y=num)
            num=num+30

    else:
        obeselabel=Label(f1, text="You are obese", fg="yellow", font=("Arial", 20, "bold"), bg="#172c3e")
        obeselabel.place(x=280, y=200)
        for i in break4:
            dietlabel=Label(f1, text=i, fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
            dietlabel.place(y=num)
            num=num+30
    theBack = Button(f1, text="BACK", command=Diet,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)
def Fooddesc():
    global foods
    global theLabelF
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)
    Efood = Label(f1, text="FOOD DESCRIPTION", fg="yellow", font=("Arial", 25, "bold italic"),bg="#172c3e")
    Efood.place(x=220, y=50)
    num=150
    foods = fs.foods_search(foodItem.get())
    for i in foods:
        label1=Label(f1, text=i['food_name'], fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
        label1.place(y=num)
        label2=Label(f1, text=i['food_description'], fg= 'white', font = ("Arial", 10, "bold italic"), bg="#172c3e")
        label2.place(x=210, y=num)
        num=num+25
    theBack = Button(f1, text="BACK", command=Detail,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

def Detail():
    global foodItem
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    Efood = Label(f1, text="Enter the food you want to search", fg="yellow", font = ("Arial", 25, "bold italic"), bg="#172c3e")
    Efood.place(x=150, y=80)

    foodItem = tkinter.Entry(f1, width=40,font = ("Arial", 15, "bold italic"))
    foodItem.place(x=180, y=300)

    theButton2 = Button(f1, text="CHECK", command=Fooddesc, font = ("Arial", 15, "bold italic"))
    theButton2.place(x=360, y=380)

    theBack=Button(f1, text= "BACK", command=menu,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

def Recipe():
    global recipes
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    Efood = Label(f1, text="Enter the recipe you want to search", fg="yellow", bg="#172c3e",font = ("Arial", 30, "bold italic"))
    Efood.place(x=100, y=80)

    theBack = Button(f1, text="BACK", command=menu,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

    foodItem2 = tkinter.Entry(f1, width=40,font = ("Arial", 15, "bold italic"))
    foodItem2.place(x=180, y=300)

    def reci():
        recipes=fs.recipes_search(foodItem2.get(), max_results=10, page_number=1)

        f2 = Frame(root, bg="#172c3e")
        f2.place(height=700, width=800, y=80)

        num = 150

        for i in recipes:
            label1 = Label(f2, text=i['recipe_name'], fg='white', font=("Arial", 10, "bold italic"), bg="#172c3e")
            label1.place(y=num)
            label2 = Label(f2, text=i['recipe_description'], fg='white', font=("Arial", 10, "bold italic"), bg="#172c3e")
            label2.place(x=210, y=num)

            def callback(event):
                webbrowser.open_new(i['recipe_url'])

            label3 = Label(f2, text="Get Recipe", fg='white', font=("Arial", 10, "bold italic"), bg="#172c3e", cursor="hand2")
            label3.place(x=700, y=num)
            label3.bind("<Button-1>", callback)
            num = num + 25

        theBack = Button(f1, text="BACK", command=Recipe,font = ("Arial", 15, "bold italic"))
        theBack.place(x=20, y=20)

    theButton2 = Button(f1, text="SEARCH", command=reci, font=("Arial", 15, "bold italic"))
    theButton2.place(x=360, y=380)

    theBack = Button(f1, text="BACK", command=menu,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

def Diet():
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    Efood = Label(f1, text="Enter the diet you want to search", fg="yellow", bg="#172c3e",font = ("Arial", 15, "bold italic"))
    Efood.place(x=230, y=80)

    detailbutton=Button(f1,text="view your diet plan",command=enterDetails,font = ("Arial", 15, "bold italic"))
    detailbutton.place(x=290,y=200)

    theBack = Button(f1, text="BACK", command=menu,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

def menu():

   
    f1 = Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    theBack = Button(f1, text="BACK", command=initial,font = ("Arial", 15, "bold italic"))
    theBack.place(x=20, y=20)

    Welcome = Label(f1, text="CHOOSE FROM THE MENU ", fg="yellow", bg="#172c3e", font = ("Arial", 30, "bold italic"))
    Welcome.place(x=130, y=150)

    theDetail = Button(f1, text="DETAILS", width=20,height=1, command= Detail, font = ("Arial", 15, "bold italic"))
    theDetail.place(x=270, y=310)

    theRecipe = Button(f1, text="RECIPE", width =20, height=1, command=Recipe, font = ("Arial", 15, "bold italic"))
    theRecipe.place(x=270, y=410)

    theDiet = Button(f1, text="DIET PLAN", width =20,height=1, command=Diet, font = ("Arial", 15, "bold italic"))
    theDiet.place(x=270, y=510)

def initial():
    global Weight1, Height1,Name1, Age1, user, passw
    f1=Frame(root, bg="#172c3e")
    f1.place(height=800, width=800)

    def check():
        global user,password,Utext,Ptext,username,passw, Age1, Weight1, Height1, h, w
        username=user.get()
        password=passw.get()
        
        if username == "rishab" and password == "rishab":
            tkmessagebox.showinfo("Login Info", "Welcome Rishab")
            menu()
        else:
            tkmessagebox.showerror("Error", "Wrong Username or Password ")


    f3 = Frame(f1, bg="black")
    f3.place(height=400, width=380, y=200)

    f4= tkinter.Frame(f1, bg="black")
    f4.place(height = 400, width= 380 , y=200, x=400)

    Welcome=Label(f1, text= "WELCOME", fg="yellow", bg="#172c3e", font = ("Arial", 30, "bold italic"))
    Welcome.place(x=300,y=100)

    ULabel=Label(f4, text ="Username",font = ("Arial", 12, "bold italic"), width=10)
    user=tkinter.Entry(f4,font = ("Arial", 12, "bold italic"), width=15)
    ULabel.place(x=20, y=100)
    user.place(x=160, y=100)

    PLabel=Label(f4,text="Password",font = ("Arial", 12, "bold italic"), width=10)
    passw=tkinter.Entry(f4,font = ("Arial", 12, "bold italic"), width=15, show='*')
    PLabel.place(x=20, y=150)
    passw.place(x=160, y=150)

    theButton=Button(f4, text= "LOGIN", command=check,  font = ("Arial", 12 , "bold italic"), width =8 )
    theButton.place(x=130, y=250)

    Name = Label(f3, text="Name", font=("Arial", 12, "bold italic"), width=13)
    Name1 = tkinter.Entry(f3, font=("Arial", 12, "bold italic"), width=15)
    Name.place(x=20, y=100)
    Name1.place(x=180, y=100)


    Age = Label(f3, text="Age", font=("Arial", 12, "bold italic"), width=13)
    Age1= tkinter.Entry(f3, font=("Arial", 12, "bold italic"), width=15)
    Age.place(x=20, y=150)
    Age1.place(x=180, y=150)

    Weight = Label(f3, text="Weight(in kgs)", font=("Arial", 12, "bold italic"), width=13)
    Weight1 = tkinter.Entry(f3, font=("Arial", 12, "bold italic"), width=15)
    Weight.place(x=20, y=200)
    Weight1.place(x=180, y=200)

    Height = Label(f3, text="Height(in m)", font=("Arial", 12, "bold italic"), width=13)
    Height1 = tkinter.Entry(f3, font=("Arial", 12, "bold italic"), width=15)
    Height.place(x=20, y=250)
    Height1.place(x=180, y=250)

    theButton5 = Button(f3, text="ENTER", command=menu, font=("Arial", 12, "bold italic"))
    theButton5.place(x=130, y=300)



initial()
root.mainloop()
