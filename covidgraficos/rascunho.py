def histog_dado(dados, h, typeh=0, padrao='continent'):
    index = list((dados.groupby([padrao])[h].sum()).index)
    if typeh == 0:
        h = list(dados.groupby([padrao])[h].sum())
    else:
        h = list(dados.groupby([padrao])[h].mean())
    plt.bar(index, h)
    
def scatter_dois_dados(dados, x, y, typex=0, typey=0, padrao='location'):
    if typex == 0:
        eixox = list(dados.groupby([padrao])[x].sum())
    else:
        eixox = list(dados.groupby([padrao])[x].mean())
    if typey == 0:
        eixoy = list(dados.groupby([padrao])[y].sum())
    else:
        eixoy = list(dados.groupby([padrao])[y].mean())
                     
    plt.scatter(eixox, eixoy)
    x = x.replace("_", " ").upper() 
    y = y.replace("_", " ").upper()
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} X {y}")
    plt.show()