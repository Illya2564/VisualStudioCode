from models.Ampfetamine import Ampfetamine

sulf_amf = Ampfetamin("sulf", 400)
print ("Уточните вес?")
weight = input()
print ("Вам це вийде", str(weight*sulf_amf.price))