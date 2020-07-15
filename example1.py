from Settings1 import wd,url

class webrowsercmd():
    def wbget(self):
        wd.get(url)

        titleName = print(wd.title)
        print(wd.current_url)
        print(wd.current_url1)
        print((wd.get_window_position()))
        print(wd.get_window_rect())
        position=wd.get_window_position()
        print(position)
        updt_pos=wd.set_window_position(position['x']+100,position['y']+100)
        wd.refresh()
        import time
        time.sleep(1)
        wd.back()
        wd.forward()
        wd.fullscreen_window()



obj=webrowsercmd()
obj.wbget()

