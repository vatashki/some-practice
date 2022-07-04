offers = input()
nuber_of_beggars = int(input())

str_list_offers = offers.split(', ')
int_list_offers = [int(x) for x in str_list_offers]

int_list_what_beggars_got = []

for i in range(nuber_of_beggars):
    int_list_what_beggars_got.append(0)

while len(int_list_offers) > 0:
    for beggar in range(nuber_of_beggars):
        int_list_what_beggars_got[beggar] = int_list_what_beggars_got[beggar] + (int_list_offers[0])
        int_list_offers.remove(int_list_offers[0])
        if len(int_list_offers) == 0:
            break

print(int_list_what_beggars_got)

