preheat_oven = lambda: print('Preheating oven')
put_croissants_in = lambda: print('Putting croissants in')
wait_five_minutes = lambda: print('Waiting five minutes')
take_croissants_out = lambda: print('Take croissants out and enjoy them!')

# (1) Execute the four steps in order
print('Option one ...')
preheat_oven()
put_croissants_in()
wait_five_minutes()
take_croissants_out()

# (2) Launcher function
print('Option two ...')
def make_croissants(*funcs):
    for func in funcs:
        func()


make_croissants(
    preheat_oven,
    put_croissants_in,
    wait_five_minutes,
    take_croissants_out)       


# (3) Recipe function
print('Option three ...')
def create_recipe(*funcs):
    def run_all():
        for func in funcs:
            func()

    return run_all

recipe = create_recipe(
    preheat_oven,
    put_croissants_in,
    wait_five_minutes,
    take_croissants_out)

recipe()      