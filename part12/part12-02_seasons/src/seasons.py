# Write your solution here:
def sort_by_seasons(shows:list):
    def order_by_season(show:dict):
        return show["seasons"]

    return sorted(shows, key=order_by_season)