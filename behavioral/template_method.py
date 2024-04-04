from abc import ABC, abstractmethod


class WebPage(ABC):
    @abstractmethod
    def render_header(self):
        raise NotImplementedError()

    @abstractmethod
    def render_body(self):
        raise NotImplementedError()

    @abstractmethod
    def render_footer(self):
        raise NotImplementedError()


class WebTemplate:
    def render_header(self):
        print("This is header")

    def render_footer(self):
        print("This is footer")


class HomePage(WebTemplate):
    def render_body(self):
        print("This is body of home page")


class ProductPage(WebTemplate):
    def render_body(self):
        print("This is body of product page")


class RenderWebite:
    _website: WebPage

    def __init__(self, website):
        self._website = website

    def render(self):
        self._website.render_header()
        self._website.render_body()
        self._website.render_footer()


if __name__ == "__main__":
    home_page = HomePage()
    render_website = RenderWebite(home_page)
    render_website.render()

    print("======================================")

    product_page = ProductPage()
    render_website = RenderWebite(product_page)
    render_website.render()
