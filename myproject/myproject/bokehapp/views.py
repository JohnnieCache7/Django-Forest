from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components


def bokeh_plot(request):
    # Hardcoded video game data
    video_games = [
        {"Title": "The Legend of Zelda: Breath of the Wild", "Global_Sales": 23.21},
        {"Title": "Super Mario Bros.", "Global_Sales": 40.24},
        {"Title": "Minecraft", "Global_Sales": 200.0},
        {"Title": "Grand Theft Auto V", "Global_Sales": 135.0},
        {"Title": "Tetris", "Global_Sales": 35.0},
        {"Title": "Wii Sports", "Global_Sales": 82.86},
        {"Title": "Pokemon Red/Green/Blue", "Global_Sales": 31.38},
        {"Title": "PlayerUnknown's Battlegrounds", "Global_Sales": 70.0},
        {"Title": "Mario Kart 8 Deluxe", "Global_Sales": 35.39},
        {"Title": "The Elder Scrolls V: Skyrim", "Global_Sales": 30.0},
    ]

    # Filter video games to include only Minecraft, Grand Theft Auto V, and Mario Kart 8 Deluxe
    filtered_video_games = [
        game
        for game in video_games
        if game["Title"] in ["Minecraft", "Grand Theft Auto V", "Mario Kart 8 Deluxe"]
    ]

    # Create a Bokeh figure
    p = figure(
        y_range=[game["Title"] for game in filtered_video_games],  # Games on y-axis
        x_axis_label="Global Sales (in millions)",
        y_axis_label="Video Games",
        title="Global Sales of Selected Video Games",
        background_fill_color="#f0f0f0",
    )

    # Create bars for each game
    p.hbar(
        y=[game["Title"] for game in filtered_video_games],  # Games on y-axis
        right=[
            game["Global_Sales"] for game in filtered_video_games
        ],  # Global sales on x-axis
        height=0.5,
        color="#4682b4",
        line_color="#4682b4",
    )

    # Customize the plot
    p.title.text_font_size = "16pt"
    p.xaxis.major_label_text_font_size = "12pt"
    p.yaxis.major_label_text_font_size = "12pt"

    # Convert the plot to a div and script
    script, div = components(p)

    # Pass the script and div to the template
    context = {
        "script": script,
        "div": div,
    }

    return render(request, "bokeh_plot.html", context)
