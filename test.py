def test(*args, **kwargs):
    for arg in args:
        print(arg)
    if 'file_name' in kwargs:
        print(kwargs['file_name'])


test('temp', 'sea_pressure')