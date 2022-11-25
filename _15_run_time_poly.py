class black_n_white_tv:
    def color(self):
        print("Black and white")

    def video(self):
        print("480")

    def shape(self):
        print("Square")

class colored_tv(black_n_white_tv):
    def screen(self):
        print("Screen")

    def color(self):
        print("Colored")

obj = colored_tv()
obj.screen()
obj.shape()
obj.color()
obj.video()
