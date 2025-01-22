#Default Parameters & Named Arguments
def beCheerful(name = "", repeat = 2):
    print(f"good morning {name}\n" * repeat)

beCheerful()
beCheerful("tim")
beCheerful(name="john lines")
beCheerful(repeat=6)
beCheerful(name="michael", repeat=5)
beCheerful(repeat=3, name="kb")
