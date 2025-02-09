def get_store_data(stores, store_id):
	for store in stores:
		if store['props']['id'] == store_id:
			return store['props']['data']
