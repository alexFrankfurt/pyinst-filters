Instagram-filters
=================

Instagram-like image filters.(based on [this work](https://github.com/acoomans/instagram-filters))

Can be used in conjunction with the [instagram-client](https://bitbucket.org/acoomans/instagram-client) to upload the image after applying a filter.

## Dependencies

Instagram-filters depends on ImageMagick, which can be installed on a Mac with brew:
```sh
	brew install imagemagick
```
## Install
```sh
	python setup.py install
```

## Usage

First, import the client:
```python
	from instagram_filters.filters.gotham import Gotham
```
Instanciate a filter and apply it:
```python
	f = Gotham("image.jpg")
	f.apply()
```
Available filters:

- Gotham
- Kelvin
- Lomo
- Nashville
- Toaster

**Note** The filters change the image in-place. Be sure to copy it before applying any filter if you want to copy the original image.


# Tests

Run the tests with (currently doesn't work):
```sh
	cd tests
	python test.py
```
## Credits

This library is inspired from the ["Create instagram filters with php" tutsplus tutorial](http://net.tutsplus.com/tutorials/php/create-instagram-filters-with-php/).
