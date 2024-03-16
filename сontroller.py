from view import MainWindow


class Controller:
    w = MainWindow()

    def Check(self):
        if w.the_button_was_toggled() == True:
            return "ok"
        else:
            return "ne ok"


if __name__ == "__main__":
    c = Controller()
    checker = c.Check()
    print(checker)
