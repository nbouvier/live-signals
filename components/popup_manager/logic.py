next_popup_id = 0

def popup(message, type):
	global next_popup_id
	
	popup=dict(
		id=str(next_popup_id),
		message=message,
		type=type
	)

	next_popup_id += 1

	return popup
