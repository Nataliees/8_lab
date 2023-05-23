def first():
    from PIL import Image

    img = Image.open("postcard.jpg")
    img = img.crop((30, 30, int(img.width / 2), int(img.height / 2)))
    img.save("newpostcard.jpg")

def second():
    from PIL import Image
    holidays = {1: "bd.jpg", 2: "ny.jpeg", 3: "christ.jpg"}
    print("1 - Birthday \n"
          "2 - New Year \n"
          "3 - Christmas")
    num = int(input("Choose the number for getting a postcard: "))
    filename = holidays[num]
    with Image.open(filename) as img:
        img.load()

    img.show()

def third():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Write the name ")
    filename = "bd.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("Roboto-Bolditalic.ttf", 52)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 3.3, 150),
        "Dear " + name + "\n Happy",
        font=font,
        fill='white'
    )
    img.show()
    img.save(name + "bd.png")
third()