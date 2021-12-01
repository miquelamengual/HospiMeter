from graphics import *
import pandas as pd
import random as rm
import matplotlib.pyplot as plt

# Code to click on the box area
def click_box(p, box):
    p1 = box.getP1()
    p2 = box.getP2()
    return p1.getX() < p.getX() < p2.getX() and p1.getY() < p.getY() < p2.getY()

# Welcome interface
def welcome():
    win = GraphWin("HospiMeter", 1200, 650)

    # Insert title, welcome the user, and image
    win.setBackground("lightgray")
    title = Text(Point(600, 100), "HospiMeter").draw(win)
    title.setSize(36)
    title.setStyle("bold")
    title.setTextColor("darkblue")
    title.setFace("helvetica")
    Image(Point(600, 250), "hospital.png").draw(win)
    text1 = Text(Point(600, 400), "Welcome to the US hospital efficiency processor!").draw(win)
    text1.setSize(20)
    text1.setStyle("bold")
    text1.setFace("helvetica")
    text2 = Text(Point(600, 425), "Your data has been processed. Please go ahead and obtain your insights!").draw(win)
    text2.setSize(16)
    text2.setFace("helvetica")
    text3 = Text(Point(600, 450), "US Department of Health and Human Services ").draw(win)
    text3.setSize(14)
    text3.setFace("helvetica")
    text3.setStyle("italic")

    # Button to proceed
    button = Text(Point(600, 550), "Go!")
    go = Rectangle(Point(550, 520), Point(650, 580)).draw(win)
    go.setFill("white")
    button.setSize(16)
    button.setStyle("bold")
    button.draw(win)


    while True:
        click = win.getMouse()
        if click_box(click, go):
            break

    win.close()

# Menu interface
def menu():
    win = GraphWin("Menu", 1200, 650)

    # Insert instruction on how to proceed and use the program
    win.setBackground("lightgray")
    Image(Point(1050, 300), "covid.png").draw(win)
    title = Text(Point(200, 100), "HospiMeter").draw(win)
    title.setSize(28)
    title.setStyle("bold")
    title.setTextColor("darkblue")
    title.setFace("helvetica")

    text1 = Text(Point(455, 200), "This program has gathered information about the capacity of hospitals in the United States").draw(win)
    text1.setSize(16)
    text1.setStyle("bold")
    text1.setFace("helvetica")

    text2 = Text(Point(343, 225), "if 20 % of the population were to be infected with COVID-19.").draw(win)
    text2.setSize(16)
    text2.setStyle("bold")
    text2.setFace("helvetica")

    text3 = Text(Point(511, 275), "This includes data on their current and expected room availability, a forecast of the expect number of COVID cases,").draw(win)
    text3.setSize(16)
    text3.setFace("helvetica")

    text4 = Text(Point(365, 300), "and a prediction on whether hospital will be able to handle the situation.").draw(win)
    text4.setSize(16)
    text4.setFace("helvetica")

    text5 = Text(Point(300, 350), "Please select the plot you would like to see below.").draw(win)
    text5.setSize(16)
    text5.setFace("helvetica")

    # Button 1
    button = Text(Point(175, 425), "Barplot")
    button.setSize(16)
    button.setFace("helvetica")
    button.setStyle("italic")
    button.draw(win)
    bar = Rectangle(Point(125, 400), Point(225, 450)).draw(win)

    # Button 2
    button2 = Text(Point(400, 425), "Line Chart")
    button2.setSize(16)
    button2.setFace("helvetica")
    button2.setStyle("italic")
    button2.draw(win)
    line = Rectangle(Point(350, 400), Point(450, 450)).draw(win)

    # Button 3
    button3 = Text(Point(625, 425), "Stacked Barplot")
    button3.setSize(16)
    button3.setFace("helvetica")
    button3.setStyle("italic")
    button3.draw(win)
    stack = Rectangle(Point(565, 400), Point(685, 450)).draw(win)

    t = Text(Point(600, 325), "")
    t.draw(win)
    # Wait for a mouse click
    while True:
        click = win.getMouse()
        if click_box(click, bar):
            x=1
            break
        elif click_box(click, line):
            x=2
            break
        elif click_box(click, stack):
            x=3
            break
        else:
            t.setText("")
    win.close()
    return x

# Custom interface
def custom():
    win = GraphWin("Customize", 1200, 650)

    # Insert information
    Image(Point(1000, 325), "states.png").draw(win)
    win.setBackground("lightgray")
    title = Text(Point(200, 100), "HospiMeter").draw(win)
    title.setSize(28)
    title.setStyle("bold")
    title.setTextColor("darkblue")
    title.setFace("helvetica")

    text_bar = Text(Point(350, 150), "Barplot: Percentage of total ICU beds needed in 12 months per State").draw(win)
    text_bar.setSize(16)
    text_bar.setFace("helvetica")

    text_line = Text(Point(255, 175), "Line graph: Overall country performance").draw(win)
    text_line.setSize(16)
    text_line.setFace("helvetica")

    text_stack = Text(Point(267, 200), "Stacked Bar: Infected vs Hospitalized vs ICU").draw(win)
    text_stack.setSize(16)
    text_stack.setFace("helvetica")

    text1 = Text(Point(230, 250), "Go ahead and custom your plot!").draw(win)
    text1.setSize(16)
    text1.setFace("helvetica")

    # Select State
    text2 = Text(Point(265, 300), "Enter your state(s) of interest one by one:").draw(win)
    text2.setSize(14)
    text2.setStyle("bold")

    text3 = Text(Point(270, 325), "Refer to the state codes displayed on the right.").draw(win)
    text3.setSize(14)
    text3.setStyle("italic")
    outputText1 = Text(Point(270, 350), "").draw(win)

    # Button to keep adding states.
    button = Text(Point(650, 300), "Add")
    button.setSize(14)
    button.setFace("helvetica")
    button.setStyle("italic")
    button.draw(win)
    add = Rectangle(Point(625, 285), Point(675, 315)).draw(win)
    inputText1 = Entry(Point(510, 300), 25)

    # Button to print plot
    button2 = Text(Point(650, 400), "Click here to plot!")
    plot = Rectangle(Point(575, 375), Point(725, 425)).draw(win)
    plot.setFill("white")
    button2.setSize(14)
    button2.setFace("helvetica")
    button2.setStyle("bold")
    button2.draw(win)

    # Button to reset data
    button3 = Text(Point(650, 475), "Reset")
    reset = Rectangle(Point(620, 460), Point(680, 490)).draw(win)
    reset.setFill("pink")
    button3.setSize(14)
    button3.setFace("helvetica")
    button3.setStyle("italic")
    button3.draw(win)


    # Button to go back to the home page
    button4 = Text(Point(650, 525), "Menu")
    back_to_menu = Rectangle(Point(620, 510), Point(680, 540)).draw(win)
    back_to_menu.setFill("powderblue")
    button4.setSize(14)
    button4.setFace("helvetica")
    button4.setStyle("italic")
    button4.draw(win)


    # Button to set title, x and y axis
    button5 = Text(Point(480, 450), "Set")
    button5.setSize(14)
    button5.setFace("helvetica")
    button5.setStyle("italic")
    button5.draw(win)
    set = Rectangle(Point(460, 435), Point(500, 465)).draw(win)

    # Custom title
    text4 = Text(Point(180, 400), "Title of the Plot: ").draw(win)
    text4.setSize(14)
    text4.setStyle("bold")
    inputText2 = Entry(Point(335, 400), 25).draw(win)
    Entry(Point(350, 300), 100)

    # Label X Axis
    text5 = Text(Point(170, 450), "Label X Axis: ").draw(win)
    text5.setSize(14)
    text5.setStyle("bold")
    inputText3 = Entry(Point(314, 450), 25).draw(win)

    # Label Y Axis
    text6 = Text(Point(170, 500), "Label Y Axis: ").draw(win)
    text6.setSize(14)
    text6.setStyle("bold")
    inputText4 = Entry(Point(314, 500), 25).draw(win)

    t = Text(Point(600, 325), "")
    t.draw(win)

    inputText1.draw(win)
    desiredstates = []

    # assign any value
    xaxis, yaxis, title = "undefined", "undefined", "undefined"

    valid_input = False
    while not valid_input:
        click = win.getMouse()
        if click_box(click, add):
            state = inputText1.getText()
            desiredstates.append(state.upper())
            inputText1.setText("")
        if click_box(click, plot):
            decision = 1
            break
        if click_box(click, reset):
            decision = 2
            break
        if click_box(click, back_to_menu):
            decision = 3
            break
        if click_box(click, set):
            title = inputText2.getText()
            xaxis = inputText3.getText()
            yaxis = inputText4.getText()
        else:
            t.setText("")

    win.close()
    return desiredstates, decision, title, xaxis, yaxis

# General graph code
def quicksort(dict):
    if len(dict) < 2:
        return dict
    else:
        indexes = list(range(0, len(dict)))
        pivot = rm.choice(list(dict.items()))
        less = {}
        greater = {}
        pi = {}
        for key, value in dict.items():
            if value > pivot[1]:
                greater[key] = value
            if value < pivot[1]:
                less[key] = value
            if value == pivot[1]:
                pi[key] = value
        return {**quicksort(greater), **pi, **quicksort(less)}

# Creating the barplot
def getinfobar(beta):
    col_list = ["HRR","Total Hospital Beds","Total ICU Beds","Available Hospital Beds","Potentially Available Hospital Beds*","Available ICU Beds","Potentially Available ICU Beds*","Adult Population","Projected Infected Individuals","Projected Hospitalized Individuals","Projected Individuals Needing ICU Care","Hospital Beds Needed, Six Months","Percentage of Available Beds Needed, Six Months","Percentage of Potentially Available Beds Needed, Six Months","Percentage of Total Beds Needed, Six Months","Hospital Beds Needed, Twelve Months","Percentage of Available Beds Needed, Twelve Months","Percentage of Potentially Available Beds Needed, Twelve Months","Percentage of Total Beds Needed, Twelve Months","Hospital Beds Needed, Eighteen Months","Percentage of Available Beds Needed, Eighteen Months","Percentage of Potentially Available Beds Needed, Eighteen Months","Percentage of Total Beds Needed, Eighteen Months","ICU Beds Needed, Six Months","Percentage of Available ICU Beds Needed, Six Months","Percentage of Potentially Available ICU Beds Needed, Six Months","Percentage of Total ICU Beds Needed, Six Months","ICU Beds Needed, Twelve Months","Percentage of Available ICU Beds Needed, Twelve Months","Percentage of Potentially Available ICU Beds Needed, Twelve Months","Percentage of Total ICU Beds Needed, Twelve Months","ICU Beds Needed, Eighteen Months","Percentage of Available ICU Beds Needed, Eighteen Months","Percentage of Potentially Available ICU Beds Needed, Eighteen Months","Percentage of Total ICU Beds Needed, Eighteen Months"]
    df = pd.read_csv("20popstates2.csv", usecols=col_list, index_col=False)

    state = df["HRR"]
    beds = df["ICU Beds Needed, Twelve Months"]

    total_st = beta
    index_list = 0
    totalbeds = 0
    bedsbystate = {}
    valid = False
    while not valid:
        for i in range(len(state)):
            if state[i] == total_st[index_list]:
                totalbeds += beds[i]
                if not bedsbystate.get(state[i]):
                    bedsbystate[state[i]] = beds[i]
                else:
                    bedsbystate[state[i]] = bedsbystate.get(state[i]) + beds[i]
        index_list += 1
        if index_list == len(total_st):
            valid = True
    bedsbystateperc = {}
    for key, value in bedsbystate.items():
        bedsbystateperc[key] = value / totalbeds

    return bedsbystateperc

def barplot(plotinf, T, lx,ly):
    keys = plotinf.keys()
    values = plotinf.values()

    plt.bar(keys, values)
    plt.title(T)
    plt.xlabel(lx)
    plt.ylabel(ly)
    plt.show()

# Creating the line graph
def getinfoline(beta):
    col_list = ["HRR","Total Hospital Beds","Total ICU Beds","Available Hospital Beds","Potentially Available Hospital Beds*","Available ICU Beds","Potentially Available ICU Beds*","Adult Population","Projected Infected Individuals","Projected Hospitalized Individuals","Projected Individuals Needing ICU Care","Hospital Beds Needed, Six Months","Percentage of Available Beds Needed, Six Months","Percentage of Potentially Available Beds Needed, Six Months","Percentage of Total Beds Needed, Six Months","Hospital Beds Needed, Twelve Months","Percentage of Available Beds Needed, Twelve Months","Percentage of Potentially Available Beds Needed, Twelve Months","Percentage of Total Beds Needed, Twelve Months","Hospital Beds Needed, Eighteen Months","Percentage of Available Beds Needed, Eighteen Months","Percentage of Potentially Available Beds Needed, Eighteen Months","Percentage of Total Beds Needed, Eighteen Months","ICU Beds Needed, Six Months","Percentage of Available ICU Beds Needed, Six Months","Percentage of Potentially Available ICU Beds Needed, Six Months","Percentage of Total ICU Beds Needed, Six Months","ICU Beds Needed, Twelve Months","Percentage of Available ICU Beds Needed, Twelve Months","Percentage of Potentially Available ICU Beds Needed, Twelve Months","Percentage of Total ICU Beds Needed, Twelve Months","ICU Beds Needed, Eighteen Months","Percentage of Available ICU Beds Needed, Eighteen Months","Percentage of Potentially Available ICU Beds Needed, Eighteen Months","Percentage of Total ICU Beds Needed, Eighteen Months"]
    df = pd.read_csv("20popstates2.csv", usecols=col_list, index_col=False)

    state = df["HRR"]
    bedshos6 = df["Hospital Beds Needed, Six Months"]
    bedshos12 = df["Hospital Beds Needed, Twelve Months"]
    bedshos18 = df["Hospital Beds Needed, Eighteen Months"]

    bedshos6count = {}
    bedshos12count = {}
    bedshos18count = {}
    index_list = 0
    valid = False
    while not valid:
        for i in range(0, len(state)):
            if state[i] == beta[index_list]:
                if not bedshos6count.get(state[i]):
                    bedshos6count[state[i]] = bedshos6[i]
                else:
                    bedshos6count[state[i]] = bedshos6count.get(state[i]) + bedshos6[i]

                if not bedshos12count.get(state[i]):
                    bedshos12count[state[i]] = bedshos12[i]
                else:
                    bedshos12count[state[i]] = bedshos12count.get(state[i]) + bedshos12[i]

                if not bedshos18count.get(state[i]):
                    bedshos18count[state[i]] = bedshos18[i]
                else:
                    bedshos18count[state[i]] = bedshos18count.get(state[i]) + bedshos18[i]
        index_list += 1
        if index_list == len(beta):
            valid = True

    return bedshos6count, bedshos12count, bedshos18count

# Merge dictionaries
def dict_join(dic1, dic2, dic3):
    dic = {}
    dic["moths"] = ["6 months","12 months","18 months"]
    for key in dic1.keys():
        try:
            dic.setdefault(key,[]).append(dic1[key])
        except KeyError:
            pass
        try:
            dic.setdefault(key,[]).append(dic2[key])
        except KeyError:
            pass
        try:
            dic.setdefault(key,[]).append(dic3[key])
        except KeyError:
            pass
    return dic


def val(x,T,lx,ly):
    df = pd.DataFrame(x)
    df.plot(x = "moths")
    plt.title(T)
    plt.xlabel(lx)
    plt.ylabel(ly)
    plt.show()

# Creating Stacked Plot
def getinfostack(beta):
    col_list=["HRR","Total Hospital Beds","Total ICU Beds","Available Hospital Beds","Potentially Available Hospital Beds*","Available ICU Beds","Potentially Available ICU Beds*","Adult Population","Projected Infected Individuals","Projected Hospitalized Individuals","Projected Individuals Needing ICU Care","Hospital Beds Needed, Six Months","Percentage of Available Beds Needed, Six Months","Percentage of Potentially Available Beds Needed, Six Months","Percentage of Total Beds Needed, Six Months","Hospital Beds Needed, Twelve Months","Percentage of Available Beds Needed, Twelve Months","Percentage of Potentially Available Beds Needed, Twelve Months","Percentage of Total Beds Needed, Twelve Months","Hospital Beds Needed, Eighteen Months","Percentage of Available Beds Needed, Eighteen Months","Percentage of Potentially Available Beds Needed, Eighteen Months","Percentage of Total Beds Needed, Eighteen Months","ICU Beds Needed, Six Months","Percentage of Available ICU Beds Needed, Six Months","Percentage of Potentially Available ICU Beds Needed, Six Months","Percentage of Total ICU Beds Needed, Six Months","ICU Beds Needed, Twelve Months","Percentage of Available ICU Beds Needed, Twelve Months","Percentage of Potentially Available ICU Beds Needed, Twelve Months","Percentage of Total ICU Beds Needed, Twelve Months","ICU Beds Needed, Eighteen Months","Percentage of Available ICU Beds Needed, Eighteen Months","Percentage of Potentially Available ICU Beds Needed, Eighteen Months","Percentage of Total ICU Beds Needed, Eighteen Months"]
    df = pd.read_csv("20popstates2.csv", usecols=col_list, index_col=False)

    state = df["HRR"]
    infected = df["Projected Infected Individuals"]
    hospi = df["Projected Hospitalized Individuals"]
    uci = df["Projected Individuals Needing ICU Care"]

    index_list = 0
    infec = {}
    hosp = {}
    uc = {}
    valid = False
    while not valid:
        for i in range(len(state)):
            if state[i] == beta[index_list]:
                if not infec.get(state[i]):
                    val1 = infected[i].replace(",","")
                    val1 = int(val1)
                    infec[state[i]] = val1
                else:
                    infec[state[i]] = infec.get(state[i]) + val1

                if not hosp.get(state[i]):
                    hosp[state[i]] = hospi[i]*1000
                else:
                    hosp[state[i]] = hosp.get(state[i]) + hospi[i]*1000

                if not uc.get(state[i]):
                    uc[state[i]] = uci[i]*1000
                else:
                    uc[state[i]] = uc.get(state[i]) + uci[i]*1000
        index_list += 1
        if index_list == len(beta):
            valid = True

    return infec, hosp, uc


def stackplot(x,y,z,T,lx,ly):
    state = []
    peopleinf = []
    for key, value in x.items():
        state.append(key)
        peopleinf.append(value)

    peoplehospi = []
    for i in range(len(state)):
        for key, value in y.items():
            if key == state[i]:
                peoplehospi.append(value)

    peopleuci = []
    for i in range(len(state)):
        for key, value in z.items():
            if key == state[i]:
                peopleuci.append(value)

    fig, ax = plt.subplots()

    ax.bar(state, peopleinf, label='Non-Hospitalized')
    ax.bar(state, peoplehospi, bottom=peopleinf, label='Hospitalized')
    ax.bar(state, peopleuci, bottom=peoplehospi, label='UCI')

    ax.legend()
    plt.title(T)
    plt.xlabel(lx)
    plt.ylabel(ly)
    plt.show()


def main():
    welcome()
    g = menu()
    continueloop = False
    while not continueloop:
        states, dc, m, n, z = custom()
        if dc != 2:
            continueloop = True
    if dc == 1:
        if g == 1:
            barinf = getinfobar(states)
            barinf2 = quicksort(barinf)
            barplot(barinf2, m, n, z)
        elif g == 2:
            dict1, dict2, dict3 = getinfoline(states)
            x = dict_join(dict1, dict2, dict3)
            val(x, m, n, z)
        elif g == 3:
            a, b, c = getinfostack(states)
            stackplot(a, b, c, m, n, z)
    if dc == 3:
        main()

if __name__ == '__main__':
    main()
