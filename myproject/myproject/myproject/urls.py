from django.contrib import admin
from django.urls import path, re_path
from helloworld import views
from to_do import views as to_do_view
from graph import views as graph_view
from demograph import views as demograph_view
from bokehapp import views as plot_view

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("to_do/", to_do_view.to_do, name="to do list"),
    # path("graph/", demograph_view.graph, name="my_graph"),
    path("homework_vs_work/", graph_view.homework_vs_work, name="homework_vs_work"),
    path("cupcakes_sold/", graph_view.cupcakes_sold, name="cupcakes_sold"),
    re_path("db_data/", demograph_view.all_data, name="all_db_data"),
    path("pandas_frame/", demograph_view.pandasframe, name="pandas_frame"),
    path("dfgraph/", demograph_view.dfgraph, name="my df graph"),
    path("bokeh-plot/", plot_view.bokeh_plot, name="bokeh_plot"),
    re_path(r"^$", views.home, name="home"),
]
