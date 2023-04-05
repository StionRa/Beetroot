#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words_decorator(stop_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Convert stop words to set for faster lookup
            stop_words_set = set(stop_words)

            # Call the decorated function and replace stop words with asterisks
            result = func(*args, **kwargs)
            if isinstance(result, str):
                words = result.split()
                masked_words = [w.lower() if w not in stop_words_set else '*'*len(w) for w in words]
                return ' '.join(masked_words)
            else:
                return result

        return wrapper
    return decorator
@stop_words_decorator(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW"
print(create_slogan('Stas'))