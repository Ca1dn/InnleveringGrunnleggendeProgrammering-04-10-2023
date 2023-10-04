text = "Dette er en teststreng med vokaler"

def tell_vokaler(string):
    vokaler = "aeiouyæøåAEIOUYÆØÅ"
    return sum(string.count(vokaler) for vokaler in vokaler)

result = tell_vokaler(text)
print("Antall vokaler i strengen er", result)
