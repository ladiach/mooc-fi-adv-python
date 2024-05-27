# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
	    def order_by_rating_descending(item:dict):
	        return item["rating"]
	 
	    return sorted(items, key = order_by_rating_descending, reverse = True)