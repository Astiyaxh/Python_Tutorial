def station_to_number(channels):
    return {station: number for number, station in channels.items()}


channels = {
    2: "CBS",
    4: "NBC",
    5: "FOX",
    7: "ABC"
}
print(station_to_number(channels))


def coaster_conversion(my_dict):
    return {coaster: round(height * 3.28083) for coaster, height in my_dict.items()}


coaster = {
    "Kinda Ka": 139,
    "Top Thrill Dragster": 130,
    "Superman: Escape From Krypton": 126
}

print(coaster_conversion(coaster))
