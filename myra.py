from seleniumbase import SB

with SB(uc=True, test=True) as myra:

    if True:
        url = "https://kick.com/brutalles"
        myra.uc_open_with_reconnect(url, 5)
        myra.uc_gui_click_captcha()
        myra.sleep(1)
        myra.uc_gui_handle_captcha()
        myra.sleep(1)
        if myra.is_element_present('button:contains("Accept")'):
            myra.uc_click('button:contains("Accept")', reconnect_time=4)
        if myra.is_element_visible('#injected-channel-player'):
            myra2 = myra.get_new_driver(undetectable=True)
            myra2.uc_open_with_reconnect(url, 5)
            myra2.uc_gui_click_captcha()
            myra2.uc_gui_handle_captcha()
            myra.sleep(10)
            if myra2.is_element_present('button:contains("Accept")'):
                myra2.uc_click('button:contains("Accept")', reconnect_time=4)
            while myra.is_element_visible('#injected-channel-player'):
                myra.sleep(10)
            myra.quit_extra_driver()
    myra.sleep(1)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        myra.uc_open_with_reconnect(url, 5)
        if myra.is_element_present('button:contains("Accept")'):
            myra.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            myra2 = myra.get_new_driver(undetectable=True)
            myra2.uc_open_with_reconnect(url, 5)
            myra.sleep(10)
            if myra2.is_element_present('button:contains("Accept")'):
                myra2.uc_click('button:contains("Accept")', reconnect_time=4)
            while myra.is_element_visible(input_field):
                myra.sleep(10)
            myra.quit_extra_driver()
    myra.sleep(1)
