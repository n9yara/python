def voto(ano):
    idade = (2024 - ano)
    print(f"Com {idade} anos: ", end = "")
    if idade < 18:
        return "voto não é obrigatorio"
    elif idade >= 18:
        return "voto O"
    elif idade >=65:
        return "voto OPCIONAL"





nasc = int(input("Em que ano voce nasceu? "))
print(voto(nasc))