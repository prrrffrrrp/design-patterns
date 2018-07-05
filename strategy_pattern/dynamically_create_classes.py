def constructor(self, arg1):
    self.constructor_arg = arg1


def some_func(self, arg1):
    print(arg1)


@classmethod
def some_class_method(cls, arg1):
    print("{} - arg1: {}".format(cls.__name__, arg1))


NewClass = type("NewClass", (object,), {
    "string_val": "this is val1",
    "int_val": 10,
    "__init__": constructor,
    "func_val": some_func,
    "class_func": some_class_method})


instance = NewClass("constructor arg")
print(instance.constructor_arg)
print(instance.string_val)
print(instance.int_val)
instance.func_val("test")
NewClass.class_func("test")
