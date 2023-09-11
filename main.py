
def builder(tag):
    return f"<{tag}_>:</{tag}>"

def cleaner(tag):
    tag = tag.replace(":", "")
    return tag.replace("_", "")

class Html:
    def html(self):
        name = "html"
        return builder(name)
    

    def div(self, data, child=None, classname=None, idname=None):
        name = "div"
        _tag = builder(name)
        if child and data:
            _tag = _tag.replace(":", f"{child} {data}")
            if data:
                _tag = _tag.replace(":", data)

        if classname:
            _tag = _tag.replace("_", f' class="{classname}"')
        tag = cleaner(_tag)
        return tag


app = Html()

print(app.div())
