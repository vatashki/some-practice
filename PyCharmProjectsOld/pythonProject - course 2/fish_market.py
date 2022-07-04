skumriya_price = float(input())
tzatza_price = float(input())
kg_palamoud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

midi_price = 7.50
palamoud_price = skumriya_price + skumriya_price * 0.6
safrid_price = tzatza_price + tzatza_price * 0.8

total_palamoud = palamoud_price * kg_palamoud
total_safrid = safrid_price * kg_safrid
total_midi = midi_price * kg_midi

total_price = total_midi + total_safrid + total_palamoud

formated_price = "{:.2f}".format(total_price)

print(formated_price)