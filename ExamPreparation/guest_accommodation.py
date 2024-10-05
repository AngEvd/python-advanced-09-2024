def accommodate(*args, **kwargs):
    guests = args
    rooms = dict(sorted(kwargs.items(), key=lambda kvp: (kvp[1], kvp[0])))
    hotel = {"accomodated": {},
             "unaccomodated": {}
    }
    for group in guests:
        for room, room_size in rooms.items():
            if room_size >= group:
                hotel["accomodated"][room] = group
                del rooms[room]
                break
        else:
            hotel["unaccomodated"][room] = room_size

    if not hotel["accomodated"]:
        result = "No accommodations were completed!"
    else:
        result = f"A total of {len(hotel['accomodated'])} accommodations were completed!"
    for room_number, accomodated_guests in sorted(hotel["accomodated"].items(), key=lambda kvp: kvp[0]):
        result += f"\n<Room {room_number.replace('room_', '')} accommodates {accomodated_guests} guests>"

    if hotel["unaccomodated"]:
        result += f"\nGuests with no accommodation: {sum(guests) - sum(hotel['accomodated'].values())}"

    if rooms:
        result += f"\nEmpty rooms: {len(rooms)}"

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

