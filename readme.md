# FLAME GPU Website

This repository contains the source for the FLAME GPU website, built with [Jekyll](https://jekyllrb.com/), and using the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

The website is hosted on GitHub Pages and can be found at [https://flamegpu.github.io](https://flamegpu.github.io).

## Development

### Install Dependencies

1. Install Ruby
    * On Windows, this installer can be used [https://rubyinstaller.org/](https://rubyinstaller.org/)
    * On Linux, follow the instructions according to your distribution e.g. for Debian/Ubuntu:
        ```sh
        sudo apt install ruby-full
        ```
2. Install `bundler` (via a terminal):
   ```sh
   gem install bundler jekyll
   ```
3. Install other dependencies:
    ```sh
    cd path/to/clone/of/this/repo
    bundle config set path vendor/bundle
    bundle install
    ```

**Note:** if you get an error related to the `public_suffix` package, try installing and updating bundler before rebuilding the site:

```sh
gem install public_suffix --version 3.0.3
bundler update
```

### Updating Dependencies

Ensure ruby packages are up to date, to avoid differences between local and GitHub/GitHub Actions builds:

```sh
bundle update --all
```

### Serving a Local Copy of the Website

To build and serve a local copy of the website, run

```sh
bundle exec jekyll serve
```

The website can then be found at `http://127.0.0.1:4000`

Note that if you are running Ruby 2.7 then you [will see lots of deprecation warnings until Jekyll 4.1 is released](https://github.com/jekyll/jekyll/pull/7948#issuecomment-584132037).

### Building HTML files

```sh
bundle exec jekyll build
```

Generated HTML files can be found in `_site`.
