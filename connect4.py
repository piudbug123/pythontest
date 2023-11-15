# from flask import Flask, render_template_string
# from flask_plots import Plots
# from matplotlib.figure import Figure

# app = Flask(__name__)
# plots = Plots(app)

# # routes
# @app.route("/new")
# def bar():
#     # Make data:
#     countries = ["Argentina", "Brasil", "Colombia", "Chile"]
#     peoples = [14, 40, 16, 24]
    
#     # Plot:
#     fig = Figure()
#     ax = fig.subplots()
#     plots.bar(ax, countries, peoples)  # Use 'ax' instead of 'fig'
#     ax.set_title("Bar Chart")
    
#     data = plots.get_data(fig)
    
#     return render_template_string(
#         """
#         {% from 'plots/utils.html' import render_img %}
#         {{ render_img(data=data, alt_img='my_img') }}
#         """,
#         data=data
#     )

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)



    
