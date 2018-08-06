black:
	find test_tinymce/ tinymce/ -name "*.py" | xargs black

lint:
	flake8
	find test_tinymce/ tinymce/ -name "*.py" | xargs black --check
