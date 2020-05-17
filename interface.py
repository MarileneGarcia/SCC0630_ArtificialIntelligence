import tkinter
def interface (matriz):
  root = tkinter.Tk(  )
  tam_col = len(matriz)
  tam_linha = len(matriz[0])

  for r in range(tam_col):
    for c in range(tam_linha):
      if(matriz[r][c] == 1):
        tkinter.Label(root,bg="white").grid(row=r,column=c, ipadx=5, ipady=5)
      else: 
        tkinter.Label(root,bg="black").grid(row=r,column=c, ipadx=5, ipady=5)

      
  root.geometry("800x800")
  root.mainloop(  )
