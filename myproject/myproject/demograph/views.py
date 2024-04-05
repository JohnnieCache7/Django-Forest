from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from .models import best_seller
import pandas as pd
import html
from bokeh.models import ColumnDataSource
import json

# def graph(request):
#    plot = figure()
#    x1=[1,2,3,4,5]
#    y1=[2,3,4,5,6]
#    plot.line(x1,y1,line_width=5)
#     pass
#    script, div = components(plot, CDN)

#    return render(request, "index_graph.html", {"the_script": script, "the_div": div})


def all_data(request):
    output = best_seller.objects.all()
    return render(request, "index_graph2.html", {"output": output})


def pandasframe(request):
    output = best_seller.objects.all()
    my_frame = pd.DataFrame([vars(s) for s in output])
    my_frame.drop("_state", axis="columns", inplace=True)
    my_html_frame = my_frame.to_html()
    return render(request, "index_graph3.html", {"my_html_frame": my_html_frame})


def dfgraph(request):
    output = best_seller.objects.all()
    my_frame = pd.DataFrame([vars(s) for s in output])
    my_frame.drop("_state", axis="columns", inplace=True)
    source = ColumnDataSource(my_frame)

    p = figure()
    p.circle(x="review_count", y="year", source=source, size=10, color="green")

    scripts, divs = components(p)

    return render(
        request, "index_graph4.html", {"the_scripts": scripts, "the_divs": divs}
    )
