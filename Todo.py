import PySimpleGUI as s
import fileModule


lis = []
completed = []
lis = fileModule.readFile()
completed = fileModule.readCompleted()
layout = [[s.Text("TODO LIST ")],[s.Text("ENTER : "),s.InputText("",key = "entry")],
          [s.Listbox(values=lis,key = "list",size=(40,6), enable_events=True), s.Listbox(values=completed,key = "complete",size=(40,6), enable_events=True)],
          [s.InputCombo(['','1','2','3','4','5'],key="priority"),s.CalendarButton("Choose Date", target="dat", key='date'),s.InputText("",key = "dat")],
          [s.Button("add"),s.Button("delete"),s.Button("prioritize"),s.Button("completed"),s.Button("Clear completed"),s.Exit()],
          [s.Text("", auto_size_text=False, key="tell")]]

window = s.Window("my first GUI ", layout)

while True:
    event, entries = window.Read()
    print(event, entries)
    if event is None or event == "Exit":
        break

    elif (event == "add"):
        if(entries["dat"] == ""):
            s.Popup('Invalid Option')
            continue


        x = entries["entry"]+" "+str(entries["dat"])+" "+str(int(entries["priority"]))
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        window.Element("entry").Update("")
        fileModule.writeToFile(lis)

    elif( event == "delete"):
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        fileModule.writeToFile(lis)

    elif( event == "prioritize"):
        for i in range(len(lis)):
            min = i
            for j in range(i+1, len(lis)):
                if(lis[min][-1] > lis[j][-1]):
                    min = j
            lis[i],lis[min] = lis[min],lis[i]
        window.FindElement("list").Update(lis)
        window.Element("").Update("prioritized")
        fileModule.writeToFile(lis)

    elif( event == "completed"):
        lis.remove(''.join(entries["list"]))
        completed.append(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.FindElement("complete").Update(completed)
        window.Element("tell").Update("TASK DONE GREAT JOB")
        fileModule.writeToCompleted(completed)

    elif(event=="Clear completed"):
        completed.remove(''.join(entries["complete"]))
        window.FindElement("complete").Update(completed)
        window.Element("tell").Update("item deleted")
        lis.clear()
        fileModule.writeToCompleted(completed)




window.Close()