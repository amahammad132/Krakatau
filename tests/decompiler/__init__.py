# Mapping from test name -> tuple of argument lists.
registry = {
    "ArgumentTypes": (["42", "false"], ["43", "true"], ["1", "1", "1"]),
    "ArrayTest": ([], ["x"]),
    "BoolizeTest": ([],),
    "ClinitFlagsTest": ([],),
    "ConditionalTest": ([],),
    "ControlFlow": (
        [],
        [".Na", "q"],
        ["ddKK", "-2"],
        ["hB7X", "-1"],
        ["R%%X", "0", "0"],
        [">OE=.K", "#FF"],
        ["95", " ", "x", "x"],
        ["Hello, Word!"],
    ),
    "DoubleEdge": ([], ["x"]),
    "DuplicateInit": ([], ["5", "-7"], ["x", "x", "x"]),
    "ExceptionHandlers": tuple([str(x)] for x in range(-1, 12)),
    "For": ([],),
    "floattest": ([],),
    "JSRTests": ([], ["x"], ["x", "x", "x", "x"]),
    # 'LClassLiteralTest': ([],), # JVM 9 no longer accepts weird class literals
    # 'NonexistentCheckcast': ([],),
    "NullInference": ([], ["alice"], ["bob", "carol"]),
    "OddsAndEnds": ([], ["x"], ["42"], ["4"], ["-2"], ["-0x567"], ["-5678"]),
    "splitnew": (
        [],
        ["-0"],
        ["-0", ""],
        ["-0", "", "", ""],
        ["-0", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ),
    "SamSunTests": ([],),
    "StaticInitializer": ([],),
    "SwapLoopTest": (["Hello, World!"], ["Hello,", "World!"]),
    "Switch": (
        [],
        ["0"],
        ["0", "1"],
        ["0", "1", "2"],
        ["0", "1", "2", "3"],
        ["0", "1", "2", "3", "4"],
    ),
    "Synchronized": ([], [""], ["", "", "", ""]),
    "TryCatchTest": (
        [],
        ["bad"],
        ["bad", "boy"],
        ["good"],
        ["f"],
        ["=", "="],
        ["<<", "<", ":", ">", ">>"],
    ),
    "TryWithResources": ([],),
    "UnicodeTest": ([],),
    "WhileLoops": (
        [],
        ["#9"],
        ["x", "x"],
        ["x", "xx", "x"],
        ["The", "Quick", "Brown", "Fox", "Jumped", "Over", "The", "Lazy", "Dogs."],
        ["46", "08"],
        ["4608"],
    ),
}
