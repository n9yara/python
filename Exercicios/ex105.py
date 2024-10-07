def notas(* num, sit=False):
    resp = {}
    resp["total"] = len(num)
    resp["maior"] = max(num)
    resp["menor"] = min(num)
    resp["media"] = sum(num) / len(num)
    if sit:
        if resp["media"] >=7:
            resp["situacao"] = "BOA"
        elif resp["media"] >=5:
            resp["situacao"] = "RAZOAVEL"
        else:
            resp["situacao"] = "RUIM"

    return resp


resp = notas(1,1,1, sit=True)
print(resp)
