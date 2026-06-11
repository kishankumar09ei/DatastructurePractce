class cookie:
    def __init__(self,color):
        self.color=color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color=color

cookie1=cookie("blue")

print(f"cookie1 color by default is :{cookie1.get_color()}")

cookie1.set_color("green")
print(f"cookie1 color by new after set is :{cookie1.get_color()}")
