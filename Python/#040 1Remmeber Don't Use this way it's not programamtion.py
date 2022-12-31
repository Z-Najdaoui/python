import tkinter
from tkinter import *
from tkinter import ttk


def forget_page1() :
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()


# game page
# steps
def steps():
    pass
def stable_designe() :
    # style new window
    window.geometry('1350x680+10+15')

    # header
    frm_header = Frame(width=1340,height=100,bg='#444')
    frm_header.place(x=5,y=0)

    # main
    frm_main = Frame(width=1340,height=480,bg='#555')
    frm_main.place(x=5,y=105)
        # steps
    lbl_start = Label(frm_main,text='Start',font=('Arial',20),width=5,highlightbackground="#000",highlightthickness=1)
    lbl_start.place(x=1250,y=2)

    step0 = Frame(frm_main,height=35,width=81,bg='#fff',highlightbackground="#000",highlightthickness=1)
    step0.place(x=1250,y=40)

    # testHieght = Frame(frm_main,height=400,width=50,bg='#8547ff',highlightbackground="#000",highlightthickness=1)
    # testHieght.place(x=1268,y=75)

    # testwidth = Frame(frm_main,height=50,width=1150,bg='#8547ff',highlightbackground="#000",highlightthickness=1)
    # testwidth.place(x=119,y=425) 
    
    # steps colm 1 
    # step1 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step1.place(x=1268,y=75)
    # step2 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step2.place(x=1268,y=125)
    # step3 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step3.place(x=1268,y=175)
    # step4 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step4.place(x=1268,y=225)
    # step5 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step5.place(x=1268,y=275)
    # step6 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step6.place(x=1268,y=325)
    # step7 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step7.place(x=1268,y=375)
    # step8 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step8.place(x=1268,y=425)
    # step9 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step9.place(x=1218,y=425)

    # # steps colm 2 
    # step10 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step10.place(x=1168,y=75)
    # step11 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step11.place(x=1168,y=125)
    # step12 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step12.place(x=1168,y=175)
    # step13 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step13.place(x=1168,y=225)
    # step14 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step14.place(x=1168,y=275)
    # step15 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step15.place(x=1168,y=325)
    # step16 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step16.place(x=1168,y=375)
    # step17 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step17.place(x=1168,y=425)
    # step18 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step18.place(x=1118,y=75)

    # # steps colm 3 
    # step19 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step19.place(x=1068,y=75)
    # step20 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step20.place(x=1068,y=125)
    # step21 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step21.place(x=1068,y=175)
    # step22 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step22.place(x=1068,y=225)
    # step23 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step23.place(x=1068,y=275)
    # step24 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step24.place(x=1068,y=325)
    # step25 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step25.place(x=1068,y=375)
    # step26 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step26.place(x=1068,y=425)
    # step27 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step27.place(x=1018,y=425)

    # # steps colm  4
    # step28 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step28.place(x=968,y=75)
    # step29 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step29.place(x=968,y=125)
    # step30 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step30.place(x=968,y=175)
    # step31 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step31.place(x=968,y=225)
    # step32 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step32.place(x=968,y=275)
    # step33 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step33.place(x=968,y=325)
    # step34 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step34.place(x=968,y=375)
    # step35 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step35.place(x=968,y=425)
    # step36 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step36.place(x=918,y=75)
    # # steps colm 5 
    # step37 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step37.place(x=868,y=75)
    # step38 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step38.place(x=868,y=125)
    # step39 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step39.place(x=868,y=175)
    # step40 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step40.place(x=868,y=225)
    # step41 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step41.place(x=868,y=275)
    # step42 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step42.place(x=868,y=325)
    # step43 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step43.place(x=868,y=375)
    # step44 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step44.place(x=868,y=425)
    # step45 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step45.place(x=818,y=425)

    # # steps colm  6
    # step46 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step46.place(x=768,y=75)
    # step47 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step47.place(x=768,y=125)
    # step48 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step48.place(x=768,y=175)
    # step49 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step49.place(x=768,y=225)
    # step50 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step50.place(x=768,y=275)
    # step51 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step51.place(x=768,y=325)
    # step52 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step52.place(x=768,y=375)
    # step53 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step53.place(x=768,y=425)
    # step54 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step54.place(x=718,y=75)
    # # steps colm 7 
    # step55 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step55.place(x=668,y=75)
    # step56 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step56.place(x=668,y=125)
    # step57 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step57.place(x=668,y=175)
    # step58 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step58.place(x=668,y=225)
    # step59 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step59.place(x=668,y=275)
    # step60 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step60.place(x=668,y=325)
    # step61 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step61.place(x=668,y=375)
    # step62 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step62.place(x=668,y=425)
    # step63 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step63.place(x=618,y=425)

    # # steps colm  8
    # step64 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step64.place(x=568,y=75)
    # step65 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step65.place(x=568,y=125)
    # step66 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step66.place(x=568,y=175)
    # step67 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step67.place(x=568,y=225)
    # step68 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step68.place(x=568,y=275)
    # step69 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step69.place(x=568,y=325)
    # step70 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step70.place(x=568,y=375)
    # step80 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step80.place(x=568,y=425)
    # step81 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step81.place(x=518,y=75)
    # # steps colm 9 
    # step82 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step82.place(x=468,y=75)
    # step83 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step83.place(x=468,y=125)
    # step84 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step84.place(x=468,y=175)
    # step85 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step85.place(x=468,y=225)
    # step86 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step86.place(x=468,y=275)
    # step87 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step87.place(x=468,y=325)
    # step88 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step88.place(x=468,y=375)
    # step89 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step89.place(x=468,y=425)
    # step90 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step90.place(x=418,y=425)

    # # steps colm  10
    # step91 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step91.place(x=368,y=75)
    # step92 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step92.place(x=368,y=125)
    # step93 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step93.place(x=368,y=175)
    # step94 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step94.place(x=368,y=225)
    # step95 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step95.place(x=368,y=275)
    # step96 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step96.place(x=368,y=325)
    # step97 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step97.place(x=368,y=375)
    # step98 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step98.place(x=368,y=425)
    # step99 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step99.place(x=318,y=75)

    # # steps colm 11 
    # step100 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step100.place(x=268,y=75)
    # step101 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step101.place(x=268,y=125)
    # step102 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step102.place(x=268,y=175)
    # step103 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step103.place(x=268,y=225)
    # step104 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step104.place(x=268,y=275)
    # step105 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step105.place(x=268,y=325)
    # step106 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step106.place(x=268,y=375)
    # step107 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step107.place(x=268,y=425)
    # step109 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step109.place(x=218,y=425)

    # # steps colm  12
    # step110 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step110.place(x=168,y=75)
    # step111 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step111.place(x=168,y=125)
    # step112 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step112.place(x=168,y=175)
    # step113 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step113.place(x=168,y=225)
    # step114 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step114.place(x=168,y=275)
    # step115 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step115.place(x=168,y=325)
    # step116 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step116.place(x=168,y=375)
    # step117 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step117.place(x=168,y=425)
    # step118 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
    # step118.place(x=118,y=75)
    tab_of_cordonne = []
    stepss = 0
    for i in range(23,0,-2):
        stepss += 1 
        for j in range(0,8):
            tab_of_cordonne.append([118+(i*50),(j*50)+75])
        if stepss%2==0:
            tab_of_cordonne.append([118+((i-1)*50),75])
            
        else:
            tab_of_cordonne.append([118+((i-1)*50),75+(7*50)])

    for q in range(len(tab_of_cordonne)):
        steps1 = Frame(frm_main,height=50,width=50,bg='#fff',highlightbackground="#666",highlightthickness=1)
        steps1.place(x=tab_of_cordonne[q][0],y= tab_of_cordonne[q][1])


    lbl_end = Label(frm_main,text='end',font=('Arial',20),height=3,width=2,highlightbackground="#000",highlightthickness=1,wraplength=1)
    lbl_end.place(x=46,y=49)

    step119 = Frame(frm_main,height=81,width=35,bg='#fff',highlightbackground="#000",highlightthickness=1)
    step119.place(x=83,y=59)
   
    # footer
    frm_footer = Frame(width=1340,height=85,bg='#444')
    frm_footer.place(x=5,y=590)





# ------------------------------------------
def sumfuns():
    forget_page1()
    stable_designe()
    

def players2() :
    sumfuns()
    global numOfPlayers
    numOfPlayers = 2

def players3() :
    sumfuns()
    global numOfPlayers
    numOfPlayers = 3

def players4() :
    sumfuns()
    global numOfPlayers
    numOfPlayers = 4


window = Tk()
window.title('Version 1.0')
window.geometry('550x350+500+200')
window.resizable(False, False)
window['bg'] = "#333"


# page1

lbl_select = Label(text='Select number of players :',font=('Arial',30),bg='#333',fg='#fff')
lbl_select.place(x=45,y=80)


btn_player2 = Button(master=window,text='2 Players',font=('Arial',20),command=players2)
btn_player2.place(x=30,y=250)

btn_player3 = Button(master=window,text='3 Players',font=('Arial',20),command=players3)
btn_player3.place(x=200,y=250)
'''customtkinter.CTkButton'''
btn_player4 =  Button(master=window,text='4 Players',font=('Arial',20),command=players4)
btn_player4.place(x=370,y=250)





window.mainloop()