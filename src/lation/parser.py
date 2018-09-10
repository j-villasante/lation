from py_mini_racer import py_mini_racer


def parse_js(file_name: "str"):
    file = open(file_name, "r", encoding="utf-8")
    code = file.read()
    file.close()

    exported = "exported"
    ctx = py_mini_racer.MiniRacer()
    ctx.eval(code.replace("export default", f"{exported} ="))
    return ctx.eval(exported)
