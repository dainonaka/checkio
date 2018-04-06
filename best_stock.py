def bar(cnt, key, value, winner = False):
    import tkinter
    global scale, cv, barwidth, barheight, maxheight
    text = key + ":" + str(value)
    if winner:
        outline = "red"
        width = 2
    else:
        outline = "black"
        width = 1
    cv.create_rectangle(
        barwidth * (cnt) , scale * 0.9 - (barheight*(value/maxheight)),
        barwidth * (cnt + 1) , scale*0.9,
        fill = "skyblue",
        outline = outline, width = width)
    cv.create_text(barwidth * (cnt + 0.5), scale * 0.95,
                   text = text , fill = outline,
                   anchor = "s")

def best_stock(data):
    import tkinter
    global scale, cv, barwidth, barheight, maxheight, key, maxlen
    win = tkinter.Tk()
    scale = 600
    cv = tkinter.Canvas(win, width = scale, height = scale)
    barwidth = scale / (len(data)+2)
    barheight = scale*0.8
    maxheight = max(data.values())
    winner_item = 0
    winner_key = None
    cnt = 0
    for key in data.keys():
        cnt += 1
        bar(cnt, key, data[key])
        if data[key] > winner_item:
            winner_key = key
            winner_item = data[key]
            winner_cnt = cnt
    bar(winner_cnt, winner_key, winner_item, True)
    cv.pack()
    win.mainloop()
    return winner_key

if __name__ == "__main__":
    data = {"Beethoven":32,"Schubert":21,"Liszt":1, "Scriabin":9}
    best_stock(data)
