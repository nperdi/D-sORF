##sklearn_ver.py

# import sys
# # import nltk
# import sklearn

# print(f'The Python  version is {sys.version}.',)
# # print(f'The nltk version is {format(nltk.__version__)}.')
# print(f'The scikit-learn version is {format(sklearn.__version__)}.')

try:
    import sys
    print(f'Python  version is {sys.version}.',)
except ImportError:
    print ('Python is not installed, installing it now!')
    # install('')

try:
    import sklearn
    print(f'The scikit-learn version is {format(sklearn.__version__)}.')
except ImportError:
    print ('sklearn is not installed, installing it now!')
    # install('')
    


try:
    import nltk
    print(f'The nltk version is {format(nltk.__version__)}.')
except ImportError:
    print ('nltk is not installed, installing it now!')
    # install('')