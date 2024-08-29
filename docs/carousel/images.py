import dash_mantine_components as dmc

images = [
  'https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png',
  'https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-2.png',
  'https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png',
  'https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-4.png',
  'https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-5.png',
]

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Image("Slide 1", src=image))
        for image in images
    ],
    id="carousel-images",
    withIndicators=True,
    w=400
)