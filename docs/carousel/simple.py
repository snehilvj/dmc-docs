import dash_mantine_components as dmc

component = dmc.Carousel([
    dmc.CarouselSlide(dmc.Text("Slide 1", ta="center", bg="blue", c="white", p=30)),
    dmc.CarouselSlide(dmc.Text("Slide 2", ta="center", bg="blue", c="white", p=30)),
    dmc.CarouselSlide(dmc.Text("Slide 3", ta="center", bg="blue", c="white", p=30))
], id="carousel-simple")