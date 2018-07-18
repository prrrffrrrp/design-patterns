class WindowBase(object):
    def show(self):
        print("Show", self.__class__ .__name__)

    def hide(self):
        print("Hide", self.__class__.__name__)


class MainWindow(WindowBase):
    pass


class SettingsWindow(WindowBase):
    pass


class HelpWindow(WindowBase):
    pass


class WindowMediator(object):
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'settings', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_settings(self, win):
        self.windows['settings'] = win

    def set_help(self, win):
        self.windows['help'] = win


main_win = MainWindow()
settings_win = SettingsWindow()
help_win = HelpWindow()

med = WindowMediator()

med.set_main(main_win)
med.set_settings(settings_win)
med.set_help(help_win)

med.show(settings_win)
med.show(help_win)
