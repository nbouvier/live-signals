import numpy as np
from dash import Dash
from layout import create_layout

def main():
	# Initialize the Dash app
	app = Dash(
		__name__,
		external_stylesheets=[
			'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
		]
	)

	# Create the layout
	app.layout = create_layout(app)

	# Run the app
	if __name__ == '__main__':
		app.run(debug=True)

main() 
