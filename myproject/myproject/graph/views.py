from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN


def homework_vs_work(request):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    homework_time = [2, 3, 2, 4, 3]
    work_time = [8, 8, 8, 8, 8]

    plot = figure(x_range=days, title="Homework vs Work", height=250)
    plot.vbar(
        x=days, top=homework_time, width=0.4, legend_label="Homework", color="blue"
    )
    plot.vbar(
        x=days, top=work_time, width=0.4, legend_label="Work", color="green", alpha=0.5
    )

    script, div = components(plot, CDN)

    return render(
        request, "homework_vs_work.html", {"the_script": script, "the_div": div}
    )


def cupcakes_sold(request):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    cupcakes_sold = [5, 4, 6, 5, 5]

    plot = figure(
        x_range=days,
        title="Cupcakes Sold",
        x_axis_label="Day",
        y_axis_label="Number of Cupcakes",
        height=250,
    )
    plot.vbar(x=days, top=cupcakes_sold, width=0.4, color="red")

    script, div = components(plot, CDN)

    return render(request, "cupcakes_sold.html", {"the_script": script, "the_div": div})
