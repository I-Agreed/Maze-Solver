from PIL import Image

Input = "maze.png"
def make(Input):
    colourMap = {"#FF0000": "x",
                "#FFFFFF": ".",
                "#0000FF": "o",
                "#000000": "#",
                "default": "."}

    toHex = lambda colour: "#" + "".join([hex(i)[2:].upper()+"0"*(2-len(hex(i)[2:])) for i in colour])

    img = Image.open(Input)
    width = img.size[0]
    data = list(img.getdata())
    maze = []
    maze.append([])
    for i in range(len(data)):
        colour = data[i]
        if i != 0 and i % width == 0:
            maze.append([])
        hexColour = toHex(colour)
        if hexColour in colourMap:
            maze[-1].append(colourMap[hexColour])
        else:
            maze[-1].append(colourMap["default"])
    return maze
