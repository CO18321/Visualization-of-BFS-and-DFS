import tkinter as tk
from collections import defaultdict
import time

nodeinfo=[]
edgeinfo=[]
nodecount=0

nextedgex=0
nextedgey=0

graph=defaultdict(list)

def find_closest_node(x,y):

    global nodeinfo, nodecount
    for i in range (nodecount):
        if abs(x-nodeinfo[i][2])<=20 and abs(y-nodeinfo[i][3])<=20:
            return i
    return -1

def edgestart(event):
    global nextedgex,nextedgey

    print(event.x, event.y)
    nextedgex=event.x
    nextedgey=event.y


def edgeend(event):
    global nextedgex, nextedgey
    node1= find_closest_node(nextedgex,nextedgey)
    node2 = find_closest_node(event.x, event.y)

    if node1== -1 or node2==-1:
        return
    x1=nodeinfo[node1][2]
    y1=nodeinfo[node1][3]
    x2=nodeinfo[node2][2]
    y2=nodeinfo[node2][3]

    l=c.create_line(x1,y1,x2,y2,width=2)
    c.tag_lower(l)
    edgeinfo.append([l,node1,node2])
    graph[node1].append(node2)



def addnode(event):
    global nodecount,nodeinfo
    wd=c.create_oval(event.x-20,event.y-20,event.x +20, event.y+20, fill='seagreen1', outline='seagreen1')
    wt=c.create_text(event.x,event.y,text=str(nodecount),font="helvetica 12")
    nodeinfo.append([wd,wt,event.x, event.y])

    nodecount=nodecount+1

def bfs():
    global graph
    s=source.get()

    trav1= tk.Label(root, text="Traversal:", font="helvetica 20")
    trav1.place(x=50, y=555)

    txt=""
    trav2 = tk.Label(root, text=txt, font="helvetica 20",fg="red")
    trav2.place(x=170, y=555)

    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    visited.append(s)
    queue.append(s)

    while queue:

        s = queue.pop(0)
        print(s,end=" ",flush=True)
        txt = txt + " " + str(s)
        trav2.config(text=txt)
        c.itemconfig(nodeinfo[s][0],fill="yellow",outline="yellow")

        root.update()
        time.sleep(0.5)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


root = tk.Tk()
root.title("BFS with GUI")
root.geometry('610x610')
root.resizable(0,0)
source = tk.IntVar()

c = tk.Canvas(root, width=500, height=500, bg='white')
c.pack()
c.bind('<Button-3>', addnode) #select
c.bind('<ButtonPress-1>', edgestart) #drag
c.bind('<ButtonRelease-1>', edgeend) #drag

srcl=tk.Label(root,text="Source:",font="helvetica 20")
srcl.place(x=50,y=515)
srce=tk.Entry(root,textvariable=source, width=3, font="helvetica 20")
srce.place(x=150,y=515)

btn=tk.Button(root,text = 'GO',font="helvetica 20", bg='seagreen1' ,command=bfs)
btn.place(x=490,y=505)

root.mainloop()

