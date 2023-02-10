from Booking.booking import Booking

with Booking() as bot:
    bot.first_page()
    bot.place_to_go('Jeddah')
    bot.check_in_out('2023-02-13','2023-02-17')
    bot.No_of_Adults(3)
    bot.click_search()
    bot.apply_filtrations()
    bot.report_data()