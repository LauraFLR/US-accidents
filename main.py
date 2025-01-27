from dash import Dash
from src.components.layout import create_layout

def main() -> None:
    app = Dash()
    app.title='Staying Safe On The Road - Analysis On US-Traffic Accidents'
    app.layout = create_layout(app)
    app.run_server(debug=True)
    #app.run()

if __name__ == "__main__":
    main()