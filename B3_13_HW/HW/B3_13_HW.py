def main(output=None):
    class Tag:
        def __init__(self, tag, is_single=False, klass=None, **kwargs):
            self.tag = tag
            self.text = ""
            self.attributes = {}
            self.is_single = is_single
            self.children = []
            if klass is not None:
                self.attributes[" class"] = " ".join(klass)
            for attr, value in kwargs.items():
                if "_" in attr:
                    attr = attr.replace("_", "-")
                self.attributes[attr] = value

        def __enter__(self, *args, **kwargs):
            return self

        def __iadd__(self, other):
            self.children.append(other)
            return self

        def __str__(self):
            attrs = []
            for attribute, value in self.attributes.items():
                attrs.append('%s="%s"' % (attribute, value))
            attrs = " ".join(attrs)
            if len(self.children) > 0:
                opening = f"<{self.tag}{attrs}>\n"
                if self.text:
                    internal = "%s" % self.text
                else:
                    internal = ""
                for child in self.children:
                    internal += str(child)
                ending = "</%s>\n" % self.tag
                return opening + internal + ending
            else:
                if self.is_single:
                    return f"<{self.tag} {attrs}/>\n"
                else:
                    return f"<{self.tag}{attrs}>{self.text}</{self.tag}>\n"

        def __exit__(self, *args, **kwargs):
            pass

    class HTML:
        def __init__(self, output=None):
            self.output = output
            self.childrens = []

        def __enter__(self):
            return self

        def __add__(self, other):
            self.childrens.append(other)
            return self

        def __str__(self):
            opening = "<html>\n"
            internal = ""
            for child in self.childrens:
                internal += str(child)
            ending = "</html>"
            return opening + internal + ending

        def __exit__(self, *args, **kwargs):
            if self.output is not None:
                with open(self.output, "a") as fp:
                    fp.write(str(self))
            else:
                print(self)

    class TopLevelTag:
        def __init__(self, tag):
            self.tag = tag
            self.childrens = []

        def __enter__(self):
            return self

        def __add__(self, other):
            self.childrens.append(other)
            return self

        def __str__(self):
            opening = f"<{self.tag}>\n"
            internal = ""
            for child in self.childrens:
                internal += str(child)
            ending = f"</{self.tag}>\n"
            return opening + internal + ending

        def __exit__(self, *args):
            return self

    with HTML(output=output) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png") as img:
                    div += img

                body += div

            doc += body
            print(doc) # for review


if __name__ == "__main__":
    main("../../data/B3_HW.html")