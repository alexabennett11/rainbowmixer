import flet as ft
 
def main(page: ft.Page):
    page.title = "Rainbow Mixer"
 
    # Text to display RGB values
    rgb_text = ft.Text("RGB(0, 0, 0)", size=20)
 
    # Function to update color
    def update_color(e):
        r = int(red_slider.value)
        g = int(green_slider.value)
        b = int(blue_slider.value)
 
        # Convert to hexadecimal
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
 
        # Change background
        page.bgcolor = hex_color
 
        # Display values
        rgb_text.value = f"RGB({r}, {g}, {b})"
        page.update()
 
    # Sliders
    red_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
    green_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
    blue_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
 
    # Add everything to the page
    page.add(
        ft.Text("Red"),
        red_slider,
        ft.Text("Green"),
        green_slider,
        ft.Text("Blue"),
        blue_slider,
        rgb_text
    )
 
# Run app
ft.run(main=main)