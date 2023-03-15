from adafruit_pybadger import pybadger

pybadger.show_badge(name_string="Sam", hello_scale=2, my_name_is_scale=2, name_scale=3)
pybadger.pixels.brightness = .01
pybadger.pixels.fill(pybadger.RED)
pybadger.play_tone(200,.2)
pybadger.play_tone(600,.2)
pybadger.play_tone(1000,.2)

while True:
    pybadger.auto_dim_display()
    
    if pybadger.button.start:
        pybadger.pixels.fill(pybadger.RED)
        pybadger.show_badge(name_string="Sam", hello_scale=2, my_name_is_scale=2, name_scale=3)

    if pybadger.button.a:
        pybadger.pixels.fill(pybadger.WHITE)
        pybadger.show_business_card(image_name="sam.bmp", name_string="Sam Havron", name_scale=2,
                                    email_string_one="sgh65@cornell.edu")

    if pybadger.button.b:
        pybadger.pixels.fill(pybadger.BLUE)
        pybadger.show_qr_code(data="https://meta.com")
