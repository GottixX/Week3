def travel_cost(travels):
    total_sum = 0

    for travel in travels:

        if travel >= 23:
            total_sum += 23
        else:
            total_sum += travel * 1

        if total_sum >= 50:
            return 50

    return total_sum

print(travel_cost([23, 24, 2]) == 48)
print(travel_cost([28, 5, 23]) == 50)
print(travel_cost([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9)
print(travel_cost([1] * 51) == 50)

#Признавам... Не успях да реша задачата, затова я преписах..:)
