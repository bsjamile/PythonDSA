# %%
def askint():
    try:
        val = int(input("digite um number: "))
    except:
        print("Você nao digitou um numero!")
    finally:
        print("Obrigada!!!!")
# %%
askint()
# %%
def askint():
    try:
        val = int(input("digite um number: "))
    except:
        print("Você nao digitou um numero!")
        val = int(input("Tente novamente. digite um number: "))
    finally:
        print("Obrigada!!!!")
# %%
while True:
    try:
        val = int(input("digite um number: "))
    except:
        print("Você não digitou um número!")
        continue #a frase vai continuar a aparecer
    else:
        print("Obrigada por digitar um número!")
    finally:
        print("Fim da exeução!")
    print(val)
# %%
