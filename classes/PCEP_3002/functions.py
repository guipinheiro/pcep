def funcao(*args, **kwargs):
    for arg in args:
        print("Positional arg:", arg)
    print("Args:", args)
        
    for key, value in kwargs.items():
        print("Key:'", key, "' for value'", value, "'")
    print("Kwargs:", kwargs)
funcao(1, 2, a="k1", b="k2")

# def funcao2(a='', b): # it can't have position parameters after keyword args
    