def can_travel(distance_mi, is_raining, has_bike, has_car, has_ride_share_app):

    if distance_mi <= 1:
        return not is_raining

    elif distance_mi <= 6:
        return has_bike and not is_raining

    else:
        return has_car or has_ride_share_app


result = can_travel(
    distance_mi=13,
    is_raining=False,
    has_bike=False,
    has_car=True,
    has_ride_share_app=False
)

print(result)