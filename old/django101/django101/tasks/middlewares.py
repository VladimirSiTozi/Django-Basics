import time


def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        print(f'Before view - {start_time}')
        result = get_response(request, *args, **kwargs)

        end_time = time.time()
        print(f'After view - {end_time}')

        print(f'Request took {end_time - start_time} seconds')
        return result

    return middleware