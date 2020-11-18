# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs on our [issue tracker][gh-issues].

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through [the GitHub issues][gh-issues] for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Django TinyMCE Widget could always use more documentation, whether as part of the official Django TinyMCE Widget docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to [file an issue][gh-issues].

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `django-tinymce4-widget` for local development.

1.  Fork the `django-tinymce4-widget` repo on GitHub.

2.  Clone your fork locally:

    ```shell
    $ git clone git@github.com:your_name_here/django-tinymce4-widget.git
    ```

3.  Make sure you have [Poetry] installed, and from the root of the project run:

    ```shell
    $ poetry install -E docs -E spellcheck
    ```

    This will install all the needed dependencies for development in an isolated environment.

4.  Create a branch for local development:

    ```shell
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass the tests:

    ```shell
    $ poetry run manage.py test test_tinymce
    ```

6.  To make sure your change passes linting, install the [pre-commit] hooks:

    ```shell
    $ pre-commit install
    ```

7.  Commit your changes and push your branch to GitHub:

    ```shell
    $ git add .
    $ git commit -m "feat(something): your detailed description of your changes"
    $ git push origin name-of-your-bugfix-or-feature
    ```

    Note: the commit message should follow [the conventional commits guidelines][con-commits], this is to enable the automation of releases. We run [`commitlint` on CI][commit-lint] which will validate the commit messages.

8.  Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
3.  The pull request should work for our supported versions of Python and Django. Check the build on Github and make sure that the tests pass for all combinations.

## Deploying

The deployment should be automated and can be triggered from the Semantic Release workflow in Github. The next version will be based on the commit messages. This is done by [python-semantic-release][psr] via a Github action.

[gh-issues]: https://github.com/browniebroke/django-tinymce4-widget/issues
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[con-commits]: https://www.conventionalcommits.org
[commit-lint]: https://github.com/marketplace/actions/commit-linter
[psr]: https://python-semantic-release.readthedocs.io
