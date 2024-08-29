import dash_mantine_components as dmc

component = dmc.Carousel([
    dmc.CarouselSlide(dmc.Center("Slide 1", bg="blue", c="white", p=30)),
    dmc.CarouselSlide(dmc.Text("Slide 2", bg="blue", c="white", p=30)),
    dmc.CarouselSlide(dmc.Text("Slide 3", bg="blue", c="white", p=30))
], id="carousel-simple")